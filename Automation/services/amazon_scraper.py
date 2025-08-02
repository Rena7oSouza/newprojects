from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

class AmazonScraper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("window-size=1920,1080")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )

        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)

    def scrape_product(self, product_name: str) -> dict:
        try:
            search_url = f'https://www.amazon.com.br/s?k={product_name.replace(" ", "+")}'
            self.driver.get(search_url)
            time.sleep(5)

            # Accept cookies if popup is shown
            try:
                self.driver.find_element(By.ID, "sp-cc-accept").click()
                time.sleep(1)
            except:
                pass

            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            results = soup.select('div[data-component-type="s-search-result"]')
            for result in results: #remove or comment this for if must show sponsored items
                if result.find(string=lambda text: text and "Patrocinado" in text):
                    continue  
                else:
                    break  
            else:
                result = None  

            if not result:
                return {
                    'name': product_name,
                    'price': '',
                    'title': '',
                    'status': 'Failure',
                    'obs': 'No results found'
                }

            title_tag = result.select_one("h2 span")
            title = title_tag.text.strip() if title_tag else 'Title not found'

            price_whole = result.select_one("span.a-price-whole")
            price_fraction = result.select_one("span.a-price-fraction")
            if price_whole and price_fraction:
                price = f"{price_whole.text.strip()}{price_fraction.text.strip()}"
            else:
                price = "Price not found"

            return {
                'name': product_name,
                'price': price,
                'title': title,
                'status': 'Success',
                'obs': ''
            }

        except Exception as e:
            return {
                'name': product_name,
                'price': '',
                'title': '',
                'status': 'Failure',
                'obs': str(f"Error! {e}")
            }

    def process_products(self, names: list[str]) -> list[dict]:
        results = []
        for name in names:
            result = self.scrape_product(name)
            results.append(result)
        return results

    def __del__(self):
        # Make sure browser closes
        self.driver.quit()

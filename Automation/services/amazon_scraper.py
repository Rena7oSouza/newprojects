from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup

class AmazonScraper:
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("window-size=1920,1080")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )
        self.driver = webdriver.Chrome(options=chrome_options)

    def scrape_product(self, product_name: str) -> dict:
        try:
            search_url = f'https://www.amazon.com.br/s?k={product_name.replace(" ", "+")}'
            self.driver.get(search_url)
            time.sleep(5)  # um pouco mais para garantir o carregamento

            # Aceitar cookies se aparecer (ou faça isso no __init__)
            try:
                self.driver.find_element(By.ID, "sp-cc-accept").click()
                time.sleep(1)
            except:
                pass

            # Usa BeautifulSoup para analisar o HTML da página renderizada
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            # Busca o primeiro resultado válido (igual seu código que funciona)
            resultado = soup.select_one('div[data-component-type="s-search-result"]')

            if not resultado:
                return {
                    'name': product_name,
                    'price': '',
                    'title': '',
                    'status': 'Falha',
                    'obs': 'Nenhum resultado encontrado na página'
                }

            titulo_tag = resultado.select_one("h2 span")
            titulo = titulo_tag.text.strip() if titulo_tag else ''

            preco_whole = resultado.select_one("span.a-price-whole")
            preco_frac = resultado.select_one("span.a-price-fraction")
            if preco_whole and preco_frac:
                preco = f"R$ {preco_whole.text.strip()},{preco_frac.text.strip()}"
            else:
                preco = 'Preço não encontrado'

            return {
                'name': product_name,
                'price': preco,
                'title': titulo,
                'status': 'Sucesso',
                'obs': ''
            }

        except Exception as e:
            return {
                'name': product_name,
                'price': '',
                'title': '',
                'status': 'Falha',
                'obs': str(e)
            }
    def process_products(self, names: list[str]) -> list[dict]:
        results = []
        for name in names:
            result = self.scrape_product(name)
            results.append(result)
        return results
    def __del__(self):
        self.driver.quit()

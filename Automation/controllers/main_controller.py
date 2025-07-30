from models.excel_handler import ExcelHandler
from services.amazon_scraper import AmazonScraper

def run():
    filepath = r'C:\Arquivos_Teste\Template_Planilha_Teste.xlsx'

    # Initialize handlers
    excel = ExcelHandler(filepath)
    scraper = AmazonScraper()

    # Load product names from Excel
    product_names = excel.get_product_names()

    # Scrape products from Amazon
    results = scraper.process_products(product_names)

    # Update Excel with scraped data
    excel.update_product_data(results)

    # Print results to terminal
    print("✔ Finished: Data successfully written to Excel.")

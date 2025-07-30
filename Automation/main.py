from services.excel_handler import ExcelHandler
from services.amazon_scraper import AmazonScraper

def main():
    filepath = r'C:\Arquivos_Teste\Template_Planilha_Teste.xlsx'  # caminho do Excel
    excel = ExcelHandler(filepath)
    scraper = AmazonScraper()

    product_names = excel.get_product_names()
    results = scraper.process_products(product_names)

    # Atualiza planilha
    excel.update_product_data(results)

    # Imprime resultados no console
    for res in results:
        print(f"🔎 Produto: {res['name']}")
        print(f"Título: {res['title']}")
        print(f"Preço: {res['price']}")
        print(f"Status: {res['status']}")
        if res['obs']:
            print(f"Observação: {res['obs']}")
        print("-" * 60)

    print("✔ Finalizado: dados atualizados na planilha.")

if __name__ == "__main__":
    main()

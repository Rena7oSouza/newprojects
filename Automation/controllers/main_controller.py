from models.excel_handler import ExcelHandler
from services.amazon_scraper import AmazonScraper
from services.rdp_automation import RDPAutomation
from services.tn5250j_automation import TN5250JAutomation

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

    # Send connection infos
    rdp = RDPAutomation(
        dns='ec2-18-228-38-143.sa-east-1.compute.amazonaws.com',
        rdp_user='Administrator',
        rdp_pass='BP4ProcessoSeletivo!2025'
    )

    # Connect and run RDP
    rdp.run()

    #Send login infos
    tn5250j = TN5250JAutomation(user= "BPAPS06",
                                password= "bp4ps25")
    
    #Run TN5250J automation
    tn5250j.run(excel)

def testing():#exclude
     # Send connection infos
    rdp = RDPAutomation(
        dns='ec2-18-228-38-143.sa-east-1.compute.amazonaws.com',
        rdp_user='Administrator',
        rdp_pass='BP4ProcessoSeletivo!2025'
    )

    # Connect and run RDP
    rdp.run()

    #Send login infos
    tn5250j = TN5250JAutomation(user= "BPAPS06",
                                password= "bp4ps25")
    filepath = r'C:\Arquivos_Teste\Template_Planilha_Teste.xlsx'

    # Initialize handlers
    excel = ExcelHandler(filepath)
    #Run TN5250J automation
    tn5250j.run(excel)

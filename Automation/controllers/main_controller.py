from models.excel_handler import ExcelHandler
from services.amazon_scraper import AmazonScraper
#from services.rdp_automation import RDPAutomation
from services.tn5250j_automation import TN5250JAutomation
from config import (
    FILEPATH_EXCEL, TN5250J_PATH,
    RDP_DNS, RDP_USER, RDP_PASS,
    TN5250J_USER, TN5250J_PASS
)

def run():
    # Initialize Excel and scraper handlers
    excel = ExcelHandler(FILEPATH_EXCEL)
    scraper = AmazonScraper()

    # Retrieve product names from Excel file
    product_names = excel.get_product_names()

    # Scrape product information from Amazon based on the product names
    results = scraper.process_products(product_names)

    # Write the scraped data back to the Excel file
    excel.update_product_data(results)

    # Initialize RDP automation with server credentials
    #rdp = RDPAutomation(
    #    dns=RDP_DNS,
    #    rdp_user=RDP_USER,
    #    rdp_pass=RDP_PASS
    #)

    # Establish RDP connection and execute remote operations
    #rdp.run()

    # Initialize TN5250J automation with login credentials
    tn5250j = TN5250JAutomation(
        user=TN5250J_USER,
        password=TN5250J_PASS
    )
    
    # Launch the TN5250J terminal and perform automated actions using Excel data
    tn5250j.run(TN5250J_PATH, excel)

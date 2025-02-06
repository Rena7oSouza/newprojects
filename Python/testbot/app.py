

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Especificando o caminho do chromedriver corretamente
service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.pokemon-vortex.com')

# Agora você pode continuar com o código do bot

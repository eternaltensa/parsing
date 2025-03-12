from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
sites=[

"link1",
"link2",
"link3"



]
for site in sites:

        driver.get(site)
        try:
            script= driver.find_element(By.CSS_SELECTOR,'[src=""]')
            print(f'{site}     OK')
        except:
            print(f'{site}')


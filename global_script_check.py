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




        # wp_parent=driver.find_element(By.CSS_SELECTOR,'[data-gtag-click="whatsapp"]')
        # wp=wp_parent.get_attribute('href')
        # try:
        #     tg_parent=driver.find_element(By.CSS_SELECTOR,'[data-gtag-click="telegram"]')
        #     tg=tg_parent.get_attribute('href')
        #     try:
        #         phone_parent=driver.find_element(By.CSS_SELECTOR,'.phone-replace-only')
        #         phone_parent.click()
        #         phone= phone_parent.get_attribute('href')
        #         print(f'{site}       {tg}       {wp}       {phone}')
        #     except:
        #         phone_parent = driver.find_element(By.CSS_SELECTOR, '.phone-replace')
        #         phone_parent.click()
        #         phone = phone_parent.get_attribute('href')
        #         print(f'{site}       {tg}       {wp}       {phone}')
        # except:
        #     try:
        #         phone_parent=driver.find_element(By.CSS_SELECTOR,'.phone-replace-only')
        #         phone_parent.click()
        #         phone= phone_parent.get_attribute('href')
        #         print(f'{site}       {tg}       {wp}       {phone}')
        #     except:
        #         phone_parent = driver.find_element(By.CSS_SELECTOR, '.phone-replace')
        #         phone_parent.click()
        #         phone = phone_parent.get_attribute('href')
        #         print(f'{site}       {tg}       {wp}       {phone}')

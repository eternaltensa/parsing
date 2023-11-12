from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
sites=[

"https://sales-inquiries.ae/axcapital/damac-lagoons-morocco/",
"https://sales-inquiries.ae/axcapital/damac-lagoons-morocco/ru",
"https://sales-inquiries.ae/axcapital/julphar-residence/",
"https://sales-inquiries.ae/axcapital/julphar-residence/ru",
"https://sales-inquiries.ae/axcapital/oasis/",
"https://sales-inquiries.ae/axcapital/oasis/ru",
"https://sales-inquiries.ae/axcapital/the-source-2/",
"https://sales-inquiries.ae/axcapital/the-source-2/ru",
"https://sales-inquiries.ae/axcapital/sunridge/",
"https://sales-inquiries.ae/axcapital/sunridge/ru",
"https://sales-inquiries.ae/axcapital/rivana/",
"https://sales-inquiries.ae/axcapital/rivana/ru",
"https://sales-inquiries.ae/axcapital/rixos-by-nakheel/",
"https://damac-bay-2.ae/",
"https://district-west-villas.ae/",
"https://palace-residences-north.ae/"



]
for site in sites:

        driver.get(site)
        try:
            script= driver.find_element(By.CSS_SELECTOR,'[src="https://fnst.axflare.com/landings/global-script/landings-global-script.js"]')
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

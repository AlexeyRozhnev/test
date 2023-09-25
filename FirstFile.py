import time
import os
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}"
}
chrome_options.add_experimental_option("prefs",prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://www.rpachallenge.com")
time.sleep(5)
driver.find_element("xpath", "//a[text()=' Download Excel ']").click()
time.sleep(10)
driver.find_element("xpath", "//button[text() ='Start']").click()
time.sleep(3)
df=pd.read_excel('challenge.xlsx')
for i, row in df.iterrows():
    FirstNameInput = driver.find_element("xpath", "//input[@ng-reflect-name='labelFirstName']")
    LastNameInput = driver.find_element("xpath", "//input[@ng-reflect-name='labelLastName']")
    CompanyInput = driver.find_element("xpath", "//input[@ng-reflect-name='labelCompanyName']")
    RoleInput = driver.find_element("xpath", "//input[@ng-reflect-name='labelRole']")
    AddressInput = driver.find_element("xpath", "//input[@ng-reflect-name='labelAddress']")
    EmailInput = driver.find_element("xpath", "//input[@ng-reflect-name='labelEmail']")
    PhoneInput = driver.find_element("xpath", "//input[@ng-reflect-name='labelPhone']")

    FirstNameInput.send_keys(row['First Name'])
    LastNameInput.send_keys(row['Last Name '])
    CompanyInput.send_keys(row['Company Name'])
    RoleInput.send_keys(row['Role in Company'])
    AddressInput.send_keys(row['Address'])
    EmailInput.send_keys(row['Email'])
    PhoneInput.send_keys(row['Phone Number'])
    driver.find_element("xpath", "//input[@value='Submit']").click()

time.sleep(5)
driver.save_screenshot("resuls.png")
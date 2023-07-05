from selenium import webdriver

import time 
from bs4 import BeautifulSoup
import pandas as pd

def browser_function():
    chr_driver = webdriver.Chrome()
    
    chr_driver.get("hello/login")
    xpath1 = "//*[@id = 'username']"
    xpath2 = "//*[@id = 'password']"
    xpath3 = "(//*[text()='Sign in'])[3]/.."
    xpath4= "//*[@id='entity-menu']"
    xpath5 = "(//*[text()='Game Info'])"
    xpath6 = "(//*[@class='table'])[1]"
    username = chr_driver.find_element("xpath",xpath1)
    username.send_keys('admin')
    time.sleep(1)
    passw = chr_driver.find_element("xpath",xpath2)
    passw.send_keys('123456**')
    time.sleep(2)
    passw.submit()
    time.sleep(3)
    ent = chr_driver.find_element("xpath",xpath4)
    ent.click()
    ent = chr_driver.find_element("xpath",xpath5)
    ent.click()
    time.sleep(2)
    table=chr_driver.find_element("xpath",xpath6)
    tablehtml= table.get_attribute('outerHTML')  # outerHTML ile hem açılış hem kapanış taglarını alıyoruz
    # BeautifulSoup ile HTML'i parse edelim
    soup = BeautifulSoup(tablehtml, "html.parser")
    # Pandas ile HTML tablosunu DataFrame'ye çevirelim
    df = pd.read_html(str(soup), header=0)[0]
    # İlk 6 satırı ve ilk 6 sütunu alalım
    df = df.iloc[:6, :6]
    # DataFrame'i CSV dosyasına kaydedelim
    df.to_csv("table.csv", index=False)
    print("CSV file created successfully.")
    
browser_function()


import pandas as pd

# CSV dosyasını okuyun
df = pd.read_csv('table.csv')

# Excel dosyasına yazın
df.to_excel('table.xlsx', index=False)

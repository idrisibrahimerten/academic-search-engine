# -*- coding: utf-8 -*-
"""
@author: IdrisIbrahimERTEN
"""

from  selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import requests


class academic_search_engine:
    def __init__(self):
        ######################### Constant Values #################################
        ######################### Sabit Değerler  #################################
        pass
        
    def initDriver(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            
        time.sleep(1)
    
    
    def dergipark(self, user_input, sayac):
        # print(" DERGİ PARK ")
        address = f"https://dergipark.org.tr/tr/search/{sayac}?q={user_input}&section=articles"
        url = requests.get(address)
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
    
        items = soup.findAll('h5', class_='card-title')
        link = []
        for item in items:
            data = []
            data.append(item.get_text())
            # print(item.get_text())
    
            text = str(item.findAll('a', href=True))
            index_start = text.index('href=')+6
            text = text[index_start:]
            index_end = text.index('\"')
    
            link.append(text[:index_end])
            # print(text[:index_end])
        return link
            
    def googleacademy(self, user_input, google_sayac):
        # print(" GOOGLE AKADEMİK ")
        address = f"https://scholar.google.com/scholar?start={google_sayac}&as_sdt=0%2C10&q=" + user_input
        url = requests.get(address)
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
    
        items = soup.findAll(class_='gs_r gs_or gs_scl')
        link_ = []
        for item in items:
            data = []
            data.append(item.get_text())
            # print(item.get_text())
        
            text = str(item.findAll('a', href=True))
            index_start = text.index('href=')+6
            text = text[index_start:]
            index_end = text.index('\"')
        
            link_.append(text[:index_end])
            # print(text[:index_end])
        return link_
            
    def sciencedirect(self, user_input, email, password):
        self.initDriver()
        self.driver.get("https://id.elsevier.com/as/authorization.oauth2?platSite=SD%2Fscience&scope=openid%20email%20profile%20els_auth_info%20els_idp_info%20els_idp_analytics_attrs%20els_sa_discover%20urn%3Acom%3Aelsevier%3Aidp%3Apolicy%3Aproduct%3Aindv_identity&response_type=code&redirect_uri=https%3A%2F%2Fwww.sciencedirect.com%2Fuser%2Fidentity%2Flanding&authType=SINGLE_SIGN_IN&prompt=login&client_id=SDFE-v3&state=retryCounter%3D0%26csrfToken%3D803fa8b8-c0d7-4298-a295-0fb07c90af2c%26idpPolicy%3Durn%253Acom%253Aelsevier%253Aidp%253Apolicy%253Aproduct%253Aindv_identity%26returnUrl%3D%252Fsearch%253Fqs%253Dbig%252520data%26prompt%3Dlogin%26cid%3Datp-e8df5c4a-62d2-458d-a836-bf2311bd3073&els_policy=idp_policy_indv_identity_plus")
        time.sleep(4)
        input_mail = self.driver.find_element("xpath", '/html/body/div/section/main/form/div[2]/div/input')
        input_mail.send_keys(email)
        input_mail.send_keys(Keys.ENTER)
        time.sleep(6)
        input_pass = self.driver.find_element("xpath",'/html/body/div/section/main/form/div[2]/div[2]/input')
        input_pass.send_keys(password)
        input_pass.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.get(f"https://www.sciencedirect.com/search?qs={user_input}")
        self.driver.refresh()
        time.sleep(5)
    
        sayac = 1
        sinir = 25
        link = []
        while True:
            for j in self.driver.find_element("xpath", f"//*[@data-rank='{sayac}']").get_attribute('href').split():
                link.append(j)
            sayac = sayac+1
            if sayac == sinir:
                break
        result = self.driver.find_element("id", "srp-results-list").text.split("Research article")
        
        data = []
        for i in result:
            data.append(i)
            
        data_ = []
        for a, b in zip(data, link):
            threadData = {"Makale Başlık": a, 
                          "Makale Link": b}
            data_.append(threadData)
            
        self.driver.close()
            
        return print(data_)
        
    def sayfa(self,user_input, page_num):
        sayac = 1
        google_sayac = 0
        while True:
            # print(sayac)
            # print(google_sayac)
            dergi_park = self.dergipark(user_input, sayac)
            google = self.googleacademy(user_input, google_sayac)
            google_sayac = google_sayac+10
            if sayac==page_num:
                break
            sayac = sayac+1
            # print(sayac)
            # print(google_sayac)
            
        data_ = []
        for a, b in zip(dergi_park, google):
            threadData = {"Dergi Park Link": a, 
                          "Google Akademik Link": b}
            data_.append(threadData)
        
        return print(data_)

# """ Test Alanı"""
# user_input = input("Makale Arayın : ")
# # eng_user_input = input("Makale Ara Eng : ")
# page_num = int(input("Kaç sayfa istiyorsunuz : "))

# """
# sciencedirect giriş
# """
# academy = academic_search_engine()

# academy.sayfa(user_input, page_num)

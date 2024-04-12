import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service


# noinspection PyDictCreation,PyPep8Naming
class HP_RERA:
    def __init__(self, url, driver_path):
        self.url = url
        self.driver_path = driver_path
        self.main_list = []

    def __enter__(self):
        self.service = Service(executable_path=self.driver_path)
        self.options = ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get(self.url)
        time.sleep(15)
        self.scrap_page()
        if all([self.main_list]):
            print('Main list to bn gyi iska mtlb')
            return self.main_list

    def scrap_page(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        main_content = soup.find('div', attrs={'id': 'tab_project_main-filtered-data'})
        rows_content = main_content.find_all('div', class_='shadow py-3 px-3 font-sm radius-3 mb-2')
        print(len(rows_content))

        list1 = []
        for i in rows_content:
            var = i.text.strip().split('\n')
            list1.append(var)

        for r in range(180):
            dict1 = {}
            dict1['Project Name'] = (list1[r][0])
            dict1['RERA ID'] = (list1[r][1])
            dict1['Project Type'] = (list1[r][3])
            dict1['Phone Number'] = ((list1[r][5]).strip(' :'))
            dict1['Email ID'] = ((list1[r][6]).strip(' :'))
            dict1['Address'] = ((list1[r][8]).strip())
            dict1['Valid Upto'] = (list1[r][12])
            self.main_list.append(dict1)
        print('loop to pura hogya mtlb')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit Function')
        pass

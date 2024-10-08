from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re
# import time

def link_grabber():
    subjects_stored = {
        'names': [],
        'links': [],
    }
    subject_biology = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
    subject_bc = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_English = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
    
    subject_CHEMISTRY = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    

    subject_CA = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }


    subject_psysical = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
    subject_Ancient_History = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
    subject_indian_geography = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
    subject_Modern_History = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
    physics = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
    
    afcat_special = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
    subject_polity = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }
   

    subject_index = [subject_biology, subject_bc, subject_English, subject_CHEMISTRY, subject_CA, subject_psysical, subject_Ancient_History, subject_indian_geography, subject_Modern_History, physics, afcat_special, subject_polity]

    opt = Options()
    # opt.add_experimental_option("debuggerAddress", "127.0.0.1:9222") 
    # opt.add_argument("--headless")
    
    driver = webdriver.Chrome(options=opt)
    # cookies = driver.get_cookies()

    # with open('cookies1.pkl', 'wb') as file:
    #     pickle.dump(cookies, file)
    driver.get('https://www.cdsjourney.com/student-dashboard/batch/13/subjects/')
    # driver.delete_all_cookies()
    cookies = pickle.load(open('cookies.pkl', 'rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get('https://www.cdsjourney.com/student-dashboard/batch/13/subjects/')
    #driver.refresh()

    subjects = driver.find_elements(By.XPATH, "//div[contains(@class, 'col-lg-2 col-md-2 mb-4')]")

    for subject in subjects:
        name = subject.find_element(By.TAG_NAME, 'a').find_element(By.TAG_NAME, 'img').get_attribute('alt')
        link = subject.find_element(By.TAG_NAME, 'a').get_attribute('href')
        subjects_stored['names'].append(name)
        subjects_stored['links'].append(link)

    ref = 0
    for subject_link in subjects_stored['links']:
        driver.get(subject_link)
        html_data = driver.page_source
        soup = BeautifulSoup(html_data, "html.parser")
        class_elements = soup.find_all("span", {"class": "btn btn-header-link"})
        for element in class_elements:
            class_name = element.find('p').text.replace('None', '').replace('\xa0','').strip(' ')
            class_date = element.find('h6').getText()
            if ref == 0:
                subject_biology['class_names'].append(class_name)
                subject_biology['class_date'].append(class_date)
            elif ref == 1:
                subject_bc['class_names'].append(class_name)
                subject_bc['class_date'].append(class_date)
            elif ref == 2:
                subject_English['class_names'].append(class_name)
                subject_English['class_date'].append(class_date)
            elif ref == 3:
                subject_CHEMISTRY['class_names'].append(class_name)
                subject_CHEMISTRY['class_date'].append(class_date)
            elif ref == 4:
                subject_CA['class_names'].append(class_name)
                subject_CA['class_date'].append(class_date)
            elif ref == 5:
                subject_psysical['class_names'].append(class_name)
                subject_psysical['class_date'].append(class_date)
            elif ref == 6:
                subject_Ancient_History['class_names'].append(class_name)
                subject_Ancient_History['class_date'].append(class_date)
            elif ref == 7:
                subject_indian_geography['class_names'].append(class_name)
                subject_indian_geography['class_date'].append(class_date)
            elif ref == 8:
                subject_Modern_History['class_names'].append(class_name)
                subject_Modern_History['class_date'].append(class_date)
            elif ref == 9:
                physics['class_names'].append(class_name)
                physics['class_date'].append(class_date)
            elif ref == 10:
                afcat_special['class_names'].append(class_name)
                afcat_special['class_date'].append(class_date)
            elif ref == 11:
                subject_polity['class_names'].append(class_name)
                subject_polity['class_date'].append(class_date)

        

        class_link_elements = soup.find_all("span", {"class": "btn btn-primary btn-sm radius-sm no-animation"})
        
        for link in class_link_elements:
            final_link = link.get("onclick").split('\'')[1]
            if ref == 0:
                subject_biology['class_link'].append(final_link)
            elif ref == 1:
                subject_bc['class_link'].append(final_link)
            elif ref == 2:
                subject_English['class_link'].append(final_link)
            elif ref == 3:
                subject_CHEMISTRY['class_link'].append(final_link)
            elif ref == 4:
                subject_CA['class_link'].append(final_link)
            elif ref == 5:
                subject_psysical['class_link'].append(final_link)
            elif ref == 6:
                subject_Ancient_History['class_link'].append(final_link)
            elif ref == 7:
                subject_indian_geography['class_link'].append(final_link)
            elif ref == 8:
                subject_Modern_History['class_link'].append(final_link)
            elif ref == 9:
                physics['class_link'].append(final_link)
            elif ref == 10:
                afcat_special['class_link'].append(final_link)
            elif ref == 11:
                subject_polity['class_link'].append(final_link)

        if ref > len(subject_index):
            break
        else:
            ref += 1


    # print(subject_indian_geography)
    subject_final = ['subject_biology', 'subject_bc', 'subject_English', 'subject_CHEMISTRY', 'subject_CA', 'subject_psysical', 'subject_Ancient_History', 'subject_indian_geography', 'subject_Modern_History', 'physics', 'afcat_special', 'subject_polity']
    numb = 0 
    for sub in subject_index:
        # print(len(sub['class_link']))
        # print(len(sub['class_names']))
        # print(len(sub['class_date']))
        # print("\n\n")
        df = pd.DataFrame(sub)
        df.to_csv(fr"info\{subject_final[numb]}.csv")
        numb += 1
# link_grabber()

# link_grabber()
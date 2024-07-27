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
    subject_indian_geography = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_Ancient_History = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_CHEMISTRY = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_biology = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_CA = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_English = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_bc = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_psysical = {
            'class_names': [],
            'class_date': [],
            'class_link': [],
    }

    subject_index = [subject_Modern_History, physics, subject_indian_geography, subject_Ancient_History, subject_CHEMISTRY, subject_biology, subject_CA, subject_English, subject_bc, subject_psysical]

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
        classes_elements = driver.find_elements(By.XPATH, "//span[contains(@class, 'btn btn-header-link')]")
        for class_element in classes_elements:
            class_name = class_element.find_element(By.TAG_NAME, 'p').text.rstrip('None').strip(' ')
            class_date = class_element.find_element(By.TAG_NAME, "h6").text
            if ref == 0:
                subject_Modern_History['class_names'].append(class_name)
                subject_Modern_History['class_date'].append(class_date)
            elif ref == 1:
                physics['class_names'].append(class_name)
                physics['class_date'].append(class_date)
            elif ref == 2: 
                subject_indian_geography['class_names'].append(class_name)
                subject_indian_geography['class_date'].append(class_date)
            elif ref == 3:
                subject_Ancient_History['class_names'].append(class_name)
                subject_Ancient_History['class_date'].append(class_date)
            elif ref == 4:
                subject_CHEMISTRY['class_names'].append(class_name)
                subject_CHEMISTRY['class_date'].append(class_date)
            elif ref == 5:
                subject_biology['class_names'].append(class_name)
                subject_biology['class_date'].append(class_date)
            elif ref == 6:
                subject_CA['class_names'].append(class_name)
                subject_CA['class_date'].append(class_date)
            elif ref == 7:
                subject_English['class_names'].append(class_name)
                subject_English['class_date'].append(class_date) 
            elif ref == 8:
                subject_bc['class_names'].append(class_name)
                subject_bc['class_date'].append(class_date)
            elif ref == 9:
                subject_psysical['class_names'].append(class_name)
                subject_psysical['class_date'].append(class_date)

        classes_links = driver.find_elements(By.XPATH, "//li[contains(@class, 'course-content')]")
        
        for class_link in classes_links:
            t_class_link = class_link.find_element(By.TAG_NAME, "span").get_attribute('onclick')
            pattern = r"https:\/\/us06web\.zoom\.us\/rec\/share\/[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+"
            final_link = re.findall(pattern, t_class_link)
            if ref == 0:
                subject_Modern_History['class_link'].append(final_link[0])
            elif ref == 1:
                physics['class_link'].append(final_link[0])
            elif ref == 2: 
                subject_indian_geography['class_link'].append(final_link[0])
            elif ref == 3:
                subject_Ancient_History['class_link'].append(final_link[0])
            elif ref == 4:
                subject_CHEMISTRY['class_link'].append(final_link[0])
            elif ref == 5:
                subject_biology['class_link'].append(final_link[0])
            elif ref == 6:
                subject_CA['class_link'].append(final_link[0])
            elif ref == 7:
                subject_English['class_link'].append(final_link[0])
            elif ref == 8:
                subject_bc['class_link'].append(final_link[0])  
            elif ref == 9:
                subject_psysical['class_link'].append(final_link[0])
        if ref > len(subject_index):
            break
        else:
            ref += 1


    # print(subject_indian_geography)
    subject_final = ['subject_Modern_History', 'physics', 'subject_indian_geography', 'subject_Ancient_History', 'subject_CHEMISTRY', 'subject_biology', 'subject_CA', 'subject_English', 'subject_bc', 'subject_geography']
    numb = 0 
    for sub in subject_index:
        df = pd.DataFrame(sub)
        df.to_csv(fr"info\{subject_final[numb]}.csv")
        numb += 1
link_grabber()
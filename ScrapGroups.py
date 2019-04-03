
import codecs

from time import sleep

import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrapGroups(kind_of_study, year_of_study):

    print('--> SCRAP GROUPS FOR SCHEDULE')

    options = Options()
    options.add_argument('headless')
    driver = selenium.webdriver.Chrome(options=options)
    driver.get("https://nastava.foi.hr/public/schedule")

    select_kind_of_study = Select(driver.find_element(By.ID, "study" ))   
    select_kind_of_study.select_by_value(kind_of_study)

    select_year_of_study = Select(driver.find_element(By.ID, "year" ))   
    select_year_of_study.select_by_value(year_of_study)
    
    button = driver.find_element(By.NAME, "_action_schedule")
    button.click()

    sleep(1)
    td = driver.find_element(By.NAME, "studentGroup")
    text = '\n' + td.text
    if (text != '\n'):
        text = text.replace('\n', '\n\t* ')
        f = open('slides/groupN.rst','r')
        lines = f.readlines()
        #print(text)
        
        stay_lines = [x for x in lines if '*' not in x]        

        f = codecs.open('slides/groupN.rst','w', 'utf-8')
        f.writelines(stay_lines)
        f.write(text)
        f.close()
        return True
    else: return False

def scrapAllGroups():

    print('--> SCRAP ALL GROUPS')

    options = Options()
    options.add_argument('headless')
    driver = selenium.webdriver.Chrome(options=options)
    driver.get("https://nastava.foi.hr/public/schedule")

    kinds_of_study = driver.find_element(By.ID, "study").find_elements_by_css_selector("*")
    years_of_study = ["1", "2", "3"]

    groups = set()
    
    for kind in kinds_of_study:
        for year in years_of_study:

            select_kind_of_study = Select(driver.find_element(By.ID, "study" ))
            select_kind_of_study.select_by_visible_text(kind.text)

            select_year_of_study = Select(driver.find_element(By.ID, "year" ))   
            select_year_of_study.select_by_value(str(year))

            #driver.implicitly_wait(5)

            try:
                element = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.NAME, "studentGroup")))
                g = driver.find_element(By.NAME, "studentGroup").text
                if g != '':
                    g_list = g.split('\n')
                    for elem in g_list:
                        groups.add(elem)
            except: pass       

    return groups
        
    


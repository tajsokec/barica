
import codecs

from time import sleep

import os

import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


from PIL import Image

def scrapSchedule(kind_of_study, year_of_study, group):

    print('--> SCRAP SCHEDULE')

    '''options = Options()
    options.add_argument('headless')'''
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    
    driver = webdriver.Chrome(options=chrome_options)

    #driver = selenium.webdriver.Chrome(options=options)
    driver.get("https://nastava.foi.hr/public/schedule")
    #driver.maximize_window()

    select_kind_of_study = Select(driver.find_element(By.ID, "study" ))   
    select_kind_of_study.select_by_value(kind_of_study)

    select_year_of_study = Select(driver.find_element(By.ID, "year" ))   
    select_year_of_study.select_by_value(year_of_study)

    button = driver.find_element(By.NAME, "_action_schedule")
    button.click()
    
    sleep(1)
    select_group = Select(driver.find_element(By.ID, "studentGroup" ))   
    select_group.select_by_visible_text(group)
    
    button = driver.find_element(By.NAME, "_action_schedule")
    button.click()

    sleep(1)
    driver.find_element_by_id("calendar").screenshot(
        os.path.join('slides\images', 'screenshot.png'))

    im = Image.open("slides\\images\\screenshot.png") # uses PIL library to open image in memory

    left, top, right, bottom = 0, 0, 1860, 900


    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save("slides\\images\\screenshot.png") # saves new cropped image




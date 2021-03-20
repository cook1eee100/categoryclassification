import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os


presidentNumber = range(582410, 596504)

for number in presidentNumber:


    options  = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome('./chromedriver', options=options)
    url = ('https://www1.president.go.kr/petitions/%d' %(number))
    driver.get(url)
    Checkpresident = driver.find_element_by_css_selector('#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div')

    if '비공개된 청원' in Checkpresident.text:
        driver.close()
        continue



    else:
            PresidentTitle = driver.find_element_by_css_selector(
                '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > h3')
            Presidentnumber = driver.find_element_by_css_selector(
                '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > h2')
            PresidentStartDy = driver.find_element_by_css_selector(
                '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > div.petitionsView_info > ul > li:nth-child(2)')
            PresidentStory = driver.find_element_by_css_selector(
                '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > div.petitionsView_write > div.View_write')
            f = open('%d.json' % (number), mode='wt', encoding='utf-8')
            f.write(PresidentTitle.text + '\n')
            f.write(Presidentnumber.text + '\n')
            f.write(PresidentStartDy.text + '\n')
            f.write(PresidentStory.text + '\n')
            print("=====" * 20)
            print("Success")
            print(number)
            print("국민청원 데이터")

    
    driver.close()

# from selenium import webdriver
import time
import os
from bs4 import BeautifulSoup
import requests
import re

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome("./chromedriver", options=options)

# driver.get("https://www1.president.go.kr/petitions/597091")

# a = driver.find_element_by_css_selector
# print(a.text)


# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# url = requests.get("https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012276315", headers = headers)
# soup = BeautifulSoup(url.content, "html.parser")

# s = soup.select('body')
# print(s[0].get_text())






# presidentNumber = range(400000, 400002)

# for number in presidentNumber:


    
#     response = requests.get('https://www1.president.go.kr/petitions/%d' %(number))
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     Checkpresident = soup.select('#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div')
    

#     if '비공개된 청원' in Checkpresident[0].get_text():
#         print("비공개된 청원", number)
#         continue


# text='참여인원 : [ 2,447명 ]'

# text = re.findall('\d+', text)
# text = int(''.join(text))

# print(text+3)

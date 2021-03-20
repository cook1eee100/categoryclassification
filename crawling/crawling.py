from bs4 import BeautifulSoup
import requests
import time
import os
from utils import *
import json

presidentNumber = range(582925, 596504)

if not os.path.isdir('./data'):
    os.mkdir('./data')

for number in presidentNumber:
    url = requests.get('https://www1.president.go.kr/petitions/%d' %(number))
    soup = BeautifulSoup(url.content, "html.parser")
    Checkpresident = soup.select('#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div')

    if '비공개된 청원' in Checkpresident[0].get_text():
        print("비공개된 청원", number)
        continue

    else:
        PetitionDict = {}
        PetitionsTitle = soup.select(               
            '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > h3')
        PetitionsNumAgree = soup.select(
            '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > h2')
        PetitionsCategory = soup.select(
            '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > div.petitionsView_info > ul > li:nth-child(1)')
        PetitionsBegin = soup.select(
            '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > div.petitionsView_info > ul > li:nth-child(2)')
        PetitionsContent = soup.select(
            '#cont_view > div.cs_area > div.new_contents > div > div.petitionsView_left > div > div.petitionsView_write > div.View_write')

        
        CategoryValue = PetitionsCategory[0].get_text()[4:]
        BeginValue = PetitionsBegin[0].get_text()[4:]
        ContentValue = normalize_text(PetitionsContent[0].get_text().strip())
        NumAgreeValue = normalize_number(PetitionsNumAgree[0].get_text())
        PetitionIdxValue = str(number)
        TitleValue = PetitionsTitle[0].get_text()


        # dictionary 저장 { category, begin, content, num_agree, petition_idx, title}
        PetitionDict['category']=CategoryValue                                  # 청원 카테고리
        PetitionDict['begin']=BeginValue                                        # 청원 날짜
        PetitionDict['content']=ContentValue                                    # 청원 내용
        PetitionDict['num_agree']=NumAgreeValue                                 # 참여 인원
        PetitionDict['petition_idx']=PetitionIdxValue                           # 청원 번호
        PetitionDict['title']=TitleValue                                        # 청원 제목



        with open('data/%d.json' % (number), mode='wt', encoding='utf-8') as f:
            json.dump(PetitionDict, f, ensure_ascii=False, indent=2)




        print("=====" * 20)
        print(number, "국민 청원 Success")


        time.sleep(0.7)

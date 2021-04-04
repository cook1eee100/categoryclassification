import os
import json

petitionsPath='preprocessing/petitions'         # 기존 데이터 파일 위치
dataPath='preprocessing/data'                   # 크롤링 데이터 파일 위치

if not os.path.isdir(petitionsPath):
    os.makedirs(petitionsPath)

if not os.path.isdir(dataPath):
    exit()

for fileName in os.listdir(dataPath):
    jsondata=""
    with open(f"{dataPath}/{fileName}", encoding='utf-8') as jp:
        jsondata=str(json.load(jp))
    
    with open(f"{petitionsPath}/petitions_26", 'a', encoding='utf-8') as fp:
        fp.write(jsondata+"\n")

    
    
import os
from ast import literal_eval
import utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats             # 표준 연속/이산 확률 분포(집적도 함수, 샘플러, 연속 분포 함수)와 다양한 통계 테스트, 그리고 좀 더 기술적인 통계 도구

petitionsPath = "preprocessing/petitions"
delTxt = '[본 게시물의 일부 내용이 국민 청원 요건에 위배되어 관리자에 의해 수정되었습니다]'

if not os.path.isdir(petitionsPath):
    exit()

txtList = []
for fileName in os.listdir(petitionsPath):
    with open(f'{petitionsPath}/{fileName}', 'r', encoding='utf-8') as fp:
        for line in fp.readlines():
            lineDict = literal_eval(line)
            txt = lineDict['petition_idx']+'  '+lineDict['category']+'  '+utils.normalize_text(lineDict['title'])+'  '+lineDict['content']
            if delTxt in txt:
                txt =txt.replace(delTxt, "")
            txtList.append(txt)
    
lenList=[]
for txt in txtList:
    lenList.append(len(txt))

lenArray = np.asarray(lenList)
df = pd.DataFrame(lenArray)

# 이상치
zscore_threshold = 1.8          # zscore outliers 임계값
outliers=df[(np.abs(stats.zscore(df)) > zscore_threshold).all(axis=1)].values.ravel()

# 최소값, 1사분위값, 2사분위값, 3사분위값, 최대값, 사용할 데이터 시작, 사용할 데이터 끝
rangeList=[0,25,50,75,100,25,75]
qValue=np.percentile(df[(np.abs(stats.zscore(df)) < zscore_threshold).all(axis=1)].values.ravel(), rangeList, interpolation='nearest')    
ratio=rangeList[6]-rangeList[5]

plt.boxplot([lenArray], showmeans=True)
plt.show()

tList=[]
for line in txtList:
    if qValue[1]<=len(line)<=qValue[3]:
        tList.append(line)

print(f"전체 데이터 개수(게시글 수) : {len(txtList)}, 이상치 개수 : {len(outliers)}, 사용 할 데이터 비율 : {ratio}%, 사용 할 데이터 개수 : {len(tList)}")

with open(f'preprocessing/data.txt', 'w', encoding='utf-8') as fp:
    for idx in tList:
        fp.write(idx+"\n")


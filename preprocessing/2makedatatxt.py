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

# rangeList 최소값, 1사분위값, 2사분위값, 3사분위값, 최대값, 사용할 데이터 시작, 사용할 데이터 끝
rangeList=[0,25,50,75,100, 5, 95]
qValue=np.percentile(df.values.ravel(), rangeList, interpolation='nearest')

ratio=rangeList[6]-rangeList[5]

plt.boxplot(df.values.ravel(), showmeans=True)
plt.text(1.05, qValue[0], qValue[0])
plt.text(1.09, qValue[1], qValue[1])
plt.text(1.09, qValue[2], qValue[2])
plt.text(1.09, qValue[3], qValue[3])
plt.text(1.05, qValue[4], qValue[4])
plt.text(1.15, qValue[5], qValue[5])
plt.text(1.15, qValue[6], qValue[6])
plt.show() 

tList=[]
for line in txtList:
    if qValue[5]<=len(line)<=qValue[6]:
        tList.append(line)

print(f"전체 데이터 개수(게시글 수) : {len(txtList)}, 사용 할 데이터 비율 : {ratio}%, 사용 할 데이터 개수 : {len(tList)}")

with open(f'preprocessing/data.txt', 'w', encoding='utf-8') as fp:
    for idx in tList:
        fp.write(idx+"\n")


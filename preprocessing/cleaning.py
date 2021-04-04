import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

lenList = []

with open("preprocessing/dataMerge.txt", 'r', encoding='utf-8') as fp:
    txtlist = fp.readlines()
    for line in txtlist:
        lenList.append(len(line)-1)             # -1 이유: 개행문자 카운트 제거     별 상관 없을듯





lenArray = np.asarray(lenList)
df = pd.DataFrame(lenArray)

# # 이상치
# a=df[(np.abs(stats.zscore(df)) > zscore_threshold).all(axis=1)].values.ravel()
# print(a)

# 최소값 1사분위값 2사분위값 3사분위값 최대값
qValue=np.percentile(df.values.ravel(), [0,25,50,75,100], interpolation='nearest')    

iqr = qValue[3]-qValue[1]
iqr_wieght = iqr*1.5
minValue = qValue[1]-iqr_wieght
maxValue = qValue[3]+iqr_wieght

outlier_index = df[(df<minValue) | (df>maxValue)]
outlier_index=outlier_index.dropna(axis=0)
print(outlier_index.values.ravel())

plt.boxplot(df.values.ravel(), showmeans=True)
plt.text(1.05, qValue[0], qValue[0])
plt.text(1.09, minValue, minValue)
plt.text(1.09, qValue[1], qValue[1])
plt.text(1.09, qValue[2], qValue[2])
plt.text(1.09, qValue[3], qValue[3])
plt.text(1.09, maxValue, maxValue)
plt.text(1.05, qValue[4], qValue[4])
plt.show()




tlist=[]
for line in txtlist:
    if minValue<=len(line)<maxValue:
        tlist.append(line)

print(qValue)
print("전체 데이터 수 : ", len(lenList))
print("min값 : ", minValue)
print("max값 : ", maxValue)
print("이상치 : ", len(outlier_index.values.ravel()))

print("데이터 개수 : ", len(tlist))



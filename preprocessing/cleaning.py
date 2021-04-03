import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

lenList = []

with open("preprocessing/data.txt", 'r', encoding='utf-8') as fp:
    txtlist = fp.readlines()
    for line in txtlist:
        lenList.append(len(line)-1)             # -1 이유: 개행문자 카운트 제거     별 상관 없을듯

lenArray = np.asarray(lenList)
df = pd.DataFrame(lenArray)
zscore_threshold = 1.8          # zscore outliers 임계값

# 이상치 개수
a=df[(np.abs(stats.zscore(df)) > zscore_threshold).all(axis=1)].values.ravel()
print(len(a))

# 최소값 1사분위값 2사분위값 3사분위값 최대값
qValue=np.percentile(df[(np.abs(stats.zscore(df)) < zscore_threshold).all(axis=1)].values.ravel(), [0,15,50,85,100], interpolation='nearest')    
print(qValue)


plt.boxplot([lenArray], showmeans=True, vert=False)
plt.show()


tlist=[]
for line in txtlist:
    if qValue[1]<=len(line)<=qValue[3]:
        tlist.append(line)

print(len(tlist))



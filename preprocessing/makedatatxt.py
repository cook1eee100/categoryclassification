import os
from ast import literal_eval
import utils

petitionsPath = "preprocessing/petitions"
delTxt = '[본 게시물의 일부 내용이 국민 청원 요건에 위배되어 관리자에 의해 수정되었습니다]'
txtList = []

if not os.path.isdir(petitionsPath):
    exit()

for fileName in os.listdir(petitionsPath):
    with open(f'{petitionsPath}/{fileName}', 'r', encoding='utf-8') as fp:
        for line in fp.readlines():
            lineDict = literal_eval(line)
            txt = lineDict['category']+'  '+utils.normalize_text(lineDict['title'])+'  '+lineDict['content']
            if delTxt in txt:
                txt =txt.replace(delTxt, "")

            txtList.append(txt)
    

print(len(txtList))

# 체크s
# for idx, line in enumerate(txtList):
#     print(idx, line)
#     print('='*30)



with open(f'preprocessing/dataMerge.txt', 'w', encoding='utf-8') as fp:
    for idx in txtList:
        fp.write(idx+"\n")

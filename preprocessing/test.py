# #-*- coding:utf-8 -*-

# import os
# import json



# # if not os.path.isdir("preprocessing/datamerge"):
# #     os.makedirs("preprocessing/datamerge")

# # if not os.path.isdir("preprocessing/data"):
# #     exit()


# # j=1

# # for i in range(582410, 596504):
# #     if i%1000==0:
# #         j+=1
# #     if not os.path.isfile(f"preprocessing/data/{i}.json"):
# #         continue

# #     jsondata=""
# #     with open(f"preprocessing/data/{i}.json", encoding='utf-8') as jp:
# #         jsondata=str(json.load(jp))
    
# #     filenumber = str(j).zfill(2)
# #     with open(f"preprocessing/datamerge/mergefile-{filenumber}", 'a', encoding='utf-8') as fp:
# #         fp.write(jsondata+"\n")


# from ast import literal_eval
# import utils

# # x = '{"category": "보건복지", "begin": "2017-08-31", "end": "2017-09-07", "content": "저희아버지 폐암4기로 3년을투병생활하셨습니다 기존표준항암 이제 항암부작용이커서. 더이상은 힘들것같다는의사의말을 들었습니다. 표준항암보다 부작용이 없는 면역항암제 쓰시게 해드리고싶어요 오프라벨에서라도 마지막으로 슬수잇게해주세요 임상실험중이라는데 저희아버진 시간이없어요 승인날대가지 기다릴시간이 없어요 부탁드립니다[본 게시물의 일부 내용이 국민 청원 요건에 위배되어 관리자에 의해 수정되었습니다]", "num_agree": 1, "petition_idx": "1198", "status": "청원종료", "title": "오프라벨"}'
# x = '{"category" : "정치개혁", "title" : "●   우리 나라가 생기고 요즘 보다 좋은 때는 없엇다   ●", "content" : "길거리 나가봐라 수입차가 늘비 하고 차가 막혀 앞으로 나갈수가 없이 잘사는데 박정희때 생각 해봐라 길거리 차하나 서 잇으면 뭐 신기 해서 동내 꼬마들 구경 하고 50가구에 자동차는 커능 자전거도 하나 하나 없엇다 박 정희때 수원 삼성 울산 현대 다녀도 월급이 얼마 인지 아느냐 1979년도 수원 삼성 근로자 월급이 85000원 수원 매탄동 방하나 부엌 하나 월세가 3만원 1979년도 공장 다녀서 아들 대학교 맛도 못봤다 요즘 99%가 대학교 출신이다 ~ 박 정때 막걸리 먹다가 대통령 욕하면 막 걸리 보안법에 남산 지하 남영동 지하 껄려 가면 병신 대는거 누구나 다 안다 박정희 새마을 사업 한다고 국민을 강제로 부역 시키고 부역 시킨 인건비 안주나 ~??"}'
# d = literal_eval(x)
# txt = d['category']+'  '+utils.normalize_text(d['title'])+'  '+d['content']
# # if '[본 게시물의 일부 내용이 국민 청원 요건에 위배되어 관리자에 의해 수정되었습니다]' in txt:

# print(txt.replace('[본 게시물의 일부 내용이 국민 청원 요건에 위배되어 관리자에 의해 수정되었습니다]', ""))






import re


text='e2 as3a sㅏ거냐더  ㅁ냐ㅓㄹ ㅁ냐어랸더랴넏ㄹ'
test = re.compile(r'[^가-힣ㅋ-ㅎa-zA-Z0-9\s]+')


text = test.sub('', text)

print(len(text.split()))

print(text)
import os
import json



if not os.path.isdir("preprocessing/datamerge"):
    os.makedirs("preprocessing/datamerge")

if not os.path.isdir("preprocessing/data"):
    exit()


j=1

for i in range(582410, 596504):
    if i%1000==0:
        j+=1
    if not os.path.isfile(f"preprocessing/data/{i}.json"):
        continue

    jsondata=""
    with open(f"preprocessing/data/{i}.json", encoding='utf-8') as jp:
        jsondata=str(json.load(jp))
    
    filenumber = str(j).zfill(2)
    with open(f"preprocessing/datamerge/mergefile-{filenumber}", 'a', encoding='utf-8') as fp:
        fp.write(jsondata+"\n")

    
    
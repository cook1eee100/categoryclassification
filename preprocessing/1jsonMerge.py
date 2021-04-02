import os
import json


if not os.path.isdir("preprocessing/petitions"):
    os.makedirs("preprocessing/petitions")

if not os.path.isdir("preprocessing/data"):
    exit()

for i in range(582410, 596504):
    if not os.path.isfile(f"preprocessing/data/{i}.json"):
        continue

    jsondata=""
    with open(f"preprocessing/data/{i}.json", encoding='utf-8') as jp:
        jsondata=str(json.load(jp))
    
    with open(f"preprocessing/petitions/petitions_26", 'a', encoding='utf-8') as fp:
        fp.write(jsondata+"\n")

    
    
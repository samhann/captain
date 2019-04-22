import json
import re


final =''

for i in range(1,149):
    with open('captain'+str(i)+'.txt') as json_file:
        data = json.load(json_file)
        for p in data['items']:
            title = '\n'+p['title'] +'\n'
            content = p['content']
            content = re.sub(r"<a>.*?</a>", "", content)
            content = re.sub(r"<.*?>", "", content)
            content = re.sub(r"&nbsp;", "", content)
            content = re.sub(r"\n+", "\n", content)
            print(title+content)



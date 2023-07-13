import json

with open("/home/sys16/Desktop/chatbot-emmanuel/test.json",'r') as f:
    d = json.load(f)
d = d['data']
for i in range(len(d)):
    t = d[i]
    tag = t['tag']
    responses = t["responses"]
    patterns = t["patterns"]
    print({"tag": tag, "responses": responses, "patterns": patterns})
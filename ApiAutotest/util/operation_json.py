import json

fb = open('../dataconfig/user.json')
data = json.load(fb)
print(data['user'])
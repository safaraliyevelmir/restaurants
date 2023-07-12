import requests as res
import json
# data = res.get('https://restaurants-yw3nygnvqq-uc.a.run.app?filter=true');
# text = data.text
# json_data = json.loads(text);
with open("data.json") as file:
    json_data = json.loads(file.read())

# for i in json_data:
#     data = {"fire_id": i["id"], "name":i["name"],"latitude":i["latitude"],"longitude":i["longtude"]}

#     post = res.post("http://206.189.199.212/restaurants/",data=data)
#     print(post.status_code)
#     print(post.content)


print(json_data[10])

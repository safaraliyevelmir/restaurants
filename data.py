import requests as res
import json
data = res.get('https://restaurants-yw3nygnvqq-uc.a.run.app?filter=true');
text = data.text
json_data = json.loads(text);


for i in json_data:
    data = {"fire_id": i["id"], "name":i["name"],"latitude":i["latitude"],"longitude":i["longtude"]}

    post = res.post("https://restaurants0staging.herokuapp.com/restaurants/",data=data)
    print(post.status_code)
    print(post.content)
import requests as res
import json
data = res.get('https://restaurants-yw3nygnvqq-uc.a.run.app?filter=true');
text = data.text
json_data = json.loads(text);
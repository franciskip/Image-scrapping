import requests
import json
from requests.structures import CaseInsensitiveDict

def pexels():
    key_words = ['indian man', 'player']
    i = 0
    page = 1
    while True:
        count = 1
        for reqs in range(200):
            url = f"https://api.pexels.com/v1/search?query={key_words[i]}&per_page=80&page={page}"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer [YOUR_API_KEY]"
            resp = requests.get(url, headers=headers)
            our_json = json.loads(resp.text)
            with open(f'{key_words[i]}.txt', 'a') as pt:
                pt.write("%s\n" % our_json)
            page+=1
            count += 1
            if count == 101:
                page = 1
                i +=1
pexels()
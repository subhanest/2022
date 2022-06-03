import requests
import json

def callup(word): 
    app_id  = '7aca66ec'
    app_key = 'b8874d0b4db834ec6076fa0df898a7e9'

    language = 'en-gb'
    word_id = word
    fields = 'pronunciations'
    strictMatch = 'false'

    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
    r = requests.get(url, headers = {'app_id':app_id,'app_key':app_key})
 
    return r.status_code
    #print("code {}\n".format(r.status_code))
    #print("text \n" + r.text)
    #print("json \n" + json.dumps(r.json()))
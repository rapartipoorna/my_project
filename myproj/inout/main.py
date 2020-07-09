import requests
import json


def send_sms(number,message):
    url="https://www.fast2sms.com/dev/bulk"
    params={
    'authorization':'QbVySiFz79oE2a61OwnuhUrtZ4lpNvxA0jeBfY38dsqIDLcJkmVXnpksf9JAvFPG65MiQgZylao7dU1h',
    'sender_id':'FSTSMS',
    'message':message,
    'language':'english',
    'route':'p',
    'numbers':number
    }

    response=requests.get(url, params=params)
    dict=response.json()
    print(dict)

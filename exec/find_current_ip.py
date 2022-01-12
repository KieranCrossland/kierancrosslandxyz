#!/bin/python3
import os
import requests

def ipcurl():
    url = "https://api.ipify.org/"
    payload = dict(key1='value1', key2='value2')
    res = requests.get(url, data=payload)
    print(res.text)
ipcurl()

# mPyPlx - Extensions to Monadic Pipeline Library for Python
# http://github.com/shwars/mPyPlx

# Different services related to Bing search

import requests
from mPyPl.mdict import *

class CognitiveService():

    def __init__(self,key,url):
        self.key = key
        self.url = url

    def __url(self,method=""):
        u = self.url if self.url[-1]=='/' else self.url+'/'
        return u+method

    def request_get(self,params,headers=dict(),method=""):
        headers["Ocp-Apim-Subscription-Key"]=self.key
        resp = requests.get(self.__url(method),headers=headers,params=params)
        resp.raise_for_status()
        return resp.json()

    def request_post(self,params,data,headers=dict(),method=""):
        headers["Ocp-Apim-Subscription-Key"]=self.key
        resp = requests.post(self.__url(method),headers=headers,params=params,data=data)
        resp.raise_for_status()
        return resp.json()

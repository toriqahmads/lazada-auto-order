import requests
import json
import re

def loginPage() :
    url = "https://member.lazada.co.id/user/login"
    s = requests.session()
    
    headers = {'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://member.lazada.co.id',
                'referer': 'https://member.lazada.co.id/user/login',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
               }

    req = s.get(url, headers=headers)
    pat = re.compile(r"id=\"X-CSRF-TOKEN\" content=\"(.*?)\"")
    res = re.findall(pat, req.text)
    
    return {'token':res[0], 'cookie': req.cookies}
    
def login(token) :
    url = "https://member.lazada.co.id/user/api/login"
    s = requests.session()
    
    headers = {'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://member.lazada.co.id',
                'referer': 'https://member.lazada.co.id/user/login',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-csrf-token': token['token']
               }

    datas = {'loginName':'toriqahmads@gmail.com','password':'Kbps1234'}

    req = s.post(url, data=json.dumps(datas), headers=headers, cookies=token['cookie'])
    reqs= req.json()
    print(req.cookies)
    if reqs['success'] == True :
        return {'cookie': req.cookies, 'content': reqs}

def visitProd(token) :
    url = "https://www.lazada.co.id/-i174951351-s207287470.html?spm=a2o4j.order_details.details_title..3b896664srxzbW&urlFlag=true&mp=1"
    s = requests.session()
    
    headers = {'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://member.lazada.co.id',
                'referer': 'https://member.lazada.co.id/user/login',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
               }

    req = s.get(url, headers=headers, cookies=token['cookie'])
    pat = re.compile(r"id=\"X-CSRF-TOKEN\" content=\"(.*?)\"")
    res = re.findall(pat, req.text)
    
    return {'token':res[0], 'cookie': req.cookies}

def addCart(token) :
    url = "https://cart.lazada.co.id/cart/api/add"
    s = requests.session()
    
    headers = {'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://member.lazada.co.id',
                'referer': 'https://member.lazada.co.id/user/login',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-csrf-token': token['token']
               }
    print(headers)
    datas = [{'itemId':'174951351','skuId':'207287470','quantity':1}]
    req = s.post(url, data=json.dumps(datas), headers=headers, cookies=token['cookie'])
    res = req.json()

    if res['success'] == True :
        
    
r=loginPage()
r2 = login(r)
r3 = visitProd(r2)
addCart(r3)

from time import sleep

import requests
import json

url = "https://mall.bilibili.com/mall-magic-c/internet/c2c/v2/list"

i_want = []
nextId = None
while True:
    payload = json.dumps({
        "categoryFilter": "2312",
        "priceFilters": [
            "5000-9000"
        ],
        "discountFilters": [
            "10-100"
        ],
        "nextId": nextId
    })

    headers = {
        'authority': 'mall.bilibili.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'cookie': "修改我！！！！！",
        'origin': 'https://mall.bilibili.com',
        'referer': 'https://mall.bilibili.com/neul-next/index.html?page=magic-market_index',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        response = response.json()
        nextId = response["data"]["nextId"]
        if nextId is None:
            break
        data = response["data"]["data"]
        for item in data:
            name = item["c2cItemsName"]
            if "锦木千束" in name:
                if item not in i_want:
                    i_want.append(item)


    except Exception as e:
        sleep(3)

print(i_want)

min_element = min(i_want, key=lambda x: x["price"])
for item in i_want:
    print(f"{item['c2cItemsName']},{item['c2cItemsId']},{item['price']}")
print(min_element)

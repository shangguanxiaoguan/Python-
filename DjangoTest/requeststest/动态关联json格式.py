import json

import requests


# def relate_json():
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-07-17&leftTicketDTO.from_station=FZS&leftTicketDTO.to_station=HGH&purpose_codes=ADULT'

cookies = {
    'Cookie': '_uab_collina=159497654972640974504758; JSESSIONID=14D6649A4EDEBD5801F047666AA926E1; _jc_save_wfdc_flag=dc; _jc_save_toStation=%u676D%u5DDE%u4E1C%2CHGH; _jc_save_fromStation=%u798F%u5DDE%2CFZS; BIGipServerotn=602931722.50210.0000; BIGipServerpool_passport=401408522.50215.0000; RAIL_EXPIRATION=1595314609476; RAIL_DEVICEID=K8WjReNlWNrUoqTbY1RX90loW1wyNTuZxXwzpEtKRYIT7vHQDgkDY9UiL0GfddcgIHqkyfZKCjS0E3Sjn_pVUiaf30vBPohT5Cdxnxf_FaVx8p2y8f73gsevQSX_RMGG7yBpTMB23kfQJ9biKP1cRYFIr83Zpe2a; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromDate=2020-07-17; _jc_save_toDate=2020-07-17'
}
res = requests.get(url=url, cookies=cookies)
# print(json.loads(res.text))
print(res.json())

# 提取返回结果的值
print(res.json()['httpstatus'])
print(res.json()['data'])
print(res.json()['data']['map'])
print(res.json()['data']['map']['HGH'])


from urllib import parse
# # import AES
# from Crypto.Cipher import AES

# ori_url_10='http://192.168.0.10:3080/asg/portal.do?call=230&j' \
#            'son={"pri":{"search_key":"","f":"f1,f2,f3,f4,f5,f7,f9,f10,f11","sadu":"0","apkversion":"1",' \
#            '"imeibak":"868805034766728,868805034854508,A000008C057C25","isInsHwSevice":true,' \
#            '"utd_id":"Wt1InLx\/qxUDAETE+FTqwQkW","czip":"0","supportLoginWay":["QQ","WECHAT","SINA",' \
#            '"PHONE_NUM_VERIFY","HUAWEI",null,"GEYAN"],"isLogin":"2","appSign":"09a448c68f8502610a48287073621e9c",' \
#            '"clip_info":"","sourceIp":"http:\/\/192.168.0.10:3080\/asg\/portal.do","bookHero":"","v":"1",' \
#            '"rCode":"3973004","vtv":"9","bidReqCount":3,"android_id":"441c3a1de1b2ad7d",' \
#            '"payDexTime":"2019-04-23 20:20:34","installHours":0},"pub":{"clientAgent":"svnVer_1909051616",' \
#            '"city":"%E4%BA%B3%E5%B7%9E%E5%B8%82","sign":"ba8e936e5991211c5664bce09d063c1f","screen":"720x1206",' \
#            '"appCode":"f002","imsi":"dz_1567589819625","deviceId":"dz4fb51a4614604ad185d390bb40101f00","lsw":"2",' \
#            '"apiVersion":"3.9.7.3004","province":"%E5%AE%89%E5%BE%BD%E7%9C%81","model":"ALP-AL00","brand":"HUAWEI",' \
#            '"apn":"wifi","channelCode":"Google","dzPaySupport":"2","os":"android28","pname":"com.ishugui",' \
#            '"utdid":"Wt1InLx\/qxUDAETE+FTqwQkW","en":"{\"adsdk\":\"1\",\"geyan\":\"1\"}","channelFee":"Google05",' \
#            '"userId":"","p":"59","subPline":"2","afu":"0","cmTel":"","v":"4","imei":"868805034766728",' \
#            '"macAddr":"E4:A7:C5:08:8C:5B"}}'

ori_url_10='http://54.241.21.249:8089/skyvpn/v2/invite/getUrl?userId=7393118869599801&' \
           'deviceId=And.0dc777f006a811ea93480c9d921af4a1.skyvpn&types=3&token=ad4c8cfb9a4e0da08996aa9c962db7aa' \
           '&sign=406d14d74054580f940fc015d8dfd60e&timestamp=1597133126368'
print('----------------------ori_url\n', ori_url_10)

# decode解码
urldecode = parse.unquote(ori_url_10)
print('----------------------urldecode\n', urldecode)

# encode编码
urlencode=parse.quote(urldecode)
print('----------------------urlencode\n', urlencode)

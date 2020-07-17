import requests

url = 'https://sinfo.ctrip.com/MyInfo/Ajax/UploadPhoto.ashx'

# uploadFile_928：文件参数的名字

files = {
    'uploadFile_928': ('1.png', open('F:\\1.png', 'rb'), 'image/png')
}
#  Sys_Login_Time_Out  ===>需要cookie信息
cookies = {

}

res = requests.post(url=url, files=files, verify=False)
print(res.text)



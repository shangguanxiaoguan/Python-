import requests

url = 'https://sinfo.ctrip.com/MyInfo/Ajax/UploadPhoto.ashx'

# uploadFile_928���ļ�����������

files = {
    'uploadFile_928': ('1.png', open('F:\\1.png', 'rb'), 'image/png')
}
#  Sys_Login_Time_Out  ===>��Ҫcookie��Ϣ
cookies = {

}

res = requests.post(url=url, files=files, verify=False)
print(res.text)



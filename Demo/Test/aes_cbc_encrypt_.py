import base64
import hashlib

from Crypto.Cipher import AES

from api.DtUtils import log


class AesCBC:

    def __init__(self):
        # self.MODE = AES.MODE_CBC
        # self.BS = AES.block_size
        # self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        # self.unpad = lambda s: s[0:-ord(s[-1])]

    def md5_value(self, value):
        '''
        进行16位的md5加密
        :param value:
        :return:
        '''
        m = hashlib.md5(value.encode())
        m_result = m.hexdigest()[0:16]
        log.info('16 digits md5 value：' + m_result)
        return m_result

    def add_to_16(self, value):
        '''
        value不是16的倍数那就补足为16的倍数
        :param value:
        :return:
        '''
        while len(value) % 16 != 0:
            value += '\0'
        log.info('str.encode(value)：' + str(str.encode(value)))
        # 返回bytes
        return str.encode(value)

    def aes_encrypt(self, text, key, iv):
        '''
        AES128 加密
        :param text:
        :param key:
        :param iv:
        :return: encrypted_text
        '''
        mode = AES.MODE_CBC
        BS = AES.block_size
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        unpad = lambda s: s[0:-ord(s[-1])]
        aes = AES.new(self.add_to_16(key), mode, self.add_to_16(iv))  # 初始化加密器
        log.info('aes：' + str(aes))
        # 执行加密并转码返回bytes
        encrypted_text = str(base64.encodebytes(aes.encrypt(self.add_to_16(pad(text)))), encoding='utf-8').replace('\n', '')
        log.info('base64 output：' + encrypted_text)
        return encrypted_text


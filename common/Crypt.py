"""
加解密模块（暂时不用）
"""
import base64

from Crypto.Cipher import AES


class CryptWithPhp(object):
    key = b'QWHeJfoWQgaYasdf'
    iv = b'QWHeJfoWQgaYasdf'

    def __init__(self):
        pass

    # 目前暂时无法和php交互，两边结果不一致
    def aes_encode(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.key)  # 设置AES加密模式 此处设置为CBC模式
        block_size = AES.block_size
        # 判断data是不是16的倍数，如果不是用'?'补足
        if len(data) % block_size != 0:
            add = block_size - (len(data) % block_size)
        else:
            add = 0
        data += '?' * add
        data = bytes(data, encoding='utf-8')
        encrypted = cipher.encrypt(data)  # aes加密
        # result = binascii.b2a_hex(encrypted)  # b2a_hex encode  将二进制转换成16进制 ——》 不进行转换了，直接发送base64编码后的二进制
        return base64.urlsafe_b64encode(encrypted)

    def aes_decode(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.key)
        data = base64.b64decode(data)
        # result2 = binascii.a2b_hex(data)  # 十六进制还原成二进制 # php传过来就是二进制的，不需要再次转化
        decrypted = cipher.decrypt(data)
        result = decrypted.decode(encoding='utf-8', errors='ignore')
        return result[0:16].replace('?', '')  # 长度达到16位时python会自动再增加16位，所以截取前16位，并将问号替换掉，问号是和php那边约定好的


# if __name__ == '__main__':
    # crypt = CryptWithPhp()
    # res = crypt.aes_encode("92558851")
    # print(res)

    # en = 'BKyicblTuZL0S97OM2JRPajq0OuQeSkulY1irfQfq0c='
    # res = crypt.aes_decode(en)
    # print(res)

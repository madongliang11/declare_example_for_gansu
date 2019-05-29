"""
百度ocr模块
"""
import time

import requests
from aip import AipOcr
from common.Container import Container
from common.Config import Config


class Ocr(object):
    def __init__(self):
        self.__CONFIG = Config()
        _, self.APP_ID = self.__CONFIG.get_config('baiduocr', 'app_id')
        _, self.API_KEY = self.__CONFIG.get_config('baiduocr', 'api_key')
        _, self.SECRET_KEY = self.__CONFIG.get_config('baiduocr', 'secret_key')

    @staticmethod
    def save_img_file(img_src, img_save_path):
        with open(img_save_path, 'wb') as f:
            f.write(requests.get(img_src).content)

    @staticmethod
    def get_img_file(img_save_path):
        with open(img_save_path, 'rb') as f:
            return f.read()

    def get_code_with_file(self, img_src, place):
        img_save_path = Container.PATH + 'static\\' + place + '_' + str(int(time.time())) + '_code.png'
        self.save_img_file(img_src, img_save_path)
        client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        img_file = self.get_img_file(img_save_path)
        res = client.basicAccurate(img_file)
        return res['words_result'][0]['words']

    def get_code_with_screen_shot(self, img_save_path):
        client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        img_file = self.get_img_file(img_save_path)
        res = client.basicAccurate(img_file)
        try:
            return res['words_result'][0]['words']
        except:
            return ''

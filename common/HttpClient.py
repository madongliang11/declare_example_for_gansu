"""
http客户端
"""
import base64
import hashlib
import json
import os
import random
import threading
import time
import requests

from common.Container import Container


class HttpClient(object):
    token = 'LxVto2aO2UsU9WxZ55EEKiPxSy9W0CAahAIpuH6ezKg='
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        """
        单例
        :param args:
        :param kwargs:
        :return:
        """
        if not hasattr(HttpClient, '_instance'):
            with HttpClient._instance_lock:
                if not hasattr(HttpClient, "_instance"):
                    HttpClient._instance = object.__new__(cls)
        return HttpClient._instance

    def encode_token(self):
        """
        加密
        :return:
        """
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        value = str(chr(random.randint(97, 122))) + date + str(random.randint(1000, 9999))
        value = self.get_md5(HttpClient.token) + base64.b64encode(value.encode('utf-8')).decode('utf-8')
        value = base64.b64encode(value.encode('utf-8')).decode('utf-8')
        return value

    @staticmethod
    def get_md5(md5str):
        m1 = hashlib.md5()
        m1.update(md5str.encode("utf-8"))
        return m1.hexdigest()

    @staticmethod
    def get_filename(path):
        return os.path.basename(path)

    @staticmethod
    def to_request_for_code(method, url, data=None, params=None):
        """
        验证码请求，静态化（实验）
        :param method:
        :param url:
        :param data:
        :param params:
        :return:
        """
        return HttpClient.to_request(method=method, url=url, data=data, params=params)

    def to_request_for_declare(self, method, url, data=None, params=None):
        """
        申报和反馈请求
        :param method:
        :param url:
        :param data:
        :param params:
        :return:
        """
        files = None
        if data is not None:
            if data['data']['result_img'] is not []:
                files = {}
                for file in data['data']['result_img']:
                    files.update(
                        {self.get_filename(file): (self.get_filename(file), open(file, 'rb'), 'image/png')})
            # data['data'].pop('result_img')
            data['data'] = json.dumps(data['data'])
        else:
            data = {}
        data.update({'token': self.encode_token()})
        data.update({'tax_area_code': Container.TAX_AREA_CODE})
        return self.to_request(method=method, url=url, data=data, params=params, files=files)

    @staticmethod
    def to_request(**kwargs):
        try:
            response = requests.request(method=kwargs.get('method', None), url=kwargs.get('url', None),
                                        data=kwargs.get('data', None),
                                        params=kwargs.get('params', None), files=kwargs.get('files', None), timeout=15)
            return (True, response.json()) if response.status_code == 200 else (False, repr(response))
        except Exception as e:
            print(repr(e))
            return False, repr(e)

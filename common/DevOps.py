import threading
import time

from common.HttpClient import HttpClient
from common.Container import Container


class DevOps(object):
    heartbeat_type = 1
    heartbeat_url = Container.HEARTBEAT_URL

    def __init__(self):
        pass

    @staticmethod
    def heartbeat_action(heartbeat_type):
        while True:
            request_param = dict()
            request_param.update({'heartbeat_type': heartbeat_type})
            HttpClient.to_request_for_code(url=DevOps.heartbeat_url, method='POST', params=request_param)
            print(threading.current_thread().name)
            time.sleep(60)

    @staticmethod
    def heartbeat():
        """
        开启心跳，60s发送一次
        :return:
        """
        by = threading.Thread(target=DevOps.heartbeat_action, args=(DevOps.heartbeat_type,), name='heartbeat')
        by.start()

"""
日志
"""
import logging
import threading
import time
import os

from common.Container import Container


class Logger(object):
    _instance_lock = threading.Lock()
    _logger = None
    _file_handle = None

    def __new__(cls, *args, **kwargs):
        """
        单例模式
        注意：每次重新设置file_handle，使其能正确的按照日期生成日志文件
        :param args:
        :param kwargs:
        :return:
        """
        cls.set_file_handle(cls)
        if not hasattr(Logger, '_instance'):
            with Logger._instance_lock:
                if not hasattr(Logger, "_instance"):
                    Logger._instance = object.__new__(cls)
                    cls.set_logger(cls)
        return Logger._instance

    def set_logger(self):
        self._logger = logging.getLogger('PyClientTaxReturn')
        self._logger.propagate = False
        self._logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s')
        # file_handle = logging.FileHandler(filename=self.get_filename(), encoding='utf-8')
        file_handle = self._file_handle
        console_handle = logging.StreamHandler()
        file_handle.setFormatter(formatter)
        console_handle.setFormatter(formatter)
        self._logger.addHandler(file_handle)
        self._logger.addHandler(console_handle)

    def set_file_handle(self):
        self._file_handle = logging.FileHandler(filename=self.get_filename(), encoding='utf-8')

    def to_log(self, level, message):
        if level == 'error':
            self._logger.error(message)
        elif level == 'warning':
            self._logger.warning(message)
        elif level == 'info':
            self._logger.info(message)

    @staticmethod
    def get_filename():
        filename = time.strftime('%Y%m%d', time.localtime(time.time()))
        path = Container.PATH + 'static\\logs\\'
        filename = path + filename + '.log'
        if os.path.exists(path) is False:
            os.makedirs(filename)
        return filename

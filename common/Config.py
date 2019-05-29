"""
读取配置
"""
import configparser

from common.Container import Container


class Config(object):

    def __init__(self):
        self.config = {}
        self.set_all_config()

    def set_all_config(self):
        conf = configparser.ConfigParser()
        conf.read(Container.PATH + 'config\\config.ini')
        for section in conf.sections():
            self.config[section] = {}
            for item in conf.items(section):
                self.config[section][item[0]] = item[1]

    def get_config(self, section, item):
        try:
            conf = self.config[section][item]
            return True, conf
        except KeyError:
            return False, '没有' + section + '或者' + item

"""
打码平台
"""
import hashlib
import time

from common.Container import Container
from common.HttpClient import HttpClient


class VerificationCode(object):
    """
    c_type 验证码类型
    c_addr 图片地址
    c_text 提醒信息
    client_id 客户端id
    sign 加密后的字符串
    """

    def __init__(self):
        # 请求参数组 和 唯一id
        self.request_param = None
        self.unique = None
        # 相关常量，稍后写进常量文件Constants中
        self.client_id = Container.CODE_PLATFORM_CLIENT_ID
        self.secret_key = Container.CODE_PLATFORM_SECRET_KEY
        self.get_request_url = Container.CODE_PLATFORM_REQUEST_URL
        self.get_captcha_result_url = Container.CODE_PLATFORM_GET_RESULT_URL
        self.put_captcha_web_result_url = Container.CODE_PLATFORM_FEEDBACK_URL

    def set_sign(self, param):
        """
        将内容去掉 sign 之后，按照 key 升序组合 key1=value1&key2=value2&key3=value3 的格式拼接,
        再将 your_secret 追加到后面
        :param param:
        :return: 加密字符串
        """
        if 'sign' in param:
            param.pop('sign')
        data_keys = list(param.keys())
        data_keys.sort(reverse=False)
        key_value_list = []
        for key in data_keys:
            key_value_list.append('%s=%s' % (key, param[key]))
        make_sign_str = '&'.join(key_value_list) + self.secret_key
        make_sign_str = hashlib.new('md5', make_sign_str.encode('utf-8')).hexdigest()
        make_sign_str = make_sign_str
        return make_sign_str

    def set_request_param_for_1(self, code_img_url):
        """
        构造数据，第一种类型验证码，填写文本
        :param code_img_url:
        :return:
        """
        # 构造数据
        request_param = dict()
        request_param['c_type'] = 2
        request_param['c_addr'] = code_img_url
        request_param['c_text'] = '请输入验证码结果'
        request_param['client_id'] = self.client_id
        request_param['sign'] = self.set_sign(request_param)
        self.request_param = request_param

    def set_request_param_for_2(self, code_img_url, tips_test):
        """
        构造数据：第二种类型验证码，点击图片上文字
        :param code_img_url: 验证码图片地址
        :param tips_test: 说明文字
        :return: 请求参数
        """
        # 构造数据
        request_param = dict()
        request_param['c_type'] = 2
        request_param['c_addr'] = code_img_url
        request_param['c_text'] = tips_test
        request_param['client_id'] = self.client_id
        request_param['sign'] = self.set_sign(request_param)
        self.request_param = request_param

    def set_request_param_for_3(self):
        pass

    def request(self, retry_times=0):
        """
        一、将获取一个唯一id，获取打码结果的请求要带上这个id
        :param retry_times: 重试次数
        :return:
        """
        if retry_times >= 3:
            return False, '打码平台暂时无响应'
        retry_times += 1
        result_bool, content = HttpClient.to_request_for_code(method='POST', url=self.get_request_url,
                                                              data=self.request_param)
        if result_bool is False:
            self.request(retry_times)
        if content['r_code'] != 200:
            return False, content['msg']
        result_data = dict()
        result_data['unique'] = content['r_id']
        self.unique = result_data['unique']
        return True, result_data

    def get_captcha_result(self, overtime):
        """
        二、轮询请求验证码打码结果，每秒1次
        :param overtime: 超时时间/秒
        :return: 打码结果
        """
        self.request_param['c_id'] = self.unique  # 唯一id
        self.request_param['sign'] = self.set_sign(self.request_param)
        print(self.request_param)
        request_count = 0  # 请求次数
        interval = 1  # 请求间隔
        max_request_count = int(overtime / interval)
        while True:
            time.sleep(interval)
            if request_count > max_request_count:
                return False, '打码超时'
            result_bool, content = HttpClient.to_request_for_code(method='POST', url=self.get_captcha_result_url,
                                                                  data=self.request_param)
            print(content)
            if result_bool is False or content['r_code'] != 200 or content['r_status'] == 1:
                request_count += 1
                continue
            return content['info']

    def feedback_result(self, exec_result=0, retry_times=0):
        """
        三、反馈验证的结果
        :param exec_result:1是验证正确，其他错误
        :param retry_times:重试次数
        :return:
        """
        self.request_param['res'] = exec_result
        self.request_param['c_id'] = self.unique
        self.request_param['sign'] = self.set_sign(self.request_param)
        request_param = self.request_param
        if retry_times >= 3:
            return False, '打码平台暂时无响应'
        retry_times += 1
        result_bool, content = HttpClient.to_request_for_code(method='POST', url=self.put_captcha_web_result_url,
                                                              data=request_param)
        if result_bool is False or content['r_code'] != 200:
            exec_result = self.request_param['res']
            self.feedback_result(exec_result, retry_times)
        if content['r_code'] != 200:
            return False, content.message
        result_data = dict()
        result_data['unique'] = content['c_id']
        return True, result_data


if __name__ == '__main__':
    code_type = 2
    code_img_url = 'https://necaptcha.nosdn.127.net/9e0264ae09bd46a5a2adef754f737bf8.jpg'
    tips_test = '请依次点击 "终" "围" "吃"'
    cc = VerificationCode()
    cc.set_request_param_for_2(code_img_url, tips_test)
    print(cc.request())  # 一、将获取一个唯一id，获取打码结果的请求要带上这个id
    print(cc.get_captcha_result(300))  # 二、轮询请求验证码打码结果，每秒1次
    print(cc.feedback_result(1))  # 三、反馈验证的结果

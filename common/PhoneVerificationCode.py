"""
手机验证码
"""
import json
import time

from common.Container import Container
from common.HttpClient import HttpClient
from common.Logger import Logger


class PhoneVerificationsCode(object):

    def __init__(self, company_account):
        self.logger = Logger()
        self.account = company_account
        self.openid = None
        self.prev_verification_code = ''

    def request_phone_code(self, retry_times):
        # 2.告诉后端手机验证码已经发送
        # 暂时去掉，不走第二步，20190409
        # openid = self.code_already_send(retry_times)
        # retry_times += 1
        # if openid is False:
        #     return False
        # self.openid = openid
        # 3.每隔5秒请求一次接口
        code = self.loop_request_code(retry_times)
        if code is False:
            return False
        return code

    def code_already_send(self, retry_times):
        """
        点击发送验证码之后，请求后端，告诉手机验证码发送发送按钮已点
        :param retry_times: 重试次数（在后端和业务代码中控制）
        :return: openid
        """
        url = Container.PHONE_SEND_CODE
        method = 'POST'
        request_param = {'account': self.account, 'retry_times': retry_times,
                         'task_type': Container.COMMON_DATA['task_type']}
        result_bool, response = HttpClient().to_request_for_code(method, url, data=request_param)
        print(response)
        Logger().to_log('info', 'code_already_send')
        if result_bool is True and response['code'] == 200:
            return response['openid']
        return False

    def loop_request_code(self, retry_times):
        """
        轮询请求客户回复的手机验证码
        :param retry_times:
        :return:
        """
        # 每隔5秒请求一次接口
        # 将本次验证码与上次的验证码做比较，如果一致d的话就表示重试请求后的验证码没有变化，还是错误的验证码（不然也不会重试）
        # 重试次数大于1的时候，将请求来的验证码保存下来，为下一次请求的验证码对比做准备
        url = Container.PHONE_GET_CODE
        method = 'POST'
        request_param = dict()
        # request_param['openid'] = self.openid
        request_param['account'] = self.account
        for i in range(int(Container.LOGIN_WAIT_SECOND / Container.LOGIN_REQUEST_INTERVAL)):
            result_bool, response = HttpClient().to_request_for_code(method, url, data=request_param)
            response = json.loads(response)
            if result_bool is True and response['code'] == 200:
                self.logger.to_log('info', '手机验证码：{}'.format(response['data']))
                if response['data'] == self.prev_verification_code:
                    self.logger.to_log('info', '两次请求验证码结果相同，验证码错误')
                    time.sleep(Container.LOGIN_REQUEST_INTERVAL)
                    continue
                if retry_times > 1:
                    self.prev_verification_code = response['data']
                return response['data']
            self.logger.to_log('info', '未请求到验证码数据')
            time.sleep(Container.LOGIN_REQUEST_INTERVAL)
        self.logger.to_log('info', '本次请求周期5分钟结束')
        return False


if __name__ == '__main__':
    account = '91610133MA6TXDH24P'
    login_retry_times = 1
    Container.PATH = Container.PATH + '\\..\\'
    pvc = PhoneVerificationsCode(account)
    Container.COMMON_DATA = dict()
    Container.COMMON_DATA['task_type'] = 1
    while True:
        # 业务代码，填写账号密码等等
        # 点击发送手机验证码的按钮
        if login_retry_times > (Container.LOGIN_MAX_RETRY_TIMES - 1):
            Logger().to_log('info', '重试次数超标')
            break
        verification_code = pvc.request_phone_code(login_retry_times)
        login_retry_times += 1
        if verification_code is False:
            continue
        else:
            break
        # 业务代码，填写获取到的手机验证码
        # 然后验证是否正确，如果是验证码错误的话就继续循环
        # continue

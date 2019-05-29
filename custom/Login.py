import json
import os
import time

from PIL import Image

from common.General import General
from common.Container import Container
from common.HttpClient import HttpClient
from common.Logger import Logger
from common.Ocr import Ocr
from custom.Helper import Helper
from custom.Step import Step


class Login(object):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.logger = Logger()
        self.general = General()
        self.driver = Container.DRIVER

    # cookies 模拟登陆，调试用
    def cookie_login(self):
        self.driver.maximize_window()
        self.driver.get("http://etaxs.sn-n-tax.gov.cn/xxmh/html/index_login.html")
        cookies = {"name": "DZSWJ_TGC", "value": "7213AA1A13395F02DFA5C012C6060B68", "domain": ".etaxs.sn-n-tax.gov.cn",
                   "path": "/", "expires": "1969-12-31T23:59:59.000Z", "size": 41}
        self.driver.add_cookie(cookies)
        cookies = {"name": "JSESSIONID", "value": "B685025F93DEA2C5B92D9885D7302252", "domain": "etaxs.sn-n-tax.gov.cn",
                   "path": "/xxmh/", "expires": "1969-12-31T23:59:59.000Z", "size": 42}
        self.driver.add_cookie(cookies)
        cookies = {"name": "SESSION_SSSQ_NAME", "value": "2018-11-01", "domain": "etaxs.sn-n-tax.gov.cn",
                   "path": "/", "expires": "2018-11-30T10:50:03.379Z", "size": 27}
        self.driver.add_cookie(cookies)
        cookies = {"name": "SESSION_SSSZ_NAME", "value": "2018-11-30", "domain": "etaxs.sn-n-tax.gov.cn",
                   "path": "/", "expires": "1969-12-31T23:59:59.000Z", "size": 27}
        self.driver.add_cookie(cookies)
        cookies = {"name": "SYS_CHANNEL_ID", "value": "A01", "domain": "etaxs.sn-n-tax.gov.cn",
                   "path": "/", "expires": "1969-12-31T23:59:59.000Z", "size": 17}
        self.driver.add_cookie(cookies)
        cookies = {"name": "TGC", "value": "TGT-104339-QztdWApRgtvLb9dd95yIHPOuyYdqJkDPcukp4lCcWeo4Wa6SOk-gddzswj",
                   "domain": ".etaxs.sn-n-tax.gov.cn",
                   "path": "/", "expires": "1969-12-31T23:59:59.000Z", "size": 70}
        self.driver.add_cookie(cookies)
        cookies = {"name": "clwz_blc_pst_pool_2x2e0xc1xaaxbaxcfxb0xe6xc9xfaxb2xfaxbbxb7xbexb3nginx",
                   "value": "862218250.20480", "domain": ".etaxs.sn-n-tax.gov.cn",
                   "path": "/", "expires": "1969-12-31T23:59:59.000Z", "size": 85}
        self.driver.add_cookie(cookies)
        cookies = {"name": "route", "value": "f8183df1d8945ec1a11915c093f46db9", "domain": ".etaxs.sn-n-tax.gov.cn",
                   "path": "/", "expires": "1969-12-31T23:59:59.000Z", "size": 37}
        self.driver.add_cookie(cookies)
        self.driver.get(
            'https://etaxs.sn-n-tax.gov.cn/xxmh/html/index_origin.html?gopage=true&m1=sbjs&m2=aqysb&fromWhere=&qxkzsx=undefined&tabTitle=null')

    def login(self, account, password, tax_return_url):
        # self.cookie_login()
        # time.sleep(3)
        # return True, 'success'
        dr = self.driver
        dr.maximize_window()
        dr.get(tax_return_url)
        try:
            dr.find_element_by_class_name('layui-layer-close').click()
        except:
            pass
        try:
            js_fun = dr.find_element_by_id('box_close_sy').get_attribute('onclick')
            dr.execute_script(js_fun)
        except:
            pass
        dr.find_element_by_id('userName').send_keys(account)
        dr.find_element_by_id('passWord').send_keys(password)
        self.driver.find_element_by_id('yzmImg').click()
        time.sleep(1)
        loop_num = 0
        empty_num = 0
        # 循环验证图片，直到正确为止
        while True:
            try:
                if loop_num > 10:
                    break
                if empty_num > 3:
                    # 更换百度orc账号
                    pass
                result_bool, code = self.get_code_with_screen_shot()
                if result_bool is False:
                    message = '验证码识别错误'
                    self.logger.to_log('error', message + '=>' + code)
                    return False, message
                if code is '':
                    empty_num += 1
                dr.find_element_by_id('captchCode').clear()
                dr.find_element_by_id('captchCode').send_keys(code)
                dr.find_element_by_id('upLoginButton').click()
                time.sleep(1)
                dr.find_element_by_class_name('layui-layer-shade')
                text = dr.find_element_by_class_name('layui-layer-content').text
                dr.find_element_by_class_name('layui-layer-close').click()
                if text.find('用户名或密码错误') >= 0:
                    message = '登录失败=》用户名或密码错误'
                    self.logger.to_log('error', message)
                    return False, message
                if text.find('认证服务异常') >= 0:
                    self.general.save_result_img()
                    message = '登录失败=》认证服务异常'
                    self.logger.to_log('error', message)
                    return False, message
                time.sleep(1)
                self.logger.to_log('error', '有弹出框，验证码错误：' + code)
                loop_num += 1
                continue
            except:
                result_bool, result_str = self.step.in_to_select_table_page_step('一')
                if result_bool is False:
                    return False, result_str
                message = '账号{}登录成功，并进入选表页面'.format(account)
                self.logger.to_log('info', message)
                return True, message
        if loop_num > 10:
            message = '登录失败=》验证码重试次数过多'
            self.logger.to_log('info', message)
            return False, message

    # 保存截图，并调用百度ocr验证
    def get_code_with_screen_shot(self):
        try:
            img_save_path = Container.PATH + '/static/' + 'shanxi' + '_' + str(int(time.time())) + '_code.png'
            code_img_el = self.driver.find_element_by_id('yzmImg')
            # 放大图片
            self.driver.execute_script(
                "$(arguments[0]).css({width:" + str(Container.CODE_IMG_WIDTH) + ",height:" + str(
                    Container.CODE_IMG_HEIGHT) + "})",
                code_img_el)
            self.driver.save_screenshot(img_save_path)
            left = code_img_el.location['x']
            top = code_img_el.location['y']
            # elementWidth = codeImg.location['x'] + self.codeImgWidth
            # elementHeight = codeImg.location['y'] + self.codeImgHeight
            element_width = code_img_el.location['x'] + code_img_el.size['width']
            element_height = code_img_el.location['y'] + code_img_el.size['height']
            picture = Image.open(img_save_path)
            picture = picture.crop((left, top, element_width, element_height))
            # 保存图片
            picture.save(img_save_path)

            # 调用百度ocr识别
            ocr = Ocr()
            code = ocr.get_code_with_screen_shot(img_save_path)
            code = code.replace(' ', '')
            os.remove(img_save_path)
            return True, code
        except Exception as e:
            return False, str(e)


class LoginInCode(object):

    def __init__(self, account, password):
        super().__init__()
        self.logger = Logger()
        self.account = account
        self.password = password
        self.helper = Helper
        self.prev_code = ''

    def login(self):
        """
        # 第一步，最大化然后根据网址打开页面，并处理可能会出现的弹框
        self.driver.maximize_window()
        self.driver.get(tax_return_url)
        try:
            self.driver.find_element_by_class_name('layui-layer-close').click()
        except:
            pass
        try:
            js_fun = self.driver.find_element_by_id('box_close_sy').get_attribute('onclick')
            self.driver.execute_script(js_fun)
        except:
            pass
        """

        """
        # 第二步，填写用户名密码
        self.driver.find_element_by_id('userName').send_keys(account)
        self.driver.find_element_by_id('passWord').send_keys(password)
        """

        # 第三步，重复三次发送和实验验证码，最大3次
        retry_times = 1
        while True:
            # 0.检查重试次数是否超标
            if retry_times > Container.LOGIN_MAX_RETRY_TIMES:
                self.logger.to_log('info', '重试次数超标')
                return False
            # 1.点击发送验证码的按钮
            openid = self.send_code(self.account, retry_times - 1)
            retry_times += 1
            if openid is False:
                continue
            # 2.每隔5秒请求一次接口
            verification_code = self.loop_request_code(openid, retry_times)
            if verification_code is False:
                continue
            print(self.prev_code)
            # 3.填写验证码，并检验是否正确
            result = self.click_and_check(verification_code)
            if result is Container.LOGIN_ACCOUNT_ERROR or result is Container.LOGIN_AUTH_ERROR:
                return False
            if result is Container.LOGIN_CODE_ERROR:
                continue
            if result is True:
                return True

    def send_code(self, account, retry_times):
        # 发送验证码
        url = Container.PHONE_SEND_CODE
        method = 'POST'
        request_param = {'account': account, 'retry_times': retry_times}
        result_bool, response = HttpClient().to_request_for_code(url, method, request_param)
        self.logger.to_log('info', 'send_code')
        if result_bool is True and response['code'] == 200:
            return response['openid']
        return False

    def loop_request_code(self, openid, retry_times):
        # 每隔5秒请求一次接口
        # 将本次验证码与上次的验证码做比较，如果一致d的话就表示重试请求后的验证码没有变化，还是错误的验证码（不然也不会重试）
        # 重试次数大于1的时候，将请求来的验证码保存下来，为下一次请求的验证码对比做准备
        url = Container.PHONE_GET_CODE
        method = 'POST'
        request_param = dict()
        request_param['openid'] = openid
        request_param['account'] = self.account
        for i in range(int(Container.LOGIN_WAIT_SECOND / Container.LOGIN_REQUEST_INTERVAL)):
            result_bool, response = HttpClient().to_request_for_code(url, method, data=request_param)
            # print(response)
            response = json.loads(response)
            if result_bool is True and response['code'] == 200:
                self.logger.to_log('info', '手机验证码：{}'.format(response['data']))
                if response['data'] == self.prev_code:
                    self.logger.to_log('info', '两次请求验证码结果相同，验证码错误')
                    time.sleep(Container.LOGIN_REQUEST_INTERVAL)
                    continue
                if retry_times > 1:
                    self.prev_code = response['data']
                return response['data']
            self.logger.to_log('info', '未请求到验证码数据')
            time.sleep(Container.LOGIN_REQUEST_INTERVAL)
        self.logger.to_log('info', '本次请求周期5分钟结束')
        return False

    def click_and_check(self, verification_code):
        # 1.填写验证码
        # python_code
        # 2.点击登陆按钮
        # python_code
        print('************验证码：{}**********'.format(verification_code))
        # 检查，如果有弹框，表示有问题
        try:
            self.driver.find_element_by_class_name('layui-layer-shade')
            text = self.driver.find_element_by_class_name('layui-layer-content').text
            self.driver.find_element_by_class_name('layui-layer-close').click()
            if text.find('用户名或密码错误') >= 0:
                message = '登录失败=》用户名或密码错误'
                self.logger.to_log('error', message)
                return Container.LOGIN_ACCOUNT_ERROR
            if text.find('认证服务异常') >= 0:
                self.helper.save_result_img()
                message = '登录失败=》认证服务异常'
                self.logger.to_log('error', message)
                return Container.LOGIN_AUTH_ERROR
            self.logger('error', '登录失败=》验证码错误')
            return Container.LOGIN_CODE_ERROR  # 验证码错误
        except:
            # 没有小框框，表示正确，返回True
            return True

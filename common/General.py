"""
通用方法模块
"""
import json
import os
import time
import threading

from PIL import Image, ImageGrab
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.Container import Container
from common.HttpClient import HttpClient
from common.Logger import Logger
from config import ShanxiTable


class General(object):

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        单例
        :param args:
        :param kwargs:
        :return:
        """
        if not hasattr(General, '_instance'):
            with General._instance_lock:
                if not hasattr(General, "_instance"):
                    General._instance = object.__new__(cls)
        return General._instance

    @staticmethod
    def close_all_windows():
        """
        关闭所有的窗口
        :return:
        """
        driver = Container.DRIVER
        if not driver:
            return False
        all_window_handle = driver.window_handles
        if len(all_window_handle) < 1:
            return False
        for wh in all_window_handle:
            driver.switch_to.window(wh)
            driver.close()

    @staticmethod
    def return_first_window():
        """
        关闭新打开的窗口，并回到第一个窗口去
        :return:
        """
        driver = Container.DRIVER
        if len(driver.window_handles) > 1:
            try:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to.default_content()
            except:
                driver.get(Container.PAGE_HOME_URL)
                time.sleep(5)

    @staticmethod
    def get_task_class_name():
        """
        根据queue_type和type获取任务类
        :return:
        """
        queue_type = Container.COMMON_DATA['queue_type']
        class_name = Container.QUEUE_CLASS_MAP.get(queue_type, 0)
        if class_name is 0:
            return False, '任务类型不存在'
        if queue_type is Container.TASK_TYPE_PAYMENT:
            class_name = Container.TAX_CLASS_MAP.get(Container.COMMON_DATA['type'], 0)
            if class_name == 0:
                return False, '对应任务类不存在'
            else:
                return True, class_name

        return True, class_name

    @staticmethod
    def feedback(status, msg, retry_times=0):
        """
        向大查柜系统反馈
        :param status: 反馈代码 1,2,3
        :param msg: 反馈信息
        :param retry_times: 重试次数，不超过5次
        :return: 终止程序
        """
        logger = Logger()
        # 重试次数不超过5次
        if retry_times > 5:
            logger.to_log('error', '{}反馈重试次数过多'.format(Container.TASK_DATA['id']))
            return
        url = Container.DECLARE_FEEDBACK_URL
        method = 'POST'
        Container.FEEDBACK['status'] = status
        Container.FEEDBACK['message'] = msg
        Container.FEEDBACK['data']['queue_id'] = Container.COMMON_DATA['queue_id']
        Container.FEEDBACK['data']['queue_type'] = Container.COMMON_DATA['queue_type']
        Container.FEEDBACK['data']['relation_status'] = 1  # TODO 获取任务状态
        request_param = Container.FEEDBACK
        print(request_param)
        result, response = HttpClient().to_request_for_declare(method, url, data=request_param)
        if not result:
            logger.to_log('error', response)
            retry_times += 1
            logger.to_log('error', '第{}次反馈重试'.format(retry_times))
            # 递归调用反馈方法，重试机制
            General.feedback(status, msg, retry_times)
        else:
            # 每当反馈成功的时候就把类变量置空
            Container().init_feedback_data()
            try:
                logger.to_log('error', response['message'])
            except Exception as e:
                logger.to_log('error', '反馈成功-数据解析失败 => ' + repr(e))

    @staticmethod
    def in_queue():
        """
        向大查柜查询是否有任务在队列中
        :return: bool, message or data
        """
        url = Container.DECLARE_IN_QUEUE_URL
        method = 'POST'
        result, response = HttpClient().to_request_for_declare(method, url, data=None)
        if not result:
            return False, '请求错误=>' + response
        else:
            try:
                if response['code'] == 200:
                    return True, response['data']
                else:
                    return False, response['message']
            except Exception as e:
                return False, '查询失败-未返回正确的数据格式 => ' + repr(e)

    @staticmethod
    def get_api_data():
        """
        获取table_data数据
        :return:
        """
        return json.loads(Container.TASK_DATA['table_data'])

    @staticmethod
    def wait_to_frame(frame, time_out=15, message=None):
        """
        自动等待并切换iframe
        :param frame: iframe的name或者id
        :param time_out: 超时时间
        :param message: 超时信息
        :return:
        """
        driver = Container.DRIVER
        if message is not None:
            message = '未切换到{} iframe中'.format(frame)
        WebDriverWait(driver, time_out).until(EC.frame_to_be_available_and_switch_to_it(frame), message)

    @staticmethod
    def wait(time_out=15, message=None, id=None, class_name=None, tag_name=None, link_text=None, xpath=None,
             css_selector=None, func=None):
        """
        等待元素
        :param time_out: 超时时间（秒）
        :param message: 超时消息
        :param id:
        :param class_name:
        :param tag_name:
        :param link_text:
        :param xpath:
        :param css_selector:
        :param func:
        :return: bool
        """
        try:
            driver = Container.DRIVER
            if message is not None:
                message = '页面加载超时'
            if id is not None:
                WebDriverWait(driver, time_out).until(
                    EC.visibility_of_any_elements_located((By.ID, id)), message)
            elif class_name is not None:
                WebDriverWait(driver, time_out).until(
                    EC.visibility_of_any_elements_located((By.CLASS_NAME, class_name)), message)
            elif tag_name is not None:
                WebDriverWait(driver, time_out).until(
                    EC.visibility_of_any_elements_located((By.TAG_NAME, tag_name)), message)
            elif link_text is not None:
                WebDriverWait(driver, time_out).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, link_text)), message)
            elif xpath is not None:
                WebDriverWait(driver, time_out).until(
                    EC.visibility_of_any_elements_located((By.XPATH, xpath)), message)
            elif css_selector is not None:
                WebDriverWait(driver, time_out).until(
                    EC.visibility_of_any_elements_located((By.CSS_SELECTOR, css_selector)), message)
            else:
                WebDriverWait(driver, time_out).until(func(driver), message)
            return True, 'success'
        except:
            return False, message

    @staticmethod
    def wait_of_custom(func, error_message='等待超时', timeout=30):
        """
        自定义的等待函数
        :param func: 确定等待结果的函数，务必返回布尔值，可用try...except包起来
        :param error_message: 错误消息
        :param timeout: 超时时间
        :return:
        """
        count = 0
        while True:
            if count > timeout:
                return False, error_message
            count += 1
            if func() is True:
                return True, 'success'
            time.sleep(1)

    @staticmethod
    def mkdir_for_result_img(img_dir):
        """
        创建文件夹
        :param img_dir:
        :return:
        """
        if os.path.exists(img_dir) is False:
            os.makedirs(img_dir)

    @staticmethod
    def get_now_format_date(format_str):
        """
        获取当前格式化的时间
        :param format_str:
        :return:
        """
        return time.strftime(format_str, time.localtime(time.time()))

    @staticmethod
    def save_result_img():
        """
        截图，并保存，将地址放入反馈数据中
        :return:
        """
        img_dir = Container.PATH + '/static/result-img/' + Container.COMMON_DATA['account'] + '/'
        General.mkdir_for_result_img(img_dir)
        img_save_path = img_dir + General.get_now_format_date('%Y%m%d%H%M%S') + '.png'
        im = ImageGrab.grab()
        im.save(img_save_path)
        Container.init_feedback_data()
        Container.FEEDBACK['data']['result_img'].append(img_save_path)
        print(Container.FEEDBACK)

    # @staticmethod
    # def save_result_img(web_driver_element=None):
    #     """
    #     另开多线程截图，保证不会被alert阻塞（待测试）
    #     :param web_driver_element:
    #     :return:
    #     """
    #     lock = threading.Lock()
    #     try:
    #         lock.acquire()
    #         t = threading.Thread(target=General.save_result_img_in_thread, args=(web_driver_element,))
    #         t.start()
    #         t.join()
    #     finally:
    #         lock.release()

    @staticmethod
    def reverse_dict(d):
        """
        字典倒序
        :param d:
        :return:
        """
        inverse = dict()
        l = list()
        for k, v in d.items():
            l.append({k: v})
        l.reverse()
        for v in l:
            inverse.update(v)
        return inverse

    @staticmethod
    def is_number(value):
        """
        判断是否能转成小数
        :param value:
        :return:
        """
        try:
            if float(value) == 0:
                return False
            else:
                return True
        except:
            # 不是数字，直接返回true
            return True

    @staticmethod
    def judge_value(value, xpath):
        """
        对数值和单元格进行检查，不符合条件的返回False，不填
        :param value: 值
        :param xpath: 元素的xpath
        :return: bool
        """
        # 空字符串
        if not value:
            return False
        # 为横扛
        if value == '--':
            return False
        # 如果是数字的话，不能为0
        if General.is_number(value) is False:
            return False
        # 这个单元格不存在
        try:
            element = Container.DRIVER.find_element_by_xpath(xpath)
        except:
            return False
        # 这个单元格只读
        is_readonly = element.get_attribute('readonly')
        if is_readonly is not None:
            return False
        return True

    @staticmethod
    def in_focus(web_driver_element):
        """
        移动焦点至某个元素
        :param web_driver_element:
        :return:
        """
        Container.DRIVER.execute_script('arguments[0].focus();', web_driver_element)

    @staticmethod
    def blur(web_driver_element):
        """
        使某个元素失去焦点
        :param web_driver_element:
        :return:
        """
        Container.DRIVER.execute_script("$(arguments[0]).blur()", web_driver_element)

    @staticmethod
    def press_delete(xpath, num=None):
        """
        按删除键
        :param xpath: 元素所在的xpath
        :param num: 删除次数
        :return:
        """
        el = Container.DRIVER.find_element_by_xpath(xpath)
        if num is None:
            num = len(el.get_attribute('value'))
        while num:
            el.send_keys(Keys.DELETE)
            num -= 1

    @staticmethod
    def fill_in(value, xpath):
        """
        执行具体的表格填充操作
        :param value: str(value)
        :param xpath: 元素的xpath
        :return:
        """
        try:
            element = Container.DRIVER.find_element_by_xpath(xpath)
            element.clear()
            element.click()
            General.press_delete(xpath)
            element.send_keys(value)
            General.blur(element)
            return True
        except:
            return False

    @staticmethod
    def judge_and_fill(value, xpath):
        """
        将判断和填充两个方法结合起来
        :param value:
        :param xpath:
        :return:
        """
        result = General.judge_value(value, xpath)
        if result is False:
            Logger().to_log('info', xpath + '不填')
            return False
        result = General.fill_in(value, xpath)
        if result is False:
            Logger().logger.to_log('error', xpath + '填充错误')
            return False
        return True

    @staticmethod
    def fill_with_three_loop(api_data, local, table_xpath, table_name):
        """
        向表格中填充数据，三重循环，适用于增值税小规模的主表、附表一、附表二，增值税的主表、附表一，文化事业建设主表
        :param api_data: 接口传过来的税种数据
        :param local:  本地的配置文件
        :param table_xpath:  表格的xpath
        :param table_name:  税表的名字
        :return:
        """
        Logger().to_log('info', '等待' + table_name + '表格初始化')
        time.sleep(5)
        try:
            for table_key, table in local.items():
                for row_key, row in table.items():
                    for field_key, field in row.items():
                        # self.logger.to_log('info', row_key + '=>' + field_key + '=>' + field[1])
                        if field[0] == ShanxiTable.FORM_FILL:
                            value = api_data[table_key][row_key][field_key]
                            General.judge_and_fill(value, table_xpath + field[1])
                        time.sleep(1)
        except Exception as e:
            raise Exception(table_name + ' 数据填充错误=>' + str(e))

    @staticmethod
    def fill_with_double_loop(api_data, local, table_xpath, table_name, func=None):
        """
        向表格中填充数据：双重循环，适用于财务报表
        :param api_data: 接口传过来的税种数据
        :param local:  本地的配置文件
        :param table_xpath:  表格的xpath
        :param table_name:  税表的名字
        :param func:  其他方法（目前是企业所得税A类传过来的）
        :return:
        """
        Logger().to_log('info', '等待' + table_name + '表格初始化')
        time.sleep(5)
        try:
            for row_key, row in local.items():
                for field_key, field in row.items():
                    # self.logger.to_log('info', row_key + '=>' + field_key + '=>' + field[1])
                    if field[0] == ShanxiTable.FORM_FILL:
                        value = api_data[row_key][field_key]
                        General.judge_and_fill(value, table_xpath + field[1])
                        if func is not None:
                            func()
                    time.sleep(1)
        except Exception as e:
            raise Exception(table_name + ' 数据填充错误=>' + str(e))

    @staticmethod
    def dict_to_list(data):
        """
        重构数据结构（将字典转成list，用于某些行数不固定的表格）
        :param data:
        :return:
        """
        if not data:
            return False
        new_data = list()
        for row_key, row in data.items():
            new_data.append(row)
        return new_data

    @staticmethod
    def is_exists_select(td_xpath):
        """
        判断表格单元是否为select
        :param td_xpath: select单元格所在的xpath
        :return:
        """
        xpath = td_xpath + '/select'
        try:
            Container.DRIVER.find_element_by_xpath(xpath)
            return True
        except:
            return False

    @staticmethod
    def in_period(input_date):
        """
        判断账期
        :param input_date: 形如2019-01的字符串
        :return:
        """
        tax_model = Container.TASK_DATA['tax_model']
        period = Container.TASK_DATA['period']
        input_date = ''.join(input_date.split('-'))
        if tax_model == Container.DECLARE_TAX_MODEL_SEASON:
            season_last_ym = period.split('-')[2]
            Logger().to_log('info', 'season' + season_last_ym)
            month = General.get_season_month(period)
            if len(month) == 1:
                month = '0' + month
            if season_last_ym[4:6] == '12':
                season_last_ym = str(int(season_last_ym[0:4]) + 1) + month
            else:
                season_last_ym = season_last_ym[0:4] + month
            Logger().to_log('info', 'season' + season_last_ym)
            if season_last_ym == input_date:
                return input_date
        else:
            if period[4:6] == '12':
                period = str(int(period[0:4]) + 1) + '01'
            else:
                month = str(int(period[4:6]) + 1)
                if len(month) == 1:
                    month = '0' + month
                period = period[0:4] + month
            if input_date == period:
                return input_date
        return False

    @staticmethod
    def get_season_month(period):
        month = {
            '1': '4',
            '2': '4',
            '3': '4',
            '4': '7',
            '5': '7',
            '6': '7',
            '7': '10',
            '8': '10',
            '9': '10',
            '10': '1',
            '11': '1',
            '12': '1'
        }
        return month[period.split('-')[2][4:6]]


if __name__ == '__main__':
    Container.DRIVER = webdriver.Chrome()
    # Container.DRIVER.maximize_window()
    # Container.DRIVER.get('file:///C:/Users/Administrator/Desktop/test.html')
    # Container.COMMON_DATA = dict()
    # Container.COMMON_DATA['account'] = '12312312312'
    # Container.PATH = 'C:\\Users\\Administrator\\Desktop'
    # General.save_result_img()
    pass


"""
第一步：获取数据
第二步：登录
第三步：填充数据
第四步：进行申报
"""

import base64
import sys
# sys.path.insert(1, "..")
from multiprocessing.pool import Pool
from time import sleep

from selenium import webdriver

from common.Container import Container
from common.HttpClient import HttpClient
from common.Logger import Logger
from common.General import General
from custom.Login import Login


class Start(object):

    def __init__(self):
        self.Logger = None
        self.general = General()
        self.HttpClient = HttpClient()

    def to_login(self, all_tax_data):
        """
        登录
        :param all_tax_data: 所有税种数据，万一登录失败，要取到其中所有的关联id
        :return:
        """
        password = Container.COMMON_DATA['password']
        account = Container.COMMON_DATA['password']
        result_bool, message = Login().login(account, password, Container.PAGE_LOGIN_URL)
        if result_bool is False:
            # 登录失败
            for tax in all_tax_data:
                Container.FEEDBACK['data']['relation_id'].append(tax['id'])
            self.general.feedback(Container.TASK_RETURN_FAILED, message)
            return result_bool
        else:
            return result_bool

    def loop_run_task(self, all_task_data):
        """
        循环申报同一公司的各条税种
        :param all_task_data: 所有税种/任务数据
        :return:
        """
        for task_data in all_task_data:
            try:
                # 判断报税类
                Container.TASK_DATA = task_data
                result_bool, class_name = self.general.get_task_class_name()
                if result_bool is False:
                    message = 'type:' + str(task_data['type']) + '=>' + class_name
                    self.Logger.to_log('error', message)
                    self.general.feedback(Container.TASK_RETURN_FAILED, message)
                    continue
                # 执行报税操作
                result_bool, message = self.implement(class_name)
                self.general.return_first_window()  # 不管成功失败，先关闭当前页面，回到第一个窗口去
                # 反馈数据放在具体的执行类中，由各人按固定结构自由赋值
                # self.feedback_data['task_type'] = self.common_data['task_type']
                # self.feedback_data['statement_id'].append(task_data['statement_id'])
                # self.feedback_data['result_img'] = self._Base.get_result_img_path()
                # self.feedback_data['payment'] = self._Base.payment
                if result_bool is False:
                    self.Logger.to_log('error', '报税失败，{}，关联ID：{}-{}'.format(message, class_name, task_data['id']))
                    self.general.feedback(Container.TASK_RETURN_FAILED, message)
                else:
                    self.Logger.to_log('error', '报税成功，关联ID:{}-{}'.format(class_name, task_data['id']))
                    self.general.feedback(Container.TASK_RETURN_SUCCESS, message)
                continue
            except Exception as e:
                message = str(e)
                Container.FEEDBACK['status'] = Container.TASK_RETURN_FAILED
                Container.FEEDBACK['message'] = message
                Container.FEEDBACK['data']['queue_id'] = Container.COMMON_DATA['queue_id']
                Container.FEEDBACK['data']['queue_type'] = Container.COMMON_DATA['queue_type']
                Container.FEEDBACK['data']['relation_id'].append(task_data['id'])
                self.Logger.to_log('error', '报税失败，{}=>关联ID:{}'.format(message, task_data['id']))
                self.general.feedback(Container.TASK_RETURN_FAILED, message)
                continue
        # 循环结束后要在发送一次请求，表示本次循环结束，本条队列任务完成
        Container.FEEDBACK['status'] = Container.TASK_RETURN_SUCCESS
        Container.FEEDBACK['message'] = '本次队列完成'
        Container.FEEDBACK['data']['queue_id'] = Container.COMMON_DATA['queue_id']
        self.general.feedback(Container.TASK_RETURN_FAILED, '本次队列完成')

    @staticmethod
    def implement(class_name=None):
        """
        调用相应的类，进行操作
        :param class_name:
        :return:
        """
        __import__('tasks.{class_name}'.format(class_name=class_name))
        return eval('{class_name}().run()'.format(class_name=class_name))

    def run_task(self, common_data, all_task_data):
        """
        业务方法入口
        0.初始化容器里面的数据
        1.登录
        2.循环申报
        3.结束申报
        :param common_data
        :param all_task_data: 所有申报数据
        :return:
        """
        common_data['account'] = base64.b64decode(common_data['account']).decode('utf-8')
        common_data['password'] = base64.b64decode(common_data['password']).decode('utf-8')
        # 初始化容器里面的数据
        Container.init_data(common_data, 'chrome')
        # 登录
        result_bool = self.to_login(all_task_data)
        if result_bool is False:
            # 登录失败，关闭所有窗口，直接return，跳出本方法，取下一个公司数据
            self.general.close_all_windows()
            return
        self.Logger.to_log('info', Container.COMMON_DATA['account_set_id'] + '-登录完成')

        # 循环报税
        self.Logger.to_log('info', Container.COMMON_DATA['account_set_id'] + '-准备任务')
        self.loop_run_task(all_task_data)

        # 结束报税
        self.general.close_all_windows()
        self.Logger.to_log('info', Container.COMMON_DATA['account_set_id'] + '-任务完成')

    def start(self):
        while True:
            # 重新实例化日志类
            self.Logger = Logger()
            self.Logger.to_log('warning', '########################################')
            sleep(2)
            result, data = self.general.in_queue()
            if result is False:
                self.Logger.to_log('error', data)
                continue
            else:
                self.Logger.to_log('warning', data['common_data'].get('account_set_id', None) + '-开始任务')
                # 开始报税
                self.run_task(data['common_data'], data['queue_data'])
                # p.apply_async(self.run_task, args=(data['common_data'], data['task_data'],))


if __name__ == '__main__':
    start = Start()
    start.implement('Added')
    # 反馈测试
    # feedback_data = dict()
    # feedback_data['task_type'] = 2
    # feedback_data['statement_id'] = ['3f699b3650ed677a9040fda3241ae344']
    # feedback_data['payment'] = 10
    # start.feedback(1, '反馈成功', feedback_data, 0)
    # 手机验证码登录测试
    # account = CODE_TEST[random.randint(0, 2)]
    # password = ''
    # login = LoginInCode(account, password)
    # login.login()

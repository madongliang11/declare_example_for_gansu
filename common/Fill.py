import time
from selenium.webdriver.common.keys import Keys
from common.Container import Container
from common.Logger import Logger
from common.Analog import Analog
from config.ShanxiTable import FORM_FILL, FORM_GET, FORM_INIT, FORM_NO


class FillAndGet(object):

    def __init__(self, tax, api_data, local, table_flag, task_type):
        """
        :param tax：税种-5001、zichanfuzhaibiao
        :param api_data: 后端传过来的数据
        :param local:   本地的xpath配置
        :param table_flag: 表格的总体xpath
        :param task_type: 任务的类型
        """
        self.logger = Logger()
        self.driver = Container.DRIVER
        self.analog = Analog()

        self.select_element_type = 'xpath'  # xpath,css_selector,id

        self.tax = tax
        self.api_data = api_data
        self.local = local
        self.table_flag = table_flag
        self.task_type = int(task_type)

        # 需要每个格子进行检查的表格
        self.check_table_list = ['5001']

        # 运行时变量
        self.value = None  # 后端数据的值
        self.flag = None  # css、xpath、id等
        self.table_key = None  # 表格key
        self.row_key = None  # 行key
        self.field_key = None  # 字段key
        self.form_type = None  # 动作类型，fill、get、no、init
        self.element = None  # 单元格元素对象
        self.cell_type = None  # 单元格类型，input、select、radio

    def fill_with_three_loop(self):
        """
        向表格中填充数据，三重循环，适用于增值税小规模的主表、附表一、附表二，增值税的主表、附表一，文化事业建设主表
        备注：财报手动在外层添加一个firstTable，使其变成三层结构
        #:param api_data: 接口传过来的税种数据
        #:param local:  本地的配置文件
        #:param table_xpath:  表格的xpath
        :return:
        """
        time.sleep(5)
        try:
            for table_key, table in self.local.items():
                for row_key, row in table.items():
                    for field_key, field in row.items():
                        if self.task_type == Container.TASK_TYPE_DECLARE:
                            temp_value = self.api_data[table_key][row_key][field_key]
                            # 非主表情况下，只填写有值的
                            if self.judge_value(temp_value, field[0]) is False and self.not_in_check_table_list():
                                continue
                            self.set_self_value(table_key, row_key, field_key, field[1])
                            self.check_and_fill()
                            time.sleep(0.5)
                        elif self.task_type == Container.TASK_TYPE_INIT:
                            if field[0] is not FORM_INIT:
                                continue
                            self.set_self_value(table_key, row_key, field_key, field[1])
                            self.account_data_init()
        except Exception as e:
            raise Exception('数据填充错误=>' + str(e))

    def set_self_value(self, table_key, row_key, field_key, flag):
        """
        设置类变量
        :param table_key:
        :param row_key:
        :param field_key:
        :param flag:
        :return:
        """
        self.table_key = table_key
        self.row_key = row_key
        self.field_key = field_key
        if self.task_type is Container.TASK_TYPE_INIT:
            # 初始化的时候可能根本就没有后端数据
            value = None
        else:
            value = self.api_data[table_key][row_key][field_key]
        self.value = value
        self.flag = self.table_flag + flag
        self.element = self.get_element()
        field = self.local[table_key][row_key][field_key]
        self.form_type = field[0]
        try:
            # 目前只有select类型的field元组中有第三个元素——‘select’
            self.cell_type = field[2]
        except:
            self.cell_type = None

    def not_in_check_table_list(self):
        """
        该表格是否属于要全部检查的表格
        :return:
        """
        if self.tax not in self.check_table_list:
            return True
        else:
            return False

    def account_data_init(self):
        """
        自动初始化方法
        :return:
        """
        if self.form_type is not Container.TASK_TYPE_INIT:
            return False
        if self.element is None or self.element is False:
            raise Exception('寻找页面元素失败')
        page_value = self.get_page_value()
        if page_value is False:
            raise Exception('获取初始化值失败')
        self.update_dict(page_value)

    def check_and_fill(self):
        """
        校验数据
        将判断和填充两个方法结合起来
        :return:
        """
        # 判断是否要填写的
        if self.form_type is FORM_NO:
            return False

        # 判断是否是get类型需要校验的
        if self.form_type is FORM_GET:
            # 针对于要校验的表（5001）
            page_value = self.judge_element(is_check=1)
            if page_value != str(self.value):
                errmsg = self.tax + '-' + self.table_key + '-' + self.row_key + '-' + self.field_key + '位置value：' + page_value
                errmsg += ' 与系统中数据不符合，系统数据为：' + str(self.value)
                raise Exception(errmsg)
            result = True
        elif self.form_type is FORM_FILL:
            result = self.judge_element()
        else:
            result = False

        # 判断校验结果的
        if result is False:
            self.logger.to_log('info', self.flag + '不填')
            return False

        # 在填写之前判断有没有提示弹框
        try:
            point_message = self.driver.find_element_by_xpath("//div[@class='mini-panel-border']").text
            point_message_list = point_message.split()
            point_message_list.pop(0)
            point_message_list.pop()
            point_message = ','.join(point_message_list)
        except:
            point_message = ''

        if point_message != '':
            # 填写出错，抛出错误。
            self.logger.to_log('info', '出现提示错误弹框：{}'.format(point_message))
            raise Exception(point_message)

        # 判断单元格类型的
        if self.cell_type == 'select':
            ok, error_message = self.fill_in_select()
            if ok is False:
                raise Exception(error_message)
            result = True
        else:
            result = self.fill_in_input()

        # 判断填写结果的
        if result is False:
            self.logger.to_log('error', self.flag + '填充错误')
            return False

        return True

    def judge_value(self, value, form_type):
        """
        对数值进行检查，不符合条件的返回False，不填
        :return: bool
        """
        # 这个格子不填
        if form_type is not FORM_FILL:
            return False
        # 空字符串
        if not value:
            return False
        # 为横扛
        if value == '--':
            return False
        # 如果是数字的话，不能为0
        if self.is_number(value) is False:
            return False
        return True

    def judge_element(self, is_check=None):
        """
        对单元格进行检查，不符合条件的返回False，不填
        :param is_check 需要检查每个格子，不需要判断是否只读
        :return: bool
        """
        # 这个单元格不存在
        if self.element is None:
            return False
        # 这个单元格只读
        if is_check is None:
            is_readonly = self.element.get_attribute('readonly')
            is_disable = self.element.get_attribute('disable')
            if is_readonly is None and is_disable is None:
                return True
            else:
                return False
        else:
            return self.get_page_value()

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

    def fill_in_input(self):
        """
        执行具体的表格填充操作
        #:param value: str(value)
        #:param flag: 元素的xpath,css,id...
        :return:
        """
        try:
            self.element.clear()
            self.element.click()
            self.element.send_keys(self.value)
            self.blur(self.element)
            return True
        except:
            return False

    def fill_in_select(self):
        """
        选择减免代码
        #:param code: 减免代码字符串 （self.value）
        #:param td_xpath: 下拉框所在xpath
        :return:
        """

        # 该单元格是否有select元素
        try:
            self.element.find_element_by_tag_name('select')
        except:
            return False, '没有下拉框元素'

        # 该select是否已经自动选取了
        option_value = self.element.find_element_by_tag_name('select').get_attribute('value')
        if option_value:
            return True, 'success'

        # 点击，让options出现
        self.element.click()

        is_error = 0
        is_exists = 0
        options = self.element.find_elements_by_tag_name('option')
        for option in options:
            if option.text == self.value:
                option.click()
                is_exists = 1
                break
        time.sleep(1)
        try:
            self.driver.find_element_by_class_name('mini-tools-close ')
            # 存在，则有错误
            is_error = 1
        except:
            pass
        if is_error == 1:
            return False, '您选择的减免性质没有进行税收减免优惠备案或者税率错误'
        elif is_exists == 0:
            return False, '没有您的减免代码或税率'
        else:
            return True, 'success'

    def get_page_value(self):
        """
        执行具体的获取表格数据操作
        :return:
        """
        try:
            if self.cell_type == 'select':
                page_value = self.element.find_element_by_tag_name('select').get_attribute('value')
            else:
                page_value = self.element.get_attribute('value')
            return page_value
        except:
            return False

    def delete_content(self):
        """
        使用pywin32全选并删除input中的内容
        :return:
        """
        self.analog.key_input_multi(['ctrl', 'a'])
        self.analog.key_input_multi(['del'])

    def get_content(self):
        """
        通过剪贴板制数据
        :return:
        """
        self.analog.set_clipboard('')
        self.analog.key_input_multi(['ctrl', 'a'])
        self.analog.key_input_multi(['ctrl', 'c'])
        # self.analog.set_clipboard(text)
        return self.analog.get_clipboard()

    def press_delete(self, xpath, num=None):
        """
        按删除键
        :param xpath: 元素所在的xpath
        :param num: 删除次数
        :return:
        """
        el = self.driver.find_element_by_xpath(xpath)
        if num is None:
            num = len(el.get_attribute('value'))
        while num:
            el.send_keys(Keys.DELETE)
            num -= 1
            self.driver.switch_to.parent_content()

    def in_focus(self, web_driver_element=None):
        """
        移动焦点至某个元素
        :param web_driver_element:
        :return:
        """
        if web_driver_element is None:
            self.analog.key_input_multi(['enter'])
        else:
            self.driver.execute_script('arguments[0].focus();', web_driver_element)

    def blur(self, web_driver_element=None):
        """
        使某个元素失去焦点
        :param web_driver_element:
        :return:
        """
        if web_driver_element is None:
            self.analog.key_input_multi(['esc'])
        else:
            self.driver.execute_script("$(arguments[0]).blur()", web_driver_element)

    def get_element(self):
        try:
            if self.select_element_type == 'xpath':
                return self.driver.find_element_by_xpath(self.flag)
            elif self.select_element_type == 'css_selector':
                return self.driver.find_element_by_css_selector(self.flag)
            elif self.select_element_type == 'id':
                return self.driver.find_element_by_id(self.flag)
        except:
            return None
        return None

    def update_dict(self, init_value):
        """
        适用于三重循环的获取数据
        #:param tax:
        #:param table_key:
        #:param row_key:
        #:param field_key:
        :param init_value:
        :return:
        """
        if Container.TAX_INIT_DATA.get(self.tax, None) is None:
            Container.TAX_INIT_DATA.update({self.tax: {}})
        if Container.TAX_INIT_DATA[self.tax].get(self.table_key, None) is None:
            Container.TAX_INIT_DATA[self.tax].update({self.table_key: {}})
        if Container.TAX_INIT_DATA[self.tax][self.table_key].get(self.row_key, None) is None:
            Container.TAX_INIT_DATA[self.tax][self.table_key].update({self.row_key: {}})
        if Container.TAX_INIT_DATA[self.tax][self.table_key][self.row_key].get(self.field_key, None) is None:
            Container.TAX_INIT_DATA[self.tax][self.table_key][self.row_key].update({self.field_key: init_value})

    def empty_decorator(self):
        pass

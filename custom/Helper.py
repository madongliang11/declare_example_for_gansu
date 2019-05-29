import datetime
import re
import threading
import time

from common.General import General
from common.Container import Container
from common.Logger import Logger
from config import ShanxiTable


class Helper(object):

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        单例
        :param args:
        :param kwargs:
        :return:
        """
        if not hasattr(Helper, '_instance'):
            with Helper._instance_lock:
                if not hasattr(Helper, "_instance"):
                    Helper._instance = object.__new__(cls)
        return Helper._instance

    def __init__(self):
        self.driver = Container.DRIVER
        self.general = General()
        self.logger = Logger()
        pass

    # 检查申报、缴款、财报的操作结果
    # type = [1,2,3] 1申报查询、2缴款查询、3财报查询
    def check_result(self, result_type):
        Container.DRIVER.switch_to.default_content()
        self.click_left_menu(4)
        time.sleep(2)
        for li_no in result_type:
            self.click_left_menu(4, li_no)
            time.sleep(1)
            self.general.wait_to_frame('ifrMain')
            button_xpath = td_xpath = ''
            if li_no == 1:
                button_xpath = "//div[@class='ui-tax-center-box']/form/table/tbody/tr/td[3]/div[5]/button"
                td_xpath = '//*[@id="sbxxGrid"]/tbody/tr[2]/td[1]'
            elif li_no == 2:
                button_xpath = '//div[@class="searchCriteria"]/div/div[2]/button[1]'
                td_xpath = '//*[@id="dataList"]/tbody/tr[2]/td[2]'
            elif li_no == 3:
                button_xpath = "//div[@class='ui-tax-center-box']/form/table/tbody/tr/td[3]/div[5]/button"
                td_xpath = '//*[@id="cbxxList"]/tbody/tr[2]/td[1]'
            if button_xpath != '' and td_xpath != '':
                self.check_result_save_img(button_xpath, td_xpath)
            self.driver.switch_to.default_content()

    def check_result_save_img(self, button_xpath, td_xpath, next_page=False):
        """
        点击查询按钮、翻页按钮进行对列表的截图
        :param button_xpath: 按钮xpath
        :param td_xpath: 判断是否有数据的xpath
        :param next_page: 下一页是否存在
        :return:
        """
        time.sleep(1)
        if next_page is False:
            self.general.wait(xpath=button_xpath)
            self.driver.find_element_by_xpath(button_xpath).click()
            # 可能会有弹出框，表示无数据，提前退出本函数
            if self.is_have_tips() is True:
                time.sleep(1)
                self.general.save_result_img()
                return
            # 可能需要点两次
            result_bool, _ = self.general.wait(xpath=td_xpath, time_out=5)
            if result_bool is False:
                self.driver.find_element_by_xpath(button_xpath).click()
                self.general.wait(xpath=td_xpath, time_out=5)  # 可能是真的没有，没有就算了
            time.sleep(1)
            self.general.save_result_img()
        try:
            # 如果有下一页，递归调用本函数，进行截图
            self.driver.find_element_by_class_name('laypage_next').click()
            self.check_result_save_img(button_xpath, td_xpath, next_page=True)
        except:
            pass

    # 检查是否有弹框
    def is_have_tips(self):
        time.sleep(1)
        try:
            self.driver.find_element_by_link_text('关闭').click()
            return True
        except:
            return False

    # 点击左侧菜单（按期应申报）
    def click_left_menu(self, top_no, child_no=None):
        if child_no is None:
            self.driver.find_element_by_xpath('//ul[@class="leftmenuul"]/li[' + str(top_no) + ']').click()
        else:
            self.driver.find_element_by_xpath(
                '//ul[@class="leftmenuul"]/li[' + str(top_no) + ']/ul/li[' + str(child_no) + ']/a').click()

    # 去“其他申报”页寻找通用申报表
    def go_other_declare_page(self, table_name):
        self.driver.switch_to.default_content()
        self.click_left_menu(1, 5)
        self.general.wait_to_frame('ifrMain')
        self.general.wait_to_frame('iframeId')
        self.general.wait(xpath='//*[@id="viewCtrlid"]/div/table/tbody/tr[1]/th[1]')
        time.sleep(1)
        # self.driver.switch_to.frame('ifrMain')
        # self.driver.switch_to.frame('iframeId')
        js = 'return document.querySelectorAll(".searchTable tr")[{tr_no}].querySelectorAll("td")[{td_no}]'
        tr_num = len(self.driver.find_elements_by_css_selector('div.searchTable>table>tbody>tr'))
        table_map = dict()
        for i in range(tr_num):
            if i == 0:
                continue
            tax_name = self.driver.execute_script(js.format(tr_no=i, td_no=1)).text
            opera = self.driver.execute_script(js.format(tr_no=i, td_no=6)).text
            if tax_name == table_name:
                table_map = {
                    'table_name': tax_name,
                    'opera': opera,
                    'tr_no': i
                }
                break

        if len(table_map) == 0:
            raise Exception(table_name + '不在其他申报中')
        self.driver.execute_script(js.format(tr_no=table_map['tr_no'], td_no=6)).click()

    # 按期应申报页面
    def go_curr_period_page(self):
        self.driver.switch_to.default_content()
        self.click_left_menu(1, 1)
        time.sleep(2)

    def select_table_for_finance(self):
        # 点击相应的申报表 首先切换iframe
        self.driver.switch_to.frame('lhsbIframe')
        time.sleep(1)
        js = "return document.querySelectorAll('.searchTable')[1].querySelectorAll('tr')[{tr_no}].querySelectorAll('td')[{td_no}]"
        tr_num = len(self.driver.find_elements_by_xpath('//*[@id="viewCtrlid"]/div[4]/div/table/tbody/tr'))
        is_exists = 0
        tr_no = 0
        if int(self.info['type']) == 12:
            table_name = '小企业会计准则'
        else:
            table_name = '企业会计准则'
        for i in range(tr_num):
            if i == 0:
                continue
            tax_name = self.driver.execute_script(js.format(tr_no=i, td_no=1)).text
            start_date = self.driver.execute_script(js.format(tr_no=i, td_no=3)).text
            end_date = self.driver.execute_script(js.format(tr_no=i, td_no=4)).text
            declare_date = self.driver.execute_script(js.format(tr_no=i, td_no=6)).text
            tr_no = i
            # 名字不一样
            if tax_name != table_name:
                continue
            # 日期大于300天
            if self.sub_two_day(start_date, end_date) is False:
                continue
            # 申报日期有值，表示已经申报了
            if declare_date != '':
                return False, Container.TABLE_ALREADY_DECLARE
            is_exists = 1
            break

        if is_exists == 1:
            # 点击申报
            self.driver.execute_script(js.format(tr_no=tr_no, td_no=7)).click()
            return True, Container.TABLE_EXISTS
        else:
            return True, Container.TABLE_NOT_EXISTS

    def get_all_table_finance(self):
        js = "return document.querySelectorAll('.searchTable')[1].querySelectorAll('tr')[{tr_no}].querySelectorAll('td')[{td_no}]"
        tr_num = len(self.driver.find_elements_by_xpath('//*[@id="viewCtrlid"]/div[4]/div/table/tbody/tr'))
        table_map = dict()
        for i in range(tr_num):
            if i == 0:
                continue
            tax_name = self.driver.execute_script(js.format(tr_no=i, td_no=1)).text
            start_date = self.driver.execute_script(js.format(tr_no=i, td_no=3)).text
            end_date = self.driver.execute_script(js.format(tr_no=i, td_no=4)).text
            deadline = self.driver.execute_script(js.format(tr_no=i, td_no=5)).text
            declare_date = self.driver.execute_script(js.format(tr_no=i, td_no=6)).text
            tr_no = i
            if self.sub_two_day(start_date, end_date) is False:
                continue
            table_map.update({
                tax_name: {
                    'tax_name': tax_name,
                    'start_date': start_date,
                    'end_date': end_date,
                    'deadline': deadline,
                    'declare_date': declare_date,
                    'tr_no': tr_no
                }
            })
        return table_map

    @staticmethod
    def sub_two_day(start_date, end_date):
        d1 = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        delta = d2 - d1
        if delta.days > 300:
            return False
        else:
            return True

    # 获取要报税的表格
    def select_table(self, table_name):
        """
        获取到所有税表信息后，对比当前税种，进行报税
        :param: table_name
        :return:
        """
        # 获取所有税种信息
        js = 'return document.querySelectorAll("#gdslhsb tr")[{tr_no}].querySelectorAll("td")[{td_no}]'
        self.general.wait(xpath='//*[@id="gdslhsb"]/tbody/tr[1]/th[1]')
        table_map = self.get_all_table(js)

        # 判断是否存在该表
        if len(table_map) == 0:
            return False, Container.TABLE_NOT_EXISTS
        # 判断是否存在该表
        if table_map.get(table_name, '') == '':
            return False, Container.TABLE_NOT_EXISTS
        # 判断该表是否已经申报
        if table_map[table_name]['opera'] == '已申报' or table_map[table_name]['declare_date'] != '':
            return False, Container.TABLE_ALREADY_DECLARE
        self.driver.execute_script(js.format(tr_no=table_map[table_name]['tr_no'], td_no=6)).click()
        time.sleep(1)
        # 防止出现弹框，点击确认
        if table_name != '增值税纳税申报表（一般纳税人适用）':
            try:
                self.driver.switch_to.parent_frame()
                self.driver.find_element_by_class_name('layui-layer-btn0').click()
            except:
                pass
        return True, Container.TABLE_EXISTS

    def get_all_table(self, js):
        """
        获取一般税表的所有信息
        :param js:
        :return: dict
        """
        self.general.wait_to_frame('lhsbIframe')
        tr_num = len(self.driver.find_element_by_id('gdslhsb').find_elements_by_tag_name('tr'))
        table_map = dict()

        # 获取到这个税种的申报信息
        for i in range(tr_num):
            if i == 0:
                continue
            tax_name = self.driver.execute_script(js.format(tr_no=i, td_no=1)).text  # 申报表
            start_date = self.driver.execute_script(js.format(tr_no=i, td_no=2)).text  # 税（费）款所属期起
            end_date = self.driver.execute_script(js.format(tr_no=i, td_no=3)).text  # 税（费）款所属期止
            deadline = self.driver.execute_script(js.format(tr_no=i, td_no=4)).text  # 申报期限
            declare_date = self.driver.execute_script(js.format(tr_no=i, td_no=5)).text  # 申报日期
            opera = self.driver.execute_script(js.format(tr_no=i, td_no=6)).text  # 操作
            table_map.update({
                tax_name: {
                    'tax_name': tax_name,
                    'start_date': start_date,
                    'end_date': end_date,
                    'deadline': deadline,
                    'declare_date': declare_date,
                    'opera': opera,
                    'tr_no': i,
                }
            })

        return table_map

    def get_table_info_list(self, table_xpath, td_map):
        """
        通用的获取表格信息，返回list
        :param table_xpath: 表格的xpath
        :param td_map: 字段与td序号的对应字典
        :return: list
        """
        result_list = list()
        if table_xpath[-6:] != '/tbody':
            table_xpath += '/tobdy/tr'
        else:
            table_xpath += '/tr'
        tr_num = len(self.driver.find_elements_by_xpath(table_xpath))
        table_xpath += '[{tr_no}]/td[{td_no}]'

        # 获取到这个税种的申报信息
        for i in range(tr_num):
            if i == 0:
                continue
            map_in_list = {}
            for td in td_map:
                result = self.driver.find_element_by_xpath(table_xpath.format(tr_no=i + 1, td_no=td_map.get(td))).text
                map_in_list.update({
                    td: result
                })
            map_in_list.update({'tr_no': i + 1})
            result_list.append(map_in_list)

        return result_list

    # 点击申报按钮，进行申报
    def to_declare(self, table_name):
        self.logger.to_log('info', table_name + '准备点击申报按钮')
        self.driver.find_element_by_link_text('申报').click()
        time.sleep(1)
        # Base.payment = 1230000
        # time.sleep(3)
        # return
        # 假如会出错
        title_text = self.driver.find_element_by_class_name('layui-layer-dialog').find_element_by_class_name(
            'layui-layer-title').text
        self.logger.to_log('info', title_text)
        if title_text.find('表格存在填写错误的数据') >= 0:
            error_message = table_name + '数据集不正确'
            raise Exception(error_message)
        time.sleep(5)
        # 提示自动选票功能
        try:
            self.driver.find_element_by_link_text('确认').click()
        except:
            pass
        time.sleep(5)
        # 申报选择框
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.logger.to_log('info', '等待15秒钟')
        time.sleep(10)

        self.driver.switch_to.frame('frmMain')
        body_string = self.driver.find_element_by_tag_name('body').text
        if body_string.find('您的申报表比对结果不通过') >= 0:
            raise Exception('申报表比对结果不通过')
        if body_string.find('纳服支撑平台错误') >= 0:
            raise Exception('纳服支撑平台错误')
        Container.FEEDBACK['data']['payment'] = self.get_payment(body_string)
        self.driver.switch_to.default_content()

        # 可能会提示没有抄税，没有提示抄税就在等待时间后点确定
        cs_error_message = ''
        try:
            # layui-layer-ico5  layui-layer-close layui-layer-content  您尚未进行抄报税，无法申报！
            self.driver.find_element_by_class_name('layui-layer-ico5')
            cs_error_message = table_name + '用户尚未抄税'
        except:
            pass
        if cs_error_message:
            raise Exception(cs_error_message)

        if Container.FEEDBACK['data']['payment'] is False:
            # 增值税=》获取提示框中的文字
            try:
                body_string = self.driver.find_element_by_class_name('layui-layer-content').text
                Container.FEEDBACK['data']['payment'] = self.get_payment(body_string)
            except:
                pass

        self.driver.switch_to.frame('frmMain')
        # self.payment = self.get_payment(body_string)
        # if self.payment is False:
        #     self.payment = 0
        if not Container.FEEDBACK['data']['payment']:
            Container.FEEDBACK['data']['payment'] = 0

        self.logger.to_log('info', table_name + '申报确定')

    @staticmethod
    def get_payment(body_string=None):
        try:
            return float(re.search('税款金额：([\d\.]+)元', body_string).groups()[0]) * 10000
        except:
            return False

    # 缴款操作
    def to_pay(self):
        self.click_left_menu(2)
        time.sleep(2)
        self.click_left_menu(2, 2)
        time.sleep(2)
        self.driver.switch_to.frame('ifrMain')
        tax_price = self.driver.find_element_by_id('hjAll').text
        if float(tax_price) == 0:
            self.general.save_result_img()
            return False
        self.driver.find_element_by_id('a_main_ljjk').click()
        button_a_array = self.driver.find_elements_by_css_selector('div#pay_moda>div#model_btn>a')
        for button in button_a_array:
            if button.value_of_css_property('display') != 'none':
                button.click()
        time.sleep(5)
        # 获取焦点，滚动条到最下方
        self.general.in_focus(self.driver.find_element_by_id('pay_result_ds_grid'))
        return True

    # 获取填表页面的左侧所有表格名（该税种所有可能需要填写的表格）（文化事业建设）
    # 增值税、财务报表、企业所得税
    def get_left_table(self):
        tax_all_table = []
        self.driver.switch_to.frame('frmMain')
        lis = self.driver.find_elements_by_xpath('//ul[@id="divSheetlist"]/li')
        for index, li in enumerate(lis):
            tax_all_table.append(li.find_element_by_tag_name('a').text)
        return tax_all_table

    # 重构数据结构（将字典转成list，用于某些行数不固定的表格）
    @staticmethod
    def dict_to_list(data):
        if not data:
            return False
        new_data = list()
        for row_key, row in data.items():
            new_data.append(row)
        return new_data

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    '                             填表相关区                                   
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    # 填写radio
    def fill_with_radio_yesno(self, api_table, local, table_xpath, table_name, text_list, func=None):
        """
        填写是与否的单选框
        :param api_table: 接口数据
        :param local: 本地配置
        :param table_xpath: 表格的xpath
        :param table_name: 表格名字
        :param text_list: 可能需要填写的input列表
        :param func: 企业所得税A类中传过来的方法
        :return:
        """
        self.logger.to_log('info', '等待' + table_name + '表格初始化')
        time.sleep(5)
        try:
            for row_key, row in local.items():
                for field_key, field in row.items():
                    self.logger.to_log('info', row_key + '=>' + field_key + '=>' + field[1])
                    if field[0] == ShanxiTable.FORM_FILL:
                        text_key = row_key + '-' + field_key
                        value = api_table[row_key][field_key]
                        if text_key in text_list:
                            self.general.judge_and_fill(value, table_xpath + field[1])
                            continue
                        # 企业所得税A类几个顽固的单选框
                        if func is not None:
                            func(row_key, field_key, field, value)
                        self.click_radio_yesno(table_xpath + field[1], value)
                        time.sleep(1)
        except Exception as e:
            raise Exception(table_name + ' 数据填充错误=>' + str(e))

    def click_radio_yesno(self, xpath, yes_or_no):
        """
        点击是与否的单选框
        :param xpath:
        :param yes_or_no:
        :return:
        """
        if yes_or_no is Container.RADIO_YES:
            yn = 0
        else:
            yn = 1
        yn_element = self.driver.find_elements_by_xpath(xpath)[yn]
        status = yn_element.get_attribute('disabled')
        if status is not None:
            return False
        # yn_element.click()
        # yn_element.click()
        self.driver.execute_script("arguments[0].click()", yn_element)
        self.driver.execute_script("arguments[0].click()", yn_element)
        return True

    def is_exists_select(self, td_xpath):
        """
        判断表格单元是否为select
        :param td_xpath: select单元格所在的xpath
        :return:
        """
        xpath = td_xpath + '/select'
        try:
            self.driver.find_element_by_xpath(xpath)
            return True
        except:
            return False

    def select_reduction_code(self, code, select_xpath, td_no=None):
        """
        选择减免代码
        :param code: 减免代码字符串
        :param select_xpath: 下拉框所在xpath  形如.../select/option格式
        :param td_no: td_no，5009营改增需要这个参数
        :return:
        """
        is_error = 0
        is_exists = 0
        options = self.driver.find_elements_by_xpath(select_xpath)
        for option in options:
            if option.text == code:
                option.click()
                is_exists = 1
                break
            # 这个if专为5009增值税营改增而写
            if td_no is not None and td_no == 1 and option.get_attribute('label') == code:
                self.driver.find_element_by_id('select2-drop-mask').click()
                is_exists = 1
                break
        time.sleep(1)
        try:
            self.driver.find_element_by_class_name('layui-layer-close').click()
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

    def confirm(self):
        """
        2019年初 处理弹出框
        :return:
        """
        self.general.wait_to_frame('frmMain')
        try:
            self.driver.find_element_by_class_name('layui-layer-btn0').click()
        except:
            pass
        self.driver.switch_to.default_content()

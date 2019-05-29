"""
CorporateIncomeTaxA
企业所得税A类
表ID：8001
"""
import time

from selenium.webdriver.support.select import Select

from app import Constant
from app.config import ShanxiTable
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class CorporateIncomeTaxA(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = '//div[@class="NewTableMain"]/table[1]/tbody'
        self.text_list = [
            'threeRow-projectOne'
        ]

    def run(self):
        self.logger.to_log('info', '企业所得税')
        dr = self.driver
        self.info['table_name'] = '居民企业（查账征收）企业所得税月（季）度申报（2018年版）'
        data = self.data['8001']

        result_bool, result_str = self.step.judge_period_and_select_table_step('二')
        if result_bool is True and result_str == Constant.TABLE_ALREADY_DECLARE_STR:
            # 已经申报过了
            return True, self.info['table_name'] + '=>' + result_str
        elif result_bool is False:
            return False, self.info['table_name'] + '=>' + result_str

        result_bool, result_str = self.step.change_window_handle_step('三')
        if result_bool is False:
            return False, self.info['table_name'] + '=>' + result_str

        try:
            # 步骤四：填写数据
            self.logger.to_log('info', '步骤四开始')
            time.sleep(5)
            local = ShanxiTable.corporate_income_tax_A()
            dr.switch_to.frame('frmMain')
            dr.switch_to.frame('frmSheet')

            # firstTable_local = local['firstTable']
            second_local = local['secondTable']
            third_local = local['thirdTable']
            fourth_local = local['fourthTable']
            left_a = '《A200000中华人民共和国企业所得税月（季）度预缴纳税申报表（A类，2018年版）》'

            # 中间部分
            self.helper.fill_with_double_loop(data['secondTable'], second_local, self.table_xpath, left_a,
                                              self.click_yes)
            self.helper.fill_with_double_loop(data['thirdTable'], third_local, self.table_xpath, left_a, self.click_yes)
            # 填写表头部分（预缴方式）税网带出来的，不填
            # self.fill_in_to_radio(data['firstTable'], firstTable_local, element_tbody, left_a)
            # 尾部部分
            tail_xpath = '//div[@class="NewTableMain"]/table[2]/tbody'

            self.helper.fill_with_radio_yesno(data['fourthTable'], fourth_local, tail_xpath, left_a, self.text_list,
                                              self.js_click_radio)

            # 选择非代理申报
            self.select_no_proxy_in_xpath()
            self.logger.to_log('info', '步骤四结束')
            time.sleep(5)
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤四：填写数据出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        result_bool, result_str = self.step.to_declare_step('五')

        if result_bool is False:
            return result_bool, self.info['table_name'] + '=>' + result_str
        else:
            return True, self.info['table_name'] + '=>报税成功'

    @staticmethod
    def js_click_radio(row_key, field_key, field, yes_or_no):
        if yes_or_no is Constant.RADIO_YES:
            yn = 0
        else:
            yn = 1
        js = "$('.NewTableMain table').eq(1).find('tr').eq({tr_num}).find('td')" \
             ".eq(1).find('input').eq({input_num}).click()"
        if row_key == 'twoRow' and field_key == 'projectOne' and field[1] == r'//tr[3]/td[2]/input':
            # 企业所得税A类中这个地方的radio莫名其妙的选不中
            Base.driver.execute_script(js.format(tr_num=2, input_num=yn))
            Base.driver.execute_script(js.format(tr_num=2, input_num=yn))
            return True
        if row_key == 'oneRow' and field_key == 'projectOne' and field[1] == r'//tr[2]/td[2]/input':
            # 企业所得税A类中这个地方的radio莫名其妙的选不中
            Base.driver.execute_script(js.format(tr_num=1, input_num=yn))
            Base.driver.execute_script(js.format(tr_num=1, input_num=yn))
            return True

    def select_no_proxy_in_xpath(self):
        self.logger.to_log('info', '选择非代理申报')
        xpath = '//div[@class="NewTableMain"]/table[2]/tbody/tr[7]/td'
        self.driver.find_element_by_xpath(xpath + '/div[2]/div[2]/input[2]').click()
        id_num = self.driver.find_element_by_xpath('//div[@class="NewTableTop"]/table/tbody/tr[1]/td/span').text
        name = self.driver.find_element_by_xpath('//div[@class="NewTableTop"]/table/tbody/tr[2]/td/span').text
        Select(self.driver.find_element_by_xpath(xpath + '/div[1]/div[4]/select')).select_by_visible_text('组织机构代码证')
        self.driver.find_element_by_xpath(xpath + '/div[1]/div[3]/input').send_keys(name)
        self.driver.find_element_by_xpath(xpath + '/div[1]/div[5]/input').send_keys(id_num)

    @staticmethod
    def click_yes():
        try:
            time.sleep(1)
            Base.driver.switch_to.parent_frame()
            Base.driver.find_element_by_class_name('layui-layer-dialog')
            Base.driver.find_element_by_link_text('是').click()
            Base.driver.switch_to.frame('frmSheet')
        except:
            Base.driver.switch_to.frame('frmSheet')
            pass

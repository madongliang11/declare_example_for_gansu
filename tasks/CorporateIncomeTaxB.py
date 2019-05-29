"""
CorporateIncomeTaxB
企业所得税B类
表ID：8008
"""
import time

from selenium.webdriver.support.select import Select

from app import Constant
from app.config import ShanxiTable
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class CorporateIncomeTaxB(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = '//div[@class="NewTableMain"]/table/tbody'
        self.text_list_third = ['oneRow-number']
        self.text_list_fourth = ['oneRow-projectOne', 'twoRow-projectOne', 'twoRow-country']

    def run(self):
        self.logger.to_log('info', '企业所得税')
        dr = self.driver
        self.info['table_name'] = '居民企业（核定征收）企业所得税月（季）度及年度申报（2018年版）'
        data = self.data['8008']

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
            self.helper.wait_to_frame('frmMain')
            self.helper.wait_to_frame('frmSheet')
            local = ShanxiTable.corporate_income_tax_B()
            left_a = '《B100000中华人民共和国企业所得税月（季）度预缴和年度纳税申报表（B类，2018年版）》'
            # first_local = local['firstTable']
            second_local = local['secondTable']
            third_local = local['thirdTable']
            fourth_local = local['fourthTable']

            # 头部，税网带出来的，不填
            # 中部
            self.helper.fill_with_double_loop(data['secondTable'], second_local, self.table_xpath, left_a)
            # 底部
            self.helper.fill_with_radio_yesno(data['thirdTable'], third_local, self.table_xpath, left_a,
                                              self.text_list_third)
            self.helper.fill_with_radio_yesno(data['fourthTable'], fourth_local, self.table_xpath, left_a,
                                              self.text_list_fourth)
            # 选择非代理申报
            self.select_no_proxy_in_xpath()
            time.sleep(1)
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

    def select_no_proxy_in_xpath(self):
        self.logger.to_log('info', '选择非代理申报')
        # 选择非代理申报
        xpath = '//div[@class="NewTableTop"][2]/table/tbody/tr/td/div/table/tbody'
        table_element = self.driver.find_element_by_xpath(xpath)
        table_element.find_element_by_xpath('//tr[2]/td[2]/input[2]').click()
        id_num = self.driver.find_element_by_xpath('//div[@class="NewTableTop"]/table/tbody/tr[1]/td/span').text
        name = self.driver.find_element_by_xpath('//div[@class="NewTableTop"]/table/tbody/tr[2]/td/span').text
        Select(self.driver.find_element_by_xpath(xpath + '/tr[4]/td[1]/select')).select_by_visible_text(
            '组织机构代码证')
        self.driver.find_element_by_xpath(xpath + '/tr[5]/td[1]/input').send_keys(id_num)
        self.driver.find_element_by_xpath(xpath + '/tr[3]/td[1]/input').send_keys(name)

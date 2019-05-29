"""
FinanceSmall
财务报表=》小企业会计准则
表ID：zichanfuzhaibiao,lirunbiao,xianjinliuliangbiao
"""
import time

from app import Constant
from app.config import ShanxiTable
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class FinanceSmall(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = '//*[@id="viewCtrlId"]/div[3]/table/tbody'

    def run(self):
        self.logger.to_log('info', '财务报表=》小企业会计准则=》finance_small_company')
        dr = self.driver
        self.info['table_name'] = '小企业会计准则'
        data = self.data

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
            # 步骤四，选择季报或月报
            time.sleep(5)
            self.logger.to_log('info', '步骤四开始')
            self.change_tax_model()
            dr.find_element_by_link_text('下一步').click()
            time.sleep(3)
            self.logger.to_log('info', '步骤四结束')
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤四：选择季报或月报出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        try:
            # 步骤五，填充数据
            self.logger.to_log('info', '步骤五开始')
            time.sleep(5)
            local = ShanxiTable.get_local_finance_small()
            if int(self.info['tax_model']) == Constant.MONTH_DECLARE:
                # left_a = {'zichanfuzhaibiao': '资产负债表', 'lirunbiao': '利润表_月报', 'xianjinliuliangbiao': '现金流量表_月报'}
                left_a = {'zichanfuzhaibiao': '资产负债表', 'lirunbiao': '利润表_月报'}
            else:
                # left_a = {'zichanfuzhaibiao': '资产负债表', 'lirunbiao': '利润表_季报', 'xianjinliuliangbiao': '现金流量表_季报'}
                left_a = {'zichanfuzhaibiao': '资产负债表', 'lirunbiao': '利润表_季报'}
            left_a = self.helper.reverse_dict(left_a)
            # 财务报表写死
            # all_table_in_page = self.get_left_table()
            # all_table_in_data = data.keys()
            # for data_table in all_table_in_data:
            #     if data_table not in all_table_in_page or data_table not in left_a.keys():
            #         left_a.pop(data_table)
            for key, val in left_a.items():
                time.sleep(2)
                dr.switch_to.frame('frmMain')
                dr.find_element_by_link_text(val).click()
                self.driver.switch_to.frame('frmSheet')
                self.helper.fill_with_double_loop(data[key], local[key], self.table_xpath, val)
                dr.switch_to.default_content()
            self.logger.to_log('info', '步骤五结束')
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤五：填写数据出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        result_bool, result_str = self.step.to_declare_step('五')

        if result_bool is False:
            return result_bool, self.info['table_name'] + '=>' + result_str
        else:
            return True, self.info['table_name'] + '=>报税成功'

    # 改变财务报表中的申报类型
    def change_tax_model(self):
        self.driver.switch_to.frame('iframehtm')
        if self.info['tax_model'] == Constant.MONTH_DECLARE:
            self.driver.find_element_by_id('bsqjId').click()
            el_option = self.driver.find_element_by_id('bsqjId').find_elements_by_tag_name('option')
            for option in el_option:
                if option.text == '月报':
                    option.click()
        else:
            self.driver.find_element_by_id('bsqjId').click()
            el_option = self.driver.find_element_by_id('bsqjId').find_elements_by_tag_name('option')
            for option in el_option:
                if option.text == '季报':
                    option.click()
        time.sleep(1)
        self.driver.switch_to.default_content()

    '''''''''''''''''''''''''''''''''''''''''
    '               获取数据
    '''''''''''''''''''''''''''''''''''''''''
    def run_for_init(self):
        # 步骤五，填充数据
        self.logger.to_log('info', '步骤五开始')
        time.sleep(5)
        local = ShanxiTable.get_local_finance_small()
        if int(self.info['tax_model']) == Constant.MONTH_DECLARE:
            # left_a = {'zichanfuzhaibiao': '资产负债表', 'lirunbiao': '利润表_月报', 'xianjinliuliangbiao': '现金流量表_月报'}
            left_a = {'zichanfuzhaibiao': '资产负债表', 'lirunbiao': '利润表_月报'}
        else:
            # left_a = {'zichanfuzhaibiao': '资产负债表', 'lirunbiao': '利润表_季报', 'xianjinliuliangbiao': '现金流量表_季报'}
            left_a = {'zichanfuzhaibiao': '资产负债表', 'lirunbiao': '利润表_季报'}
        left_a = self.helper.reverse_dict(left_a)
        # 财务报表写死
        # all_table_in_page = self.get_left_table()
        # all_table_in_data = data.keys()
        # for data_table in all_table_in_data:
        #     if data_table not in all_table_in_page or data_table not in left_a.keys():
        #         left_a.pop(data_table)
        for key, val in left_a.items():
            time.sleep(2)
            self.driver.switch_to.frame('frmMain')
            self.driver.find_element_by_link_text(val).click()
            self.driver.switch_to.frame('frmSheet')
            self.helper.fill_with_double_loop(data[key], local[key], self.table_xpath, val)
            self.driver.switch_to.default_content()
        self.logger.to_log('info', '步骤五结束')

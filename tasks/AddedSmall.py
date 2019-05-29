"""
AddedSmall
增值税报表=》小规模纳税人
表ID：5004、5005、5010
"""
import time

from app import Constant
from app.config import ShanxiTable
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class AddedSmall(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = '//*[@id="viewCtrlId"]/div[3]/table'
        self.table_xpath_5010 = '//*[@id="viewCtrlId"]/div[3]/table[1]'
        # 5010减免税，select字段与td的映射关系
        self.select_td_map_5010 = {
            'project': 1,
        }

    def run(self):
        self.logger.to_log('info', '增值税报表=》小规模纳税人=》added_small')
        dr = self.driver
        self.info['table_name'] = '增值税纳税申报表（小规模纳税人适用）'
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
            # 步骤四：填写数据
            time.sleep(3)
            self.logger.to_log('info', '步骤四开始')

            self.helper.confirm()

            local = ShanxiTable.get_local_added_small()
            left_a = {
                '5004': '《增值税纳税申报表（适用小规模纳税人）》',
                # '5005': '《增值税纳税申报表（适用于增值税小规模纳税人）附列资料》',
                '5010': '《增值税减免税申报明细表》'
            }
            left_a = self.helper.reverse_dict(left_a)
            # 只取可以填的表格
            all_table_in_page = self.helper.get_left_table()
            all_table_in_data = data.keys()
            left_a_new = dict()
            for table_key in left_a:
                if table_key in all_table_in_data and left_a[table_key] in all_table_in_page:
                    left_a_new[table_key] = left_a[table_key]
            dr.switch_to.default_content()
            for key, val in left_a_new.items():
                time.sleep(2)
                dr.switch_to.frame('frmMain')
                dr.find_element_by_link_text(val).click()
                time.sleep(2)
                dr.switch_to.frame('frmSheet')
                if key == '5010':
                    self.fill_into_5010(data[key], local[key], val)
                else:
                    self.helper.fill_with_three_loop(data[key], local[key], self.table_xpath, val)
                if key == '5004':
                    self.select_voluntarily_declare()
                dr.switch_to.default_content()

            self.logger.to_log('info', '步骤四结束')
            time.sleep(5)
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤四：填写数据出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        result_bool, result_str = self.step.to_declare_step('五')

        # 不管成功失败，先回到原先的页面去
        # self.helper.return_first_window()

        if result_bool is False:
            return result_bool, self.info['table_name'] + '=>' + result_str
        else:
            return True, self.info['table_name'] + '=>报税成功'

    # 增值税小规模主表选择自行申报操作
    def select_voluntarily_declare(self):
        self.logger.to_log('info', '选择自行申报')
        self.driver.find_element_by_id('sfzxsb_Y').click()
        self.driver.find_element_by_id('s2id_select2').click()
        el_option = self.driver.find_element_by_id('select2').find_elements_by_tag_name('option')
        for option in el_option:
            if option.text == '组织机构代码证':
                option.click()
                break
        no = self.driver.find_element_by_xpath('//div[@class="NewTableTop"]/table/tbody/tr[1]/td[2]/span').text
        self.driver.find_element_by_xpath('//*[@id="viewCtrlId"]/div[3]/table/tbody/tr[29]/td[5]/input').send_keys(no)

    '''''''''''''''''''''''''''''''''''''''''''''''''''''
    '                   5010减免税表
    '''''''''''''''''''''''''''''''''''''''''''''''''''''

    # 增值税（小规模纳税人）减免税申报明细表（这里实际上是两张表）
    def fill_into_5010(self, api_data, local, table_name):
        self.logger.to_log('info', '等待' + table_name + '表格初始化')
        time.sleep(5)
        try:
            for index in range(2):
                if index == 0:
                    local_template = local['secondTable']
                    start_line = 5
                    table_xpath = '//*[@id="viewCtrlId"]/div[3]/table[1]/tbody'
                    add_button_xpath = table_xpath + '/tr[5]/td[8]/div/a'
                    data_type_list = self.helper.dict_to_list(api_data['secondTable'])
                else:
                    local_template = local['fourthTable']
                    start_line = 8
                    table_xpath = '//*[@id="viewCtrlId"]/div[3]/table[2]/tbody'
                    add_button_xpath = table_xpath + '/tr[8]/td[8]/div/a'
                    data_type_list = self.helper.dict_to_list(api_data['fourthTable'])
                if not data_type_list:
                    return
                self.fill_into_one_5010(index, start_line, local_template, data_type_list, table_xpath,
                                        add_button_xpath)
                time.sleep(2)
        except Exception as e:
            raise Exception(table_name + ' 数据填充错误=>' + str(e))

    # 填写5010的两张表
    def fill_into_one_5010(self, index, start_line, local_template, api_data, table_xpath, add_button_xpath):
        dict_key = 0
        total_line = len(self.driver.find_elements_by_xpath(table_xpath + '/tr'))
        # 返回的是个list，而不是dict
        if index == 1:
            total_line -= 1
        trs = dict()
        all_line = start_line + len(api_data)
        while start_line < all_line:
            trs.update({dict_key: start_line})
            if start_line > total_line:
                self.driver.find_element_by_xpath(add_button_xpath).click()
            start_line += 1
            dict_key += 1

        for hurdles, tr_no in trs.items():
            data_line = api_data[hurdles]
            for field_key, field in data_line.items():
                if field_key in local_template and (local_template[field_key][0] == ShanxiTable.FORM_FILL):
                    if field_key in self.select_td_map_5010 and field != '':
                        td_no = self.select_td_map_5010[field_key]
                        td_xpath = table_xpath + '/tr[{tr_no}]/td[{td_no}]'.format(tr_no=tr_no, td_no=td_no)
                        self.select_in_5010(field, td_xpath)
                        continue
                    td_xpath = local_template[field_key][1].format(tr_no=str(tr_no))
                    td_xpath = table_xpath + td_xpath[1:]
                    self.helper.judge_and_fill(str(field), td_xpath)
                    time.sleep(1)

    # 进行5010减免税的下拉框选择
    def select_in_5010(self, field, td_xpath):
        # 该单元格是否有select元素
        if not self.helper.is_exists_select(td_xpath):
            return False
        # 点击，让options出现
        self.driver.find_element_by_xpath(td_xpath).click()
        # 进行select选择
        res_bool, res_message = self.helper.select_reduction_code(field, td_xpath + '/select/option', )
        if res_bool is False:
            raise Exception(res_message)
        return True

    '''''''''''''''''''''''''''''''''''''''''
    '               获取数据
    '''''''''''''''''''''''''''''''''''''''''
    def run_for_init(self, data):
        # 步骤四：填写数据
        time.sleep(3)
        self.logger.to_log('info', '步骤四开始')

        self.helper.confirm()

        local = ShanxiTable.get_local_added_small()
        left_a = {
            '5004': '《增值税纳税申报表（适用小规模纳税人）》',
            '5005': '《增值税纳税申报表（适用于增值税小规模纳税人）附列资料》',
            '5010': '《增值税减免税申报明细表》'
        }
        left_a = self.helper.reverse_dict(left_a)
        # 只取可以填的表格
        all_table_in_page = self.helper.get_left_table()
        all_table_in_data = data.keys()
        left_a_new = dict()
        for table_key in left_a:
            if table_key in all_table_in_data and left_a[table_key] in all_table_in_page:
                left_a_new[table_key] = left_a[table_key]
        self.driver.switch_to.default_content()
        for key, val in left_a_new.items():
            time.sleep(2)
            self.driver.switch_to.frame('frmMain')
            self.driver.find_element_by_link_text(val).click()
            time.sleep(2)
            self.driver.switch_to.frame('frmSheet')
            if key == '5010':
                self.fill_into_5010(data[key], local[key], val)
            else:
                self.helper.get_with_three_loop(local[key], key, self.table_xpath, val)
            self.driver.switch_to.default_content()

        self.logger.to_log('info', '步骤四结束')
        time.sleep(5)

    def get_init_data_5010(self):
        pass

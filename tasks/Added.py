"""
Added
增值税报表=》一般纳税人
表ID：5001、5002、5003、5006、5007、5008、5009、5010
"""
import time

from common.General import General
from common.Logger import Logger
from config import ShanxiTable

from common.Container import Container
from custom.Helper import Helper
from custom.Step import Step


class Added(object):

    def __init__(self):
        self.step = Step()
        self.helper = Helper()
        self.logger = Logger()
        self.general = General()
        self.driver = Container.DRIVER
        self.table_xpath = '//*[@id="viewCtrlId"]/div[3]/table[2]/tbody'  # 普通表的xpath
        self.table_5009_xpath = '//div[@class="NewTableMain"]/table/tbody'  # 营改增表格的xpath

    # 5009营改增，select字段和td的映射关系
    select_td_map_5009 = {
        'project': 1,
        'incrementTax': 5,
        'businessTax': 6,
    }
    # 5010减免税，select字段与td的映射关系
    select_td_map_5010 = {
        'project': 1,
    }

    def run(self):
        self.logger.to_log('info', '增值税报表=》一般纳税人=》added_commonly')
        Container.NOW_TABLE_NAME = table_name = '增值税纳税申报表（一般纳税人适用）'
        data = General.get_api_data()

        result_bool, result_str = self.step.judge_period_and_select_table_step('二')
        if result_bool is True and result_str == Container.TABLE_ALREADY_DECLARE_STR:
            # 已经申报过了
            return True, table_name + '=>' + result_str
        elif result_bool is False:
            return False, table_name + '=>' + result_str

        try:
            # 步骤三，选择一表申报和切换窗口句柄
            self.logger.to_log('info', '步骤三开始')
            self.driver.switch_to.parent_frame()
            yibiaoshenbao_xpath = '//*[@id="layui-layer1"]/div[2]/div/table/tbody/tr[2]/td[2]/button'
            General.wait(xpath=yibiaoshenbao_xpath)
            self.driver.find_element_by_xpath(yibiaoshenbao_xpath).click()
            self.logger.to_log('info', '选择一表申报')
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.logger.to_log('info', '切换窗口句柄')
            self.logger.to_log('info', '步骤三结束')
        except Exception as e:
            General.save_result_img()
            error_message = '步骤三：选择一表申报和切换窗口句柄出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        try:
            time.sleep(5)
            # 步骤四：填写数据
            self.logger.to_log('info', '步骤四开始')
            local = ShanxiTable.get_local_added_commonly()
            left_a = {
                '5001': '《增值税纳税申报表（适用于增值税一般纳税人）》',
                '5002': '《增值税纳税申报表附列资料（表一）（本期销售情况明细）》',
                '5003': '《增值税纳税申报表附列资料（表二）（本期进项税额明细）》',
                '5006': '《增值税纳税申报表附列资料（表三）（服务、不动产和无形资产扣除项目明细）》',
                '5007': '《增值税纳税申报表附列资料（表四）（税额抵减情况表）》',
                '5008': '《增值税纳税申报表附列资料（五）（不动产分期抵扣计算表）》',
                # '5010': '《增值税减免税申报明细表》',
                '5009': '《营改增税负分析测算明细表》',
            }
            left_a = General.reverse_dict(left_a)
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
                self.driver.switch_to.frame('frmSheet')
                if key == '5009':
                    self.fill_into_5009(data[key]['secondTable'], local[key], val)
                elif key == '5010':
                    # todo 一般纳税人的减免税表有问题，待配中
                    pass
                else:
                    General.fill_with_three_loop(data[key], local[key], self.table_xpath, val)
                self.driver.switch_to.default_content()

            self.logger.to_log('info', '步骤四结束')

        except Exception as e:
            General.save_result_img()
            error_message = '步骤四：填写数据出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        result_bool, result_str = self.step.to_declare_step('五')

        if result_bool is False:
            return result_bool, table_name + '=>' + result_str
        else:
            return True, table_name + '=>报税成功'

    '''''''''''''''''''''''''''''''''''''''''''''''''''''
    '                   5009营改增表
    '''''''''''''''''''''''''''''''''''''''''''''''''''''

    # 营改增，表ID：5009
    def fill_into_5009(self, data, local, table_name):
        self.logger.to_log('info', '等待' + table_name + '表格初始化')
        time.sleep(5)
        start_line = 6
        dict_key = 0
        total_line = self.get_total_line_5009()
        data_type_list = General.dict_to_list(data)
        if not data_type_list:
            return
        all_line = start_line + len(data_type_list)
        trs = dict()
        while start_line < all_line:
            # 和其他表不一样，这里是{栏次序号：对应的tr_no}
            trs.update({dict_key: start_line})
            start_line += 1
            dict_key += 1
            self.add_row(start_line, total_line)

        # 开始填写表格
        # 返回的是个list，而不是dict
        local_template = local['template']
        for hurdles, tr_no in trs.items():
            data_line = data_type_list[hurdles]
            for field_key, field in data_line.items():
                if field_key in local_template and (local_template[field_key][0] == ShanxiTable.FORM_FILL):
                    # 是select单元格
                    if field_key in self.select_td_map_5009 and field != '':
                        self.select_in_5009(field_key, field, tr_no)
                        continue
                    td_xpath = local_template[field_key][1].format(tr_no=str(tr_no))
                    General.judge_and_fill(str(field), self.table_5009_xpath + td_xpath)
                    self.continue_save()

    # 添加新行，适用于5009表
    def add_row(self, start_line, total_line):
        if start_line > total_line:
            add_button_xpath = '//*[@id="ysxxListId"]/tbody/tr[6]/td[21]/div/a'
            add_button_element = self.driver.find_element_by_xpath(add_button_xpath)
            self.driver.execute_script("$(arguments[0]).focus()", add_button_element)
            add_button_element.click()

    # 获取所有行，适用于5009营改增表
    def get_total_line_5009(self):
        xpath = self.table_5009_xpath
        return len(self.driver.find_elements_by_xpath(xpath + '/tr'))

    # 选择下拉框，5009营改增表
    def select_in_5009(self, field_key, code, tr_no):
        # 拼接xpath
        td_no = self.select_td_map_5009[field_key]
        td_xpath = self.table_5009_xpath + '/tr[{tr_no}]/td[{td_no}]'.format(tr_no=tr_no, td_no=td_no)
        # 该单元格是否有select元素
        if not General.is_exists_select(td_xpath):
            return False
        # 进行select选择
        if td_no == 5 and code == '':
            raise Exception('增值税税率或征收率不能为空')
        self.click_select_in_5009(td_xpath, td_no)
        res_bool, res_message = self.helper.select_reduction_code(code, td_xpath + '/select/option', td_no=td_no)
        if res_bool is False:
            raise Exception(res_message)
        return True

    # 首先点击select，5009增值税表
    def click_select_in_5009(self, xpath, td_no):
        if td_no == 5 or td_no == 6:
            self.driver.find_element_by_xpath(xpath + '/select').click()
        else:
            self.driver.find_element_by_xpath(xpath).click()

    # 出现弹框时继续保存，适用于5009
    def continue_save(self):
        try:
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            self.driver.find_element_by_class_name('layui-layer-dialog')
            self.driver.find_element_by_link_text('继续保存').click()
            self.driver.switch_to.frame('frmSheet')
        except:
            self.driver.switch_to.frame('frmSheet')
            pass

    '''''''''''''''''''''''''''''''''''''''''''''''''''''
    '                   5010减免税表
    '''''''''''''''''''''''''''''''''''''''''''''''''''''

    # 增值税（一般纳税人）减免税申报明细表（这里实际上是两张表）
    def fill_into_added_decrement(self, api_data, local, element_tables, table_name):
        self.logger.to_log('info', '等待' + table_name + '表格初始化')
        time.sleep(5)
        try:
            for index in range(2):
                if index == 0:
                    local_template = local['secondTable']
                    start_line = 5
                    table_xpath = '//*[@id="viewCtrlId"]/div[3]/table[1]/tbody'
                    add_button_xpath = table_xpath + '/tr[5]/td[8]/div/a'
                    data_type_list = General.dict_to_list(api_data['secondTable'])
                else:
                    local_template = local['fourthTable']
                    start_line = 8
                    table_xpath = '//*[@id="viewCtrlId"]/div[3]/table[2]/tbody'
                    add_button_xpath = table_xpath + '/tr[8]/td[8]/div/a'
                    data_type_list = General.dict_to_list(api_data['fourthTable'])
                if not data_type_list:
                    return
                self.fill_into_5010(index, start_line, local_template, data_type_list, table_xpath, add_button_xpath)
                time.sleep(2)
        except Exception as e:
            raise Exception(table_name + ' 数据填充错误=>' + str(e))

    # 填写5010的两张表
    def fill_into_5010(self, index, start_line, local_template, api_data, table_xpath, add_button_xpath):
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
                    General.judge_and_fill(str(field), td_xpath)
                    time.sleep(1)

    # 进行5010减免税的下拉框选择
    def select_in_5010(self, field, td_xpath):
        # 该单元格是否有select元素
        if not General.is_exists_select(td_xpath):
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
    def run_for_init(self):
        time.sleep(5)
        # 步骤四：填写数据
        self.logger.to_log('info', '步骤四开始')
        local = ShanxiTable.get_local_added_commonly()
        left_a = {
            '5001': '《增值税纳税申报表（适用于增值税一般纳税人）》',
            '5002': '《增值税纳税申报表附列资料（表一）（本期销售情况明细）》',
            '5003': '《增值税纳税申报表附列资料（表二）（本期进项税额明细）》',
            '5006': '《增值税纳税申报表附列资料（表三）（服务、不动产和无形资产扣除项目明细）》',
            '5007': '《增值税纳税申报表附列资料（表四）（税额抵减情况表）》',
            '5008': '《增值税纳税申报表附列资料（五）（不动产分期抵扣计算表）》',
            # '5010': '《增值税减免税申报明细表》',
            '5009': '《营改增税负分析测算明细表》',
        }
        left_a = General.reverse_dict(left_a)
        self.driver.switch_to.default_content()
        for key, val in left_a.items():
            time.sleep(2)
            self.driver.switch_to.frame('frmMain')
            self.driver.find_element_by_link_text(val).click()
            self.driver.switch_to.frame('frmSheet')
            if key == '5009':
                self.fill_into_5009(local[key], val)
            elif key == '5010':
                # todo 一般纳税人的减免税表有问题，待配中
                pass
            else:
                self.helper.get_with_three_loop(local[key], key, self.table_xpath, val)
            self.driver.switch_to.default_content()

        self.logger.to_log('info', '步骤四结束')
        pass


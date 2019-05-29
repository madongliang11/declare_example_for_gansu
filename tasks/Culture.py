"""
Culture
文化事业建设费申报表
表ID：10001、10002
"""
import time

from selenium.webdriver.support.select import Select

from app import Constant
from app.config import ShanxiTable
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class Culture(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = ''
        self.table_10001_xpath = '//div[@class="NewTableMain"]/table/tbody'
        self.table_10002_xpath = '//div[@class="NewTableMain"]/table/tbody'
        self.select_td_map = {'proofType': 5}

    def run(self):
        self.logger.to_log('info', '文化事业建设费申报表=》culture_table')
        dr = self.driver
        self.info['table_name'] = '文化事业建设费申报表（营改增）'
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
            self.logger.to_log('info', '步骤四开始')
            time.sleep(5)
            local = ShanxiTable.culture_table()
            left_a = {
                '10001': '《文化事业建设费申报表》（营改增）',
                '10002': '应税服务扣除项目清单',
            }
            left_a = self.helper.reverse_dict(left_a)
            # 只取可以填的表格
            all_table_in_page = self.helper.get_left_table()
            all_table_in_data = data.keys()
            dr.switch_to.default_content()
            # if '10001' in all_table_in_data and left_a['10001'] in all_table_in_page:
            #     self.table_10001(data['10001'], local['10001'], left_a['10001'])
            if '10002' in all_table_in_data and left_a['10002'] in all_table_in_page:
                self.table_10002(data['10002'], local['10002'], left_a['10002'])
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤四：进入选表页面出错'
            self.logger.to_log('info', error_message + '=>' + repr(e))
            return False, self.info['table_name'] + '=>' + error_message

        result_bool, result_str = self.step.to_declare_step('五')

        if result_bool is False:
            return result_bool, self.info['table_name'] + '=>' + result_str
        else:
            return True, self.info['table_name'] + '=>报税成功'

    # 填写10001表
    def table_10001(self, api_data, local, table_name):
        self.driver.switch_to.frame('frmMain')
        self.driver.switch_to.frame('frmSheet')
        self.helper.fill_with_three_loop(api_data, local, self.table_10001_xpath, table_name)
        self.driver.find_element_by_xpath(self.table_10001_xpath + '/tr[21]/td[2]/div[3]/input').click()
        self.driver.switch_to.default_content()

    # 填写10002表
    def table_10002(self, api_data, local, table_name):
        self.driver.switch_to.frame('frmMain')
        self.driver.find_element_by_link_text(table_name).click()
        self.logger.to_log('info', '进入' + table_name)
        self.driver.switch_to.frame('frmSheet')
        time.sleep(2)
        start_line = 5
        data_10002 = self.helper.dict_to_list(api_data['firstTable'])
        if not data_10002:
            return
        # data_10002.pop(len(data_10002) - 1)
        total_line = len(data_10002)
        local_template = local['template']
        index = 1
        while index < total_line:
            for i, row in enumerate(data_10002):
                for field_key, field in local_template.items():
                    if field[0] == ShanxiTable.FORM_FILL:
                        if self.select_in_10002(field_key, field, start_line, row) is False:
                            continue
                        self.fill_in_10002(local_template, field_key, row, start_line)
                    time.sleep(1)
                start_line += 1
                index += 1

    # 在10002表中进行select选择
    def select_in_10002(self, field_key, field, start_line, row):
        td_xpath = self.table_10002_xpath + field[1].format(tr_no=start_line)[0:-7]
        # 是select单元格
        if field_key in self.select_td_map and field != '':
            # 该单元格是否有select元素
            if not self.helper.is_exists_select(td_xpath):
                return False
            # 进行select选择
            try:
                xpath = self.table_10001_xpath + field[1].format(tr_no=start_line)
                select_element = self.driver.find_element_by_xpath(xpath)
                Select(select_element).select_by_visible_text(row[field_key])
            except:
                raise Exception('选择凭证种类错误')
        return True

    # 在10002表中填充数据
    def fill_in_10002(self, local_template, field_key, row, start_line):
        td_xpath = local_template[field_key][1].format(tr_no=str(start_line))
        try:
            self.driver.find_element_by_xpath(self.table_10002_xpath + td_xpath)
        except:
            self.add_row()
        self.helper.fill_in(str(row[field_key]), self.table_10002_xpath + td_xpath)

    # 点击添加行数按钮
    def add_row(self):
        xpath = self.table_10002_xpath + '/tr[5]/td[8]/div/a'
        self.driver.find_element_by_xpath(xpath).click()

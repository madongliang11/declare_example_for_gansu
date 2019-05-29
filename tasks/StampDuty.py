"""
StampDuty
其他报表=》印花税
表ID：7001
"""
import time

from app import Constant
from app.config import ShanxiTable
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class StampDuty(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = '//*[@id="viewCtrlId"]/div[2]/table/tbody'

    def run(self):
        self.logger.to_log('info', '其他报表=》印花税报表=》stamp_duty_table')
        dr = self.driver
        self.info['table_name'] = '印花税申报'
        data = self.data['7001']

        result_bool, result_str = self.step.select_other_table_step('二')
        if result_bool is False:
            return result_bool, self.info['table_name'] + '=>' + result_str

        result_bool, result_str = self.step.change_window_handle_step('三')
        if result_bool is False:
            return False, self.info['table_name'] + '=>' + result_str

        try:
            time.sleep(2)
            self.driver.find_element_by_link_text('下一步').click()
        except:
            pass

        try:
            # 步骤四，获取印花税待填项目
            self.logger.to_log('info', '步骤四开始')
            time.sleep(3)
            self.confirm()

            dr.switch_to.frame('frmMain')
            dr.switch_to.frame('frmSheet')
            xpath = self.table_xpath + '/tr[{num}]'
            start_line = 8
            trs = dict()
            while start_line:
                xpath_for_line = xpath.format(num=str(start_line))
                tr = dr.find_element_by_xpath(xpath_for_line)
                default_value = tr.get_attribute('default-value')
                if default_value is None:
                    break
                value = dr.find_element_by_xpath(xpath_for_line + '/td[2]/input').get_attribute('value')
                trs.update({value: start_line})
                start_line += 1
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤四：获取印花税待填项目错误'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        try:
            self.logger.to_log('info', '步骤五开始')
            select_id_num = 0
            if not data.get('secondTable', None):
                raise Exception('申报数据为空')
            self.click_yesno(data['policy']['oneRow']['isConformPolicy'])
            data = self.retry_set_api_data(data['secondTable'])
            local_template = ShanxiTable.get_stamp_duty_table()['template']
            for project_name, tr_no in trs.items():
                if project_name not in data:
                    data.pop(project_name)
                    continue
                data_line = data[project_name]
                for field_key, field in data_line.items():
                    if field_key in local_template and local_template[field_key][0] == ShanxiTable.FORM_FILL:
                        td_xpath = local_template[field_key][1].format(tr_no=str(tr_no))
                        if field_key == 'reliefPropertyCode':
                            self.select_in_7001(field_key, field, td_xpath)
                            continue
                        self.helper.judge_and_fill(field, self.table_xpath + td_xpath)
                        time.sleep(1)
                select_id_num += 1

            time.sleep(5)
            self.logger.to_log('info', '步骤五结束')
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤五：填写数据出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        result_bool, result_str = self.step.to_declare_step('六')

        if result_bool is False:
            return result_bool, self.info['table_name'] + '=>' + result_str
        else:
            return True, self.info['table_name'] + '=>报税成功'

    # 将数组重组成以project为key的字典
    @staticmethod
    def retry_set_api_data(data):
        field_key = 'project'
        new_data = dict()
        for row_key, row in data.items():
            new_data[row[field_key]] = row
        return new_data

    def select_in_7001(self, field_key, code, td_xpath):
        if field_key == 'reliefPropertyCode' and code != '':
            self.driver.find_element_by_xpath(td_xpath).click()
            res_bool, res_message = self.helper.select_reduction_code(code, td_xpath + '/select/option')
            if res_bool is False:
                raise Exception(res_message)
        return True

    # 在select中选择减免代码
    def to_do_select(self, select_id, code):
        is_error = 0
        is_exists = 0
        select_element = self.driver.find_element_by_id(select_id)
        select_element.click()
        time.sleep(3)
        options = self.driver.find_element_by_id(select_id).find_elements_by_tag_name('option')
        for option in options:
            if option.text == code:
                option.click()
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
            return False, '您选择的减免性质没有进行税收减免优惠备案'
        elif is_exists == 0:
            return False, '没有您的减免代码'
        else:
            return True, 'success'

    def click_yesno(self, value):
        if int(value) is 0:
            value = '否'
        else:
            value = '是'
        xpath = '//*[@id="viewCtrlId"]/div[2]/table/tbody/tr[5]/td[2]/input'
        self.helper.click_radio_yesno(xpath, value)
        self.confirm()

    def confirm(self):
        self.helper.wait_to_frame('frmMain')
        try:
            self.driver.find_element_by_class_name('layui-layer-btn0').click()
        except:
            pass
        self.driver.switch_to.default_content()

"""
Additional
附加税（费）纳税申报表
表ID：6001
"""
import time

from app import Constant
from app.config import ShanxiTable
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class Additional(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = '//div[@class="NewTableMain"]/table/tbody'

    def run(self):
        self.logger.to_log('info', '附加税（费）纳税申报表=》附加税（费）纳税申报表=》additional_table')
        dr = self.driver
        self.info['table_name'] = '附加税（费）纳税申报表'
        data = self.data['6001']

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
            time.sleep(2)
            self.driver.find_element_by_class_name('layui-layer-close').click()
        except:
            pass

        try:
            # 获取待填项目
            self.logger.to_log('info', '步骤四开始')
            dr.switch_to.frame('frmMain')
            dr.switch_to.frame('frmSheet')
            start_line = 8
            trs = dict()
            while start_line:
                xpath_for_line = self.table_xpath + '/tr[{num}]'.format(num=str(start_line))
                tr = self.driver.find_element_by_xpath(xpath_for_line)
                default_value = tr.get_attribute('default-value')
                if default_value is None:
                    break
                value = self.driver.find_element_by_xpath(xpath_for_line + '/td[2]/input').get_attribute('value')
                trs.update({value: start_line})
                start_line += 1
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤四：获取待填项目错误'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        try:
            self.logger.to_log('info', '步骤五开始')
            time.sleep(1)
            select_num = 0
            self.click_yesno(data['policy']['oneRow']['isConformPolicy'])
            data = self.retry_set_api_data(data['firstTable'])
            local_template = ShanxiTable.get_additional_table()['template']
            for project_name, tr_no in trs.items():
                if project_name not in data:
                    data.pop(project_name)
                    continue
                select_num += 1
                data_line = data[project_name]
                for field_key, field in data_line.items():
                    if field_key in local_template and (local_template[field_key][0] == ShanxiTable.FORM_FILL):
                        td_xpath = self.table_xpath + local_template[field_key][1].format(tr_no=tr_no)[0:-7]
                        self.select_in_6001(field_key, field, td_xpath)
                        # 附加税 不需要填写其他东西，只需要选择减免代码
                        time.sleep(1)
            time.sleep(5)
            self.logger.to_log('info', '步骤五结束')
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤五：填写数据出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        result_bool, result_str = self.step.to_declare_step('五')

        # 不管成功失败，先回到原先的页面去
        # self.helper.return_first_window()

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

    # 在6001中选择下拉框
    def select_in_6001(self, field_key, code, td_xpath):
        if (field_key == 'reliefPropertyCode' or field_key == 'reductionCode') and code != '':
            # 先点击，使select出现
            self.driver.find_element_by_xpath(td_xpath).click()
            res_bool, res_message = self.helper.select_reduction_code(code, td_xpath + '/select/option')
            if res_bool is False:
                raise Exception(res_message)
        return True

    def click_yesno(self, value):
        if int(value) is 0:
            value = '否'
        else:
            value = '是'
        xpath = '//*[@id="viewCtrlId"]/div[3]/table/tbody/tr[4]/td[7]/input'
        self.helper.click_radio_yesno(xpath, value)
        self.confirm()

    def confirm(self):
        self.helper.wait_to_frame('frmMain')
        try:
            self.driver.find_element_by_class_name('layui-layer-btn0').click()
        except:
            pass
        self.driver.switch_to.default_content()

    def run_for_yulei(self):
        """
        爬取表格html
        :return:
        """
        file_path = 'C:\\Users\\Administrator\\Desktop\\html\\tmp\\additional.html'
        time.sleep(5)
        self.driver.switch_to.frame('frmMain')
        self.driver.switch_to.frame('frmSheet')
        table_element = self.driver.find_element_by_xpath('//div[@class="NewTableMain"]/table')
        tds = table_element.find_elements_by_tag_name('td')
        js = 'window.ViewEngine.SCOPE.formData.'
        for td in tds:
            try:
                input_element = td.find_element_by_tag_name('input')
                jpath = input_element.get_attribute('jpath')
                if jpath is not None:
                    value = str(self.driver.execute_script('return ' + js + jpath))
                    self.driver.execute_script(
                        'arguments[0].setAttribute("value",{})'.format('\"' + value + '\"'),
                        input_element)
            except:
                pass
        html = str(self.driver.find_element_by_xpath('//div[@class="NewTableMain"]/table').get_attribute("outerHTML"))
        with open(file_path, 'w') as f:
            f.write(html)
        exit(0)

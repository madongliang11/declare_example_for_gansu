import re
import time

from selenium.webdriver.support.select import Select

from app import Constant
from app.config import ShanxiTable
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class GeneralDeclare(Base):
    def __init__(self, data, local, item_name):
        super(GeneralDeclare, self).__init__()
        self.general_data = data
        self.general_local = local
        self.item_name = item_name
        self.now_tr_no = None
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = '//*[@id="viewCtrlId"]/div[3]/table/tbody'

    def run(self):
        """
        填充数据
        :return:
        """
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
            # 步骤四，寻找tr_no顺序
            self.logger.to_log('info', '步骤四开始')
            time.sleep(10)
            self.confirm()
            self.driver.switch_to.frame('frmMain')
            self.driver.switch_to.frame('frmSheet')
            xpath = '//*[@id="viewCtrlId"]/div[3]/table/tbody/tr'
            start_len = 2
            tr_len = len(self.driver.find_elements_by_xpath(xpath))
            xpath += '[{tr_no}]/td[3]/input'
            while start_len < tr_len:
                item_name = self.driver.find_element_by_xpath(xpath.format(tr_no=start_len)).get_attribute('value')
                if item_name == self.item_name:
                    self.now_tr_no = start_len
                    break
                start_len += 1
            if self.now_tr_no is None:
                raise Exception(self.item_name + '不存在')
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤四：寻找征收品目出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        try:
            # 步骤五，填写数据
            self.logger.to_log('info', '步骤五开始')

            # 点击复选框
            check_xpath = self.table_xpath + '/tr[{tr_no}]/td/input'.format(tr_no=self.now_tr_no)
            if self.driver.find_element_by_xpath(check_xpath).is_selected() is False:
                self.driver.find_element_by_xpath(check_xpath).click()
            time.sleep(1)
            self.fill_with_general(self.general_data['firstTable'], self.general_local, self.table_xpath,
                                   self.info['table_name'])
            self.logger.to_log('info', '步骤五结束')
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤五：填写数据出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        try:
            # 步骤六，填写证件信息
            self.logger.to_log('info', '步骤五开始')
            time.sleep(2)
            tax_number = self.driver.find_element_by_xpath('//*[@id="viewCtrlId"]/div[2]/table/tbody/tr[1]/td[2]/span').text
            select_element = self.driver.find_element_by_xpath('//*[@id="viewCtrlId"]/div[4]/table/tbody/tr[1]/td[2]/select')
            Select(select_element).select_by_visible_text('101|组织机构代码证')
            input_element = self.driver.find_element_by_xpath('//*[@id="viewCtrlId"]/div[4]/table/tbody/tr[1]/td[3]/input')
            input_element.send_keys(tax_number)
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤六：填写证件信息出错'
            self.logger.to_log('error', error_message + '=>' + str(e))
            return False, error_message

        result_bool, result_str = self.step.to_declare_step('五')

        if result_bool is False:
            return result_bool, self.info['table_name'] + '=>' + result_str
        else:
            return True, self.info['table_name'] + '=>报税成功'

    def confirm(self):
        try:
            self.driver.find_element_by_class_name('layui-layer-btn0').click()
        except:
            pass

    # 向表格中填充数据，适用于通用申报表
    def fill_with_general(self, api_data, local, xpath, table_name):
        self.logger.to_log('info', '等待' + table_name + '表格初始化')
        time.sleep(5)
        try:
            for row_key, row in local.items():
                for field_key, field in row.items():
                    # self.logger.to_log('info', row_key + '=>' + field_key + '=>' + field[1])
                    if field[0] == ShanxiTable.FORM_FILL:
                        value = api_data[row_key][field_key]
                        td_xpath = field[1].replace('tr[2]', 'tr[{}]'.format(self.now_tr_no))
                        # 减免代码-其他操作
                        if field_key == 'reliefPropertyCode' or field_key == 'reductionProperties':
                            td_xpath = xpath + td_xpath[0:-7]  # 去掉最后的/select
                            self.select_for_general(value, td_xpath)
                            continue
                        self.helper.judge_and_fill(value, xpath + field[1])
                        time.sleep(1)
        except Exception as e:
            raise Exception(table_name + ' 数据填充错误=>' + str(e))

    def select_for_general(self, field, td_xpath):
        if not field:
            return False
        # 该单元格是否有select元素
        if not self.helper.is_exists_select(td_xpath):
            return False
        # 点击使select出现
        # xpath = '//div[@class="NewTableMain"]/table/tbody/tr[2]/td[14]'
        self.driver.find_element_by_xpath(td_xpath).click()
        # 进行select选择
        res_bool, res_message = self.helper.select_reduction_code(field, td_xpath + '/select/option')
        if res_bool is False:
            raise Exception(res_message)
        return True

    def run_for_yulei(self):
        """
        爬取表格html
        :return:
        """
        file_path = 'C:\\Users\\Administrator\\Desktop\\html\\tmp\\9001.html'
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

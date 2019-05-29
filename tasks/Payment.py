"""
Payment
缴款任务
流程：
1.在“缴款查询及打印”界面中寻找是否有该税种
2.有的话就返回缴款成功
3.没有的话就去缴款页面
4.缴款页面有没有第三方协议
5.有的话就缴款
6.没有的话就缴款失败
"""
import time

from app import Constant
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class Payment(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.js = "return document.querySelectorAll('#qjskDataGird table tr')[{tr_no}].querySelectorAll('{th_or_td}')[{td_no}]"

    def run(self):
        self.logger.to_log('info', '缴款')
        table_name = Constant.DECLARE_MAP[int(self.info['type'])]['table_name']
        try:
            # 步骤二，进入缴款查询及打印页面，查询是否有该税种
            self.logger.to_log('info', '步骤二开始')
            if self.tax_in_page(table_name) is True:
                return True, '缴费完成'
            self.driver.switch_to.default_content()
            self.logger.to_log('info', '不在该页面中，准备去缴费')
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤二：查看是否已经缴款出错'
            self.logger.to_log('error', error_message + '=>' + repr(e))
            return False, error_message

        try:
            # 步骤三，进入缴款页面
            self.logger.to_log('info', '步骤三开始')
            result_bool, result_str = self.to_pay(table_name)
            if result_bool is False:
                time.sleep(2)
                self.helper.save_result_img()
            return result_bool, result_str
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤三：缴款步骤出错'
            self.logger.to_log('error', error_message + '=>' + repr(e))
            return False, error_message

    def tax_in_page(self, table_name):
        """
        判断某个税种是否在缴款页面
        True 在
        False 不在
        :return:
        """
        self.driver.switch_to.default_content()
        self.helper.click_left_menu(4)
        time.sleep(2)
        self.helper.click_left_menu(4, 2)
        self.helper.wait_to_frame('ifrMain')
        button_xpath = '//div[@class="searchCriteria"]/div/div[2]/button[1]'
        self.helper.wait(xpath=button_xpath)
        self.driver.find_element_by_xpath(button_xpath).click()
        time.sleep(1)
        try:
            self.driver.find_element_by_link_text('关闭').click()
            return False
        except:
            pass
        time.sleep(2)

        js = "return document.querySelectorAll('.searchTable table tr')"
        tr_num = len(self.driver.execute_script(js))
        js += "[{tr_no}].querySelectorAll('td')[{td_no}]"
        for i in range(tr_num):
            if i == 0:
                continue
            project = self.driver.execute_script(js.format(tr_no=i, td_no=3)).text
            if table_name.find(project) > 0:
                return True
            if project.find(table_name) > 0:
                return True
        return False

    def to_pay(self, table_name):
        """
        具体的缴款操作
        :param table_name:
        :return:
        """
        self.helper.click_left_menu(2)
        time.sleep(2)
        self.helper.click_left_menu(2, 2)
        self.helper.wait_to_frame('ifrMain')
        time.sleep(2)
        # 如果缴款金额为0，直接返回不需要缴款
        tax_price = self.driver.find_element_by_id('hjAll').text
        if float(tax_price) == 0:
            error_message = '缴款金额为0'
            self.logger.to_log('info', error_message)
            return True, error_message
        # 首先关闭全部选择
        self.driver.execute_script(self.js.format(tr_no=0, th_or_td='th', td_no=0)).click()
        # 获取全部条目的缴款信息
        js = self.js.format(th_or_td='td')
        tr_num = len(self.driver.execute_script(js[0:58]))
        table_map = dict()
        for i in range(tr_num):
            if i == 0:
                continue
            tax_name = self.driver.execute_script(js.format(tr_no=i, td_no=4)).text
            table_map.update({tax_name: i})
        # 表行为0，返回false
        if len(table_map) < 1:
            error_message = '没有缴款条目'
            self.logger.to_log('info', error_message)
            return False, error_message
        if table_name in table_map:
            self.driver.execute_script(js.format(tr_no=table_map[table_name], td_no=0)).click()
            time.sleep(1)
        else:
            # 不在该字典中
            error_message = '条目中没有{}'.format(table_name)
            self.logger.to_log('info', error_message)
            return False, error_message
        # 查看是否有第三方协议，没有的话截图返回False
        try:
            self.driver.find_element_by_id('sfxyjk').click()
        except:
            error_message = '没有第三方协议'
            self.logger.to_log('info', error_message)
            return False, error_message
        # 点击立即缴款，点击失败返回False
        try:
            # self.driver.find_element_by_link_text('立即缴款').click()
            self.driver.find_element_by_id('a_main_ljjk').click()
        except:
            error_message = '无法点击缴款按钮'
            self.logger.to_log('info', error_message)
            return False, error_message
        # 点击弹出框的缴款按钮
        # self.driver.find_element_by_id('a_way_ds_sfxy').click()
        button_a_array = self.driver.find_elements_by_css_selector('div#pay_moda>div#model_btn>a')
        for button in button_a_array:
            if button.value_of_css_property('display') != 'none':
                button.click()
        time.sleep(5)
        # 获取焦点，滚动条到最下方
        result_table = self.driver.find_element_by_id('pay_result_ds_grid')
        self.helper.in_focus(result_table)
        # 检查是否有成功两个字
        if result_table.text.find('成功') < 0:
            error_message = '缴款失败'
            return False, error_message
        return True, 'success'

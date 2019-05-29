"""
TaxIdentification
税种鉴定任务
"""
import time

from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step
from app.tool.Log import Logger


class TaxIdentification(object):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.base = Base()
        self.logger = Logger()

    def run(self):
        self.logger.to_log('info', '税种鉴定')
        try:
            # 步骤二：进入鉴定页面  我要查询=》申报信息查询=》认定管理查询=》税（费）种认定查询
            home_xpath = '//*[@id="mainContent"]/table/tbody/tr/td[1]/div/div/a'
            self.helper.wait(xpath=home_xpath)
            self.base.driver.find_element_by_xpath(home_xpath).click()

            try:
                time.sleep(1)
                self.base.driver.find_element_by_id('box_close_dyc').click()
            except:
                pass

            self.helper.wait(id='wycxTab')
            self.base.driver.find_element_by_id('wycxTab').click()

            shenbao_xpath = '//*[@id="topTabs"]/div[1]/div[3]/div/div/div[4]/a'
            self.helper.wait(xpath=shenbao_xpath)
            self.base.driver.find_element_by_xpath(shenbao_xpath).click()

            time.sleep(2)
            self.helper.click_left_menu(1, 3)

            self.helper.wait_to_frame('ifrMain')
            self.helper.wait_to_frame('cxtable')

            self.helper.wait(id='queryBtn')
            self.base.driver.find_element_by_id('queryBtn').click()

        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤二：进入鉴定页面失败'
            self.logger.to_log('error', error_message + '=>' + repr(e))
            return False, error_message

        try:
            # 步骤三：获取整个表格信息
            self.get_all_tax()
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤三：获取鉴定信息失败'
            self.logger.to_log('error', error_message + '=>' + repr(e))
            return False, error_message

    def get_all_tax(self, table_info_list=None):
        if table_info_list is None:
            table_info_list = []
        self.helper.wait(class_name='custom_layper_page_info')
        table_xpath = '//*[@id="dataList"]/tbody'
        td_map = {
            'category': 3,
            'project': 4,
        }
        time.sleep(2)
        table_info_list += self.helper.get_table_info_list(table_xpath, td_map)
        for info, index in enumerate(table_info_list):
            print(info)

        try:
            self.base.driver.find_element_by_link_text('下一页').click()
            self.get_all_tax(table_info_list)
        except:
            pass

        print(table_info_list)
        time.sleep(1000)

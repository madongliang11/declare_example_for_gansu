"""
Check
检查任务
按期应申报：
1.“申报期限”属于本年本月的
2.“申报日期”中有值
3.“操作”为已申报
财务报表：
1.“报送期限”属于本年本月的
2.“报送日期”中有值
"""
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class Check(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()
        self.table_xpath = '//div[@class="NewTableMain"]/table[1]/tbody'
        self.js = 'return document.querySelectorAll("#gdslhsb tr")[{tr_no}].querySelectorAll("td")[{td_no}]'
        self.js_finance = 'return document.querySelectorAll("#gdslhsb tr")[{tr_no}].querySelectorAll("td")[{td_no}]'
        self.undeclare = list()
        self.undeclare_count = 0
        self.tax_count = 0

    def run(self):
        self.logger.to_log('info', '检查')
        try:
            # 步骤二：获取所有税种信息
            self.logger.to_log('info', '步骤二开始')
            self.helper.wait_to_frame('ifrMain')
            table_map = self.helper.get_all_table(self.js)
            table_map_finance = self.helper.get_all_table_finance()
            self.tax_count = len(table_map) + len(table_map_finance)
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤二：获取税种信息出错'
            self.logger.to_log('error', error_message + '=>' + repr(e))
            return False, error_message

        try:
            self.logger.to_log('info', '步骤三开始')
            # 当前年月
            month = self.helper.get_now_format_date('%Y-%m')
            self.tax_info(table_map, month)
            self.tax_info(table_map_finance, month)
            # 截图
            self.helper.save_result_img()
            # 全部未申报
            if self.undeclare_count == self.tax_count:
                return False, '全部未申报'
            # 部分未申报
            if len(self.undeclare) > 0:
                return False, ','.join(self.undeclare)
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤三：校验申报信息出错'
            self.logger.to_log('error', error_message + '=>' + repr(e))
            return False, error_message

        # 获取总回执
        result_bool, result_str = self.step.to_check_step('四', [1, 2, 3])
        return result_bool, result_str

    # 获取未申报的信息
    def tax_info(self, table_map, month):
        for name, tax in table_map.items():
            if tax['deadline'][0:7] != month:
                self.tax_count -= 1
                continue
            if tax['declare_date'] != '':
                continue
            if tax['opera'] == '已申报':
                continue
            self.undeclare.append(name)
            self.undeclare_count += 1

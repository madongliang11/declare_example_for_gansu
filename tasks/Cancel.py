"""
Cancel
申报作废
"""
from app import Constant
from app.declare.Base import Base
from app.declare.Helper import Helper
from app.declare.Step import Step


class Cancel(Base):

    def __init__(self):
        super().__init__()
        self.helper = Helper()
        self.step = Step()

    def run(self):
        self.logger.to_log('info', '作废')
        table_name = Constant.DECLARE_MAP[int(self.info['type'])]['table_name']
        # 步骤一在
        try:
            # 步骤二，进入缴款查询及打印页面，查询是否有该税种
            self.logger.to_log('info', '步骤二开始')
            if self.tax_in_page(table_name) is True:
                return True, '缴费完成'
            self.driver.switch_to.default_content()
            self.logger.to_log('info', '不在该页面中，准备去缴费')
        except Exception as e:
            self.helper.save_result_img()
            error_message = '步骤二：作废失败'
            self.logger.to_log('error', error_message + '=>' + repr(e))
            return False, error_message

    @staticmethod
    def get_tax_name(tax_type):
        tax_map = {
            1: '增值税',
            2: '企业会计准则',
            3: '附加税',
            4: '印花税',
            5: '通用申报表',
            6: '企业所得税',
            7: '企业所得税',
            8: '通用申报表',
            9: '通用申报表',
            10: '文化事业',
            11: '增值税',
            12: '小企业会计准则',
        }
        return tax_map.get(tax_type, '')


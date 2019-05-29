"""
DisabledWork
通用申报表=》残疾人就业保障金
表ID：11001
"""
from app.config import ShanxiTable
from app.declare.Base import Base
from app.task.GeneralDeclare import GeneralDeclare


class DisabledWork(Base):

    def __init__(self):
        super().__init__()

    def run(self):
        self.logger.to_log('info', '通用申报表=》残疾人就业保障金=》DisabledWork')
        self.info['table_name'] = '通用申报表-残疾人就业保障金'
        item_name = '残疾人就业保障金'
        data = self.data['9001']
        local = ShanxiTable.get_disabled_worker_table()
        return GeneralDeclare(data, local, item_name).run()

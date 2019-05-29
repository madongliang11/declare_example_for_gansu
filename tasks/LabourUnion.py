from app.config import ShanxiTable
from app.declare.Base import Base
from app.task.GeneralDeclare import GeneralDeclare


class LabourUnion(Base):

    def __init__(self):
        super().__init__()

    def run(self):
        self.logger.to_log('info', '通用申报表=》工会经费=》LabourUnion')
        self.info['table_name'] = '通用申报表-工会经费'
        item_name = '工会筹备金'
        data = self.data['12001']
        local = ShanxiTable.get_labour_union_table()
        return GeneralDeclare(data, local, item_name).run()

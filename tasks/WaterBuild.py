"""
WaterBuild
通用申报表=》水利建设基金
表ID：11001
"""
from app.config import ShanxiTable
from app.declare.Base import Base
from app.task.GeneralDeclare import GeneralDeclare


class WaterBuild(Base):

    def __init__(self):
        super().__init__()

    def run(self):
        self.logger.to_log('info', '通用申报表=》水利建设基金=》WaterBuild')
        self.info['table_name'] = '通用申报表-水利建设基金'
        item_name = '地方水利建设基金'
        data = self.data['11001']
        local = ShanxiTable.get_water_build_table()
        return GeneralDeclare(data, local, item_name).run()

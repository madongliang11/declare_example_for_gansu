FORM_FILL = 1  # 向表格中填充
FORM_GET = 2  # 从表格中获取& 在填写时，需要和后端数据对比这个字段标识的数据
FORM_NO = 3  # 不操作
FORM_INIT = 4  # 初始化，在填写时，需要和后端数据对比这个字段标识的数据


# 财务报表 小企业会计准则
def get_local_finance_small():
    return {
        'zichanfuzhaibiao': {
            '10010000': {
                'AssetTotal': (FORM_NO, r'//tr[2]/td[5]'),  # 流动资产
                'AssetInitial': (FORM_NO, r'//tr[2]/td[6]'),  # 流动资产
                'DebtsTotal': (FORM_NO, r'//tr[2]/td[13]'),  # 流动负债
                'DebtsInitial': (FORM_NO, r'//tr[2]/td[14]'),  # 流动负债
            },
            '10010010': {
                'AssetTotal': (FORM_FILL, r'//tr[3]/td[5]/input'),  # 货币资金 期末余额
                'AssetInitial': (FORM_GET, r'//tr[3]/td[6]/input'),  # 货币资金 年初余额
                'DebtsTotal': (FORM_FILL, r'//tr[3]/td[13]/input'),  # 短期借款 期末余额
                'DebtsInitial': (FORM_GET, r'//tr[3]/td[14]/input'),  # 短期借款 年初余额
            },
            '10010020': {
                'AssetTotal': (FORM_FILL, r'//tr[4]/td[5]/input'),  # 短期投资
                'AssetInitial': (FORM_GET, r'//tr[4]/td[6]/input'),  # 短期投资
                'DebtsTotal': (FORM_FILL, r'//tr[4]/td[13]/input'),  # 应付票据
                'DebtsInitial': (FORM_GET, r'//tr[4]/td[14]/input'),  # 应付票据
            },
            '10010030': {
                'AssetTotal': (FORM_FILL, r'//tr[5]/td[5]/input'),  # 应收票据
                'AssetInitial': (FORM_GET, r'//tr[5]/td[6]/input'),  # 应收票据
                'DebtsTotal': (FORM_FILL, r'//tr[5]/td[13]/input'),  # 应付账款
                'DebtsInitial': (FORM_GET, r'//tr[5]/td[14]/input'),  # 应付账款
            },
            '10010040': {
                'AssetTotal': (FORM_FILL, r'//tr[6]/td[5]/input'),  # 应收账款
                'AssetInitial': (FORM_GET, r'//tr[6]/td[6]/input'),  # 应收账款
                'DebtsTotal': (FORM_FILL, r'//tr[6]/td[13]/input'),  # 预收账款
                'DebtsInitial': (FORM_GET, r'//tr[6]/td[14]/input'),  # 预收账款
            },
            '10010050': {
                'AssetTotal': (FORM_FILL, r'//tr[7]/td[5]/input'),  # 预付账款
                'AssetInitial': (FORM_GET, r'//tr[7]/td[6]/input'),  # 预付账款
                'DebtsTotal': (FORM_FILL, r'//tr[7]/td[13]/input'),  # 应付职工薪酬
                'DebtsInitial': (FORM_GET, r'//tr[7]/td[14]/input'),  # 应付职工薪酬
            },
            '10010060': {
                'AssetTotal': (FORM_FILL, r'//tr[8]/td[5]/input'),  # 应收股利
                'AssetInitial': (FORM_GET, r'//tr[8]/td[6]/input'),  # 应收股利
                'DebtsTotal': (FORM_FILL, r'//tr[8]/td[13]/input'),  # 应交税费
                'DebtsInitial': (FORM_GET, r'//tr[8]/td[14]/input'),  # 应交税费
            },
            '10010070': {
                'AssetTotal': (FORM_FILL, r'//tr[9]/td[5]/input'),  # 应收利息
                'AssetInitial': (FORM_GET, r'//tr[9]/td[6]/input'),  # 应收利息
                'DebtsTotal': (FORM_FILL, r'//tr[9]/td[13]/input'),  # 应付利息
                'DebtsInitial': (FORM_GET, r'//tr[9]/td[14]/input'),  # 应付利息
            },
            '10010080': {
                'AssetTotal': (FORM_FILL, r'//tr[10]/td[5]/input'),  # 其他应收款
                'AssetInitial': (FORM_GET, r'//tr[10]/td[6]/input'),  # 其他应收款
                'DebtsTotal': (FORM_FILL, r'//tr[10]/td[13]/input'),  # 应付利润
                'DebtsInitial': (FORM_GET, r'//tr[10]/td[14]/input'),  # 应付利润
            },
            '10010090': {
                'AssetTotal': (FORM_FILL, r'//tr[11]/td[5]/input'),  # 存货
                'AssetInitial': (FORM_GET, r'//tr[11]/td[6]/input'),  # 存货
                'DebtsTotal': (FORM_FILL, r'//tr[11]/td[13]/input'),  # 其他应付款
                'DebtsInitial': (FORM_GET, r'//tr[11]/td[14]/input'),  # 其他应付款
            },
            '10010100': {
                'AssetTotal': (FORM_FILL, r'//tr[12]/td[5]/input'),  # 其中：原材料
                'AssetInitial': (FORM_GET, r'//tr[12]/td[6]/input'),  # 其中：原材料
                'DebtsTotal': (FORM_FILL, r'//tr[12]/td[13]/input'),  # 其他流动负债
                'DebtsInitial': (FORM_GET, r'//tr[12]/td[14]/input'),  # 其他流动负债
            },
            '10010110': {
                'AssetTotal': (FORM_FILL, r'//tr[13]/td[5]/input'),  # 在产品
                'AssetInitial': (FORM_GET, r'//tr[13]/td[6]/input'),  # 在产品
                'DebtsTotal': (FORM_GET, r'//tr[13]/td[13]/input'),  # 流动负债合计
                'DebtsInitial': (FORM_GET, r'//tr[13]/td[14]/input'),  # 流动负债合计
            },
            '10010120': {
                'AssetTotal': (FORM_FILL, r'//tr[14]/td[5]/input'),  # 库存商品
                'AssetInitial': (FORM_GET, r'//tr[14]/td[6]/input'),  # 库存商品
                'DebtsTotal': (FORM_NO, r'//tr[14]/td[13]'),  # 非流动负债
                'DebtsInitial': (FORM_NO, r'//tr[14]/td[14]'),  # 非流动负债
            },
            '10010130': {
                'AssetTotal': (FORM_FILL, r'//tr[15]/td[5]/input'),  # 周转材料
                'AssetInitial': (FORM_GET, r'//tr[15]/td[6]/input'),  # 周转材料
                'DebtsTotal': (FORM_FILL, r'//tr[15]/td[13]/input'),  # 长期借款
                'DebtsInitial': (FORM_GET, r'//tr[15]/td[14]/input'),  # 长期借款
            },
            '10010140': {
                'AssetTotal': (FORM_FILL, r'//tr[16]/td[5]/input'),  # 其他流动资产
                'AssetInitial': (FORM_GET, r'//tr[16]/td[6]/input'),  # 其他流动资产
                'DebtsTotal': (FORM_FILL, r'//tr[16]/td[13]/input'),  # 长期应付款
                'DebtsInitial': (FORM_GET, r'//tr[16]/td[14]/input'),  # 长期应付款
            },
            '10010150': {
                'AssetTotal': (FORM_GET, r'//tr[17]/td[5]/input'),  # 流动资产合计
                'AssetInitial': (FORM_GET, r'//tr[17]/td[6]/input'),  # 流动资产合计
                'DebtsTotal': (FORM_FILL, r'//tr[17]/td[13]/input'),  # 递延收益
                'DebtsInitial': (FORM_GET, r'//tr[17]/td[14]/input'),  # 递延收益
            },
            '10010160': {
                'AssetTotal': (FORM_NO, r'//tr[18]/td[5]'),  # 非流动资产
                'AssetInitial': (FORM_NO, r'//tr[18]/td[6]'),  # 非流动资产
                'DebtsTotal': (FORM_FILL, r'//tr[18]/td[13]/input'),  # 其他非流动负债
                'DebtsInitial': (FORM_GET, r'//tr[18]/td[14]/input'),  # 其他非流动负债
            },
            '10010170': {
                'AssetTotal': (FORM_FILL, r'//tr[19]/td[5]/input'),  # 长期债券投资
                'AssetInitial': (FORM_GET, r'//tr[19]/td[6]/input'),  # 长期债券投资
                'DebtsTotal': (FORM_GET, r'//tr[19]/td[13]/input'),  # 非流动负债合计
                'DebtsInitial': (FORM_GET, r'//tr[19]/td[14]/input'),  # 非流动负债合计
            },
            '10010180': {
                'AssetTotal': (FORM_FILL, r'//tr[20]/td[5]/input'),  # 长期股权投资
                'AssetInitial': (FORM_GET, r'//tr[20]/td[6]/input'),  # 长期股权投资
                'DebtsTotal': (FORM_GET, r'//tr[20]/td[13]/input'),  # 负债合计
                'DebtsInitial': (FORM_GET, r'//tr[20]/td[14]/input'),  # 负债合计
            },
            '10010190': {
                'AssetTotal': (FORM_FILL, r'//tr[21]/td[5]/input'),  # 固定资产原价
                'AssetInitial': (FORM_GET, r'//tr[21]/td[6]/input'),  # 固定资产原价
            },
            '10010200': {
                'AssetTotal': (FORM_FILL, r'//tr[22]/td[5]/input'),  # 减：累计折旧
                'AssetInitial': (FORM_GET, r'//tr[22]/td[6]/input'),  # 减：累计折旧
            },
            '10010210': {
                'AssetTotal': (FORM_GET, r'//tr[23]/td[5]/input'),  # 固定资产账面价值
                'AssetInitial': (FORM_GET, r'//tr[23]/td[6]/input'),  # 固定资产账面价值
            },
            '10010220': {
                'AssetTotal': (FORM_FILL, r'//tr[24]/td[5]/input'),  # 在建工程
                'AssetInitial': (FORM_GET, r'//tr[24]/td[6]/input'),  # 在建工程
            },
            '10010230': {
                'AssetTotal': (FORM_FILL, r'//tr[25]/td[5]/input'),  # 工程物资
                'AssetInitial': (FORM_GET, r'//tr[25]/td[6]/input'),  # 工程物资
            },
            '10010240': {
                'AssetTotal': (FORM_FILL, r'//tr[26]/td[5]/input'),  # 固定资产清理
                'AssetInitial': (FORM_GET, r'//tr[26]/td[6]/input'),  # 固定资产清理
            },
            '10010250': {
                'AssetTotal': (FORM_FILL, r'//tr[27]/td[5]/input'),  # 生产性生物资产
                'AssetInitial': (FORM_GET, r'//tr[27]/td[6]/input'),  # 生产性生物资产
                'DebtsTotal': (FORM_NO, r'//tr[27]/td[13]'),  # 所有者权益（或股东权益）
                'DebtsInitial': (FORM_NO, r'//tr[27]/td[14]'),  # 所有者权益（或股东权益）
            },
            '10010260': {
                'AssetTotal': (FORM_FILL, r'//tr[28]/td[5]/input'),  # 无形资产
                'AssetInitial': (FORM_GET, r'//tr[28]/td[6]/input'),  # 无形资产
                'DebtsTotal': (FORM_FILL, r'//tr[28]/td[13]/input'),  # 实收资本（或股本）
                'DebtsInitial': (FORM_GET, r'//tr[28]/td[14]/input'),  # 实收资本（或股本）
            },
            '10010270': {
                'AssetTotal': (FORM_FILL, r'//tr[29]/td[5]/input'),  # 开发支出
                'AssetInitial': (FORM_GET, r'//tr[29]/td[6]/input'),  # 开发支出
                'DebtsTotal': (FORM_FILL, r'//tr[29]/td[13]/input'),  # 资本公积
                'DebtsInitial': (FORM_GET, r'//tr[29]/td[14]/input'),  # 资本公积
            },
            '10010280': {
                'AssetTotal': (FORM_FILL, r'//tr[30]/td[5]/input'),  # 长期待摊费用
                'AssetInitial': (FORM_GET, r'//tr[30]/td[6]/input'),  # 长期待摊费用
                'DebtsTotal': (FORM_FILL, r'//tr[30]/td[13]/input'),  # 盈余公积
                'DebtsInitial': (FORM_GET, r'//tr[30]/td[14]/input'),  # 盈余公积
            },
            '10010290': {
                'AssetTotal': (FORM_FILL, r'//tr[31]/td[5]/input'),  # 其他非流动资产
                'AssetInitial': (FORM_GET, r'//tr[31]/td[6]/input'),  # 其他非流动资产
                'DebtsTotal': (FORM_FILL, r'//tr[31]/td[13]/input'),  # 未分配利润
                'DebtsInitial': (FORM_GET, r'//tr[31]/td[14]/input'),  # 未分配利润
            },
            '10010300': {
                'AssetTotal': (FORM_GET, r'//tr[32]/td[5]/input'),  # 非流动资产合计
                'AssetInitial': (FORM_GET, r'//tr[32]/td[6]/input'),  # 非流动资产合计
                'DebtsTotal': (FORM_GET, r'//tr[32]/td[13]/input'),  # 所有者权益（或股东权益）合计
                'DebtsInitial': (FORM_GET, r'//tr[32]/td[14]/input'),  # 所有者权益（或股东权益）合计
            },
            '10010310': {
                'AssetTotal': (FORM_GET, r'//tr[33]/td[5]/input'),  # 资产合计
                'AssetInitial': (FORM_GET, r'//tr[33]/td[6]/input'),  # 资产合计
                'DebtsTotal': (FORM_GET, r'//tr[33]/td[13]/input'),  # 负债和所有者权益（或股东权益）总计
                'DebtsInitial': (FORM_GET, r'//tr[33]/td[14]/input'),  # 负债和所有者权益（或股东权益）总计
            },
        },
        'lirunbiao': {
            # 一、营业收入
            '10020000': {
                'YearTotal': (FORM_GET, r'//tr[2]/td[7]/input'),  # 本年累计金额
                'Amount': (FORM_FILL, r'//tr[2]/td[10]/input'),  # 本月金额
            },
            # 减：营业成本
            '10020010': {
                'YearTotal': (FORM_GET, r'//tr[3]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[3]/td[10]/input'),
            },
            # 税金及附加
            '10020020': {
                'YearTotal': (FORM_GET, r'//tr[4]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[4]/td[10]/input'),
            },
            # 其中：消费税
            '10020030': {
                'YearTotal': (FORM_GET, r'//tr[5]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[5]/td[10]/input'),
            },
            # 营业税
            '10020040': {
                'YearTotal': (FORM_GET, r'//tr[6]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[6]/td[10]/input'),
            },
            # 城市维护建设税
            '10020050': {
                'YearTotal': (FORM_GET, r'//tr[7]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[7]/td[10]/input'),
            },
            # 资源税
            '10020060': {
                'YearTotal': (FORM_GET, r'//tr[8]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[8]/td[10]/input'),
            },
            # 土地增值税
            '10020070': {
                'YearTotal': (FORM_GET, r'//tr[9]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[9]/td[10]/input'),
            },
            # 城镇土地使用税、房产税、车船税、印花税
            '10020080': {
                'YearTotal': (FORM_GET, r'//tr[10]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[10]/td[10]/input'),
            },
            # 教育费附加、矿产资源补偿费、排污费
            '10020090': {
                'YearTotal': (FORM_GET, r'//tr[11]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[11]/td[10]/input'),
            },
            # 销售费用
            '10020100': {
                'YearTotal': (FORM_GET, r'//tr[12]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[12]/td[10]/input'),
            },
            # 其中：商品维修费
            '10020110': {
                'YearTotal': (FORM_GET, r'//tr[13]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[13]/td[10]/input'),
            },
            # 广告费和业务宣传费
            '10020120': {
                'YearTotal': (FORM_GET, r'//tr[14]/td[7]/input'),
                'Amount': (FORM_GET, r'//tr[14]/td[10]/input'),
            },
            # 管理费用
            '10020130': {
                'YearTotal': (FORM_GET, r'//tr[15]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[15]/td[10]/input'),
            },
            # 其中：开办费
            '10020140': {
                'YearTotal': (FORM_GET, r'//tr[16]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[16]/td[10]/input'),
            },
            # 业务招待费
            '10020150': {
                'YearTotal': (FORM_GET, r'//tr[17]/td[7]/input'),
                'Amount': (FORM_GET, r'//tr[17]/td[10]/input'),
            },
            # 研究费用
            '10020160': {
                'YearTotal': (FORM_GET, r'//tr[18]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[18]/td[10]/input'),
            },
            # 财务费用
            '10020170': {
                'YearTotal': (FORM_GET, r'//tr[19]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[19]/td[10]/input'),
            },
            # 其中：利息费用（收入以－号填列）
            '10020180': {
                'YearTotal': (FORM_GET, r'//tr[20]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[20]/td[10]/input'),
            },
            # 加：投资收益（亏损以－号填列）
            '10020190': {
                'YearTotal': (FORM_GET, r'//tr[21]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[21]/td[10]/input'),
            },
            # 二、营业利润(亏损以“-”号填列)
            '10020200': {
                'YearTotal': (FORM_GET, r'//tr[22]/td[7]/input'),
                'Amount': (FORM_GET, r'//tr[22]/td[10]/input'),
            },
            #  加：营业外收入
            '10020210': {
                'YearTotal': (FORM_GET, r'//tr[23]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[23]/td[10]/input'),
            },
            #  其中：政府补助
            '10020220': {
                'YearTotal': (FORM_GET, r'//tr[24]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[24]/td[10]/input'),
            },
            #  减：营业外支出
            '10020230': {
                'YearTotal': (FORM_GET, r'//tr[25]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[25]/td[10]/input'),
            },
            #  其中：坏账损失
            '10020240': {
                'YearTotal': (FORM_GET, r'//tr[26]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[26]/td[10]/input'),
            },
            #  无法收回的长期债券投资损失
            '10020250': {
                'YearTotal': (FORM_GET, r'//tr[27]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[27]/td[10]/input'),
            },
            #  无法收回的长期股权投资损失
            '10020260': {
                'YearTotal': (FORM_GET, r'//tr[28]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[28]/td[10]/input'),
            },
            # 自然灾害等不可抗力因素造成的损失
            '10020270': {
                'YearTotal': (FORM_GET, r'//tr[29]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[29]/td[10]/input'),
            },
            #  税收滞纳金
            '10020280': {
                'YearTotal': (FORM_GET, r'//tr[30]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[30]/td[10]/input'),
            },
            #  三、利润总额（亏损总额以－号填列）
            '10020290': {
                'YearTotal': (FORM_GET, r'//tr[31]/td[7]/input'),
                'Amount': (FORM_GET, r'//tr[31]/td[10]/input'),
            },
            #  减：所得税费用
            '10020300': {
                'YearTotal': (FORM_GET, r'//tr[32]/td[7]/input'),
                'Amount': (FORM_FILL, r'//tr[32]/td[10]/input'),
            },
            # 四、净利润（净亏损以－号填列）
            '10020310': {
                'YearTotal': (FORM_GET, r'//tr[33]/td[7]/input'),
                'Amount': (FORM_GET, r'//tr[33]/td[10]/input'),
            },
        },
        'xianjinliuliangbiao': {
            # 一、经营活动产生的现金流量
            '10030000': {
                'InitalAmount': (FORM_NO, r'//tr[2]/td[5]'),  # 本年累计金额
                'Amount': (FORM_NO, r'//tr[2]/td[6]'),  # 本月金额
            },
            # 销售产成品、商品、提供劳务收到的现金
            '10030010': {
                'InitalAmount': (FORM_GET, r'//tr[3]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[3]/td[6]/input'),
            },
            # 收到其他与经营活动有关的现金
            '10030020': {
                'InitalAmount': (FORM_GET, r'//tr[4]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[4]/td[6]/input'),
            },
            # 购买原材料、商品、接受劳务支付的现金
            '10030030': {
                'InitalAmount': (FORM_GET, r'//tr[5]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[5]/td[6]/input'),
            },
            # 支付的职工薪酬
            '10030040': {
                'InitalAmount': (FORM_GET, r'//tr[6]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[6]/td[6]/input'),
            },
            # 支付的税费
            '10030050': {
                'InitalAmount': (FORM_GET, r'//tr[7]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[7]/td[6]/input'),
            },
            # 支付其他与经营活动有关的现金
            '10030060': {
                'InitalAmount': (FORM_GET, r'//tr[8]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[8]/td[6]/input'),
            },
            # 经营活动产生的现金流量净额
            '10030070': {
                'InitalAmount': (FORM_GET, r'//tr[9]/td[5]/input'),
                'Amount': (FORM_GET, r'//tr[9]/td[6]/input'),
            },
            # 二、投资活动产生的现金流量:
            '10030080': {
                'InitalAmount': (FORM_NO, r'//tr[10]/td[5]'),
                'Amount': (FORM_NO, r'//tr[10]/td[6]'),
            },
            # 收回短期投资、长期债券投资和长期股权投资收到的现金
            '10030090': {
                'InitalAmount': (FORM_GET, r'//tr[11]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[11]/td[6]/input'),
            },
            # 取得投资收益收到的现金
            '10030100': {
                'InitalAmount': (FORM_GET, r'//tr[12]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[12]/td[6]/input'),
            },
            # 处置固定资产、无形资产和其他非流动资产收回的现金净额
            '10030110': {
                'InitalAmount': (FORM_GET, r'//tr[13]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[13]/td[6]/input'),
            },
            # 短期投资、长期债券投资和长期股权投资支付的现金
            '10030120': {
                'InitalAmount': (FORM_GET, r'//tr[14]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[14]/td[6]/input'),
            },
            # 购建固定资产、无形资产和其他非流动资产支付的现金
            '10030130': {
                'InitalAmount': (FORM_GET, r'//tr[15]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[15]/td[6]/input'),
            },
            # 投资活动产生的现金流量净额
            '10030140': {
                'InitalAmount': (FORM_GET, r'//tr[16]/td[5]/input'),
                'Amount': (FORM_GET, r'//tr[16]/td[6]/input'),
            },
            # 三、筹资活动产生的现金流量：
            '10030150': {
                'InitalAmount': (FORM_NO, r'//tr[17]/td[5]'),
                'Amount': (FORM_NO, r'//tr[17]/td[6]'),
            },
            # 取得借款收到的现金
            '10030160': {
                'InitalAmount': (FORM_GET, r'//tr[18]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[18]/td[6]/input'),
            },
            # 吸收投资者投资收到的现金
            '10030170': {
                'InitalAmount': (FORM_GET, r'//tr[19]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[19]/td[6]/input'),
            },
            # 偿还借款本金支付的现金
            '10030180': {
                'InitalAmount': (FORM_GET, r'//tr[20]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[20]/td[6]/input'),
            },
            # 偿还借款利息支付的现金
            '10030190': {
                'InitalAmount': (FORM_GET, r'//tr[21]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[21]/td[6]/input'),
            },
            # 分配利润支付的现金
            '10030200': {
                'InitalAmount': (FORM_GET, r'//tr[22]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[22]/td[6]/input'),
            },
            # 筹资活动产生的现金流量净额
            '10030210': {
                'InitalAmount': (FORM_GET, r'//tr[23]/td[5]/input'),
                'Amount': (FORM_GET, r'//tr[23]/td[6]/input'),
            },
            # 四、现金净增加额
            '10030220': {
                'InitalAmount': (FORM_GET, r'//tr[24]/td[5]/input'),
                'Amount': (FORM_GET, r'//tr[24]/td[6]/input'),
            },
            # 加：期初现金余额
            '10030230': {
                'InitalAmount': (FORM_GET, r'//tr[25]/td[5]/input'),
                'Amount': (FORM_FILL, r'//tr[25]/td[6]/input'),
            },
            # 五、期末现金余额
            '10030240': {
                'InitalAmount': (FORM_GET, r'//tr[26]/td[5]/input'),
                'Amount': (FORM_GET, r'//tr[26]/td[6]/input'),
            },
        },
    }


# 财务报表 一般企业会计准则
def get_local_finance_commonly():
    return {
        'zichanfuzhaibiao': {},
        'lirunbiao': {},
        'xianjinliuliangbiao': {},
    }


# 增值税一般纳税人
def get_local_added_commonly():
    return {
        # 一般纳税人主表
        '5001': {
            'firstTable': {
                # （一）按适用税率计税销售额
                'oneRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[7]/td[7]/input'),  # 一般项目 本月
                    'commonlyYear': (FORM_INIT, r'//tr[7]/td[8]/input'),  # 一般项目 本年
                    'signAndRetreatMonth': (FORM_GET, r'//tr[7]/td[10]/input'),  # 即征即退项目 本月
                    'signAndRetreatYear': (FORM_INIT, r'//tr[7]/td[12]/input'),  # 即征即退项目 本年
                },
                # 其中：应税货物销售额
                'twoRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[8]/td[7]/input'),  # 一般项目 本月
                    'commonlyYear': (FORM_INIT, r'//tr[8]/td[8]/input'),  # 一般项目 本年
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[8]/td[10]/input'),  # 即征即退项目 本月
                    'signAndRetreatYear': (FORM_INIT, r'//tr[8]/td[12]/input'),  # 即征即退项目 本年
                },
                # 应税劳务销售额
                'threeRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[9]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[9]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[9]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[9]/td[12]/input'),
                },
                # 纳税检查调整的销售额
                'fourRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[10]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[10]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[10]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[10]/td[12]/input'),
                },
                # （二）按简易办法计税销售额
                'fiveRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[11]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[11]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[11]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[11]/td[12]/input'),
                },
                # 其中：纳税检查调整的销售额
                'sixRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[12]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[12]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[12]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[12]/td[12]/input'),
                },
                # （三）免、抵、退办法出口销售额
                'sevenRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[13]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[13]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[13]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[13]/td[12]'),
                },
                # （四）免税销售额
                'eightRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[14]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[14]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[14]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[14]/td[12]'),
                },
                # 其中：免税货物销售额
                'nineRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[15]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[15]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[15]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[15]/td[12]'),
                },
                # 免税劳务销售额
                'tenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[16]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[16]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[16]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[16]/td[12]'),
                },
            },
            'secondTable': {
                # 销项税额
                'elevenRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[17]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[17]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[17]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[17]/td[12]/input'),
                },
                # 进项税额
                'twelveRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[18]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[18]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[18]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[18]/td[12]/input'),
                },
                # 上期留抵税额
                'thirteenRow': {
                    'commonlyMonth': (FORM_INIT, r'//tr[19]/td[7]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[19]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[19]/td[10]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[19]/td[12]'),
                },
                # 进项税额转出
                'fourteenRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[20]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[20]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[20]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[20]/td[12]/input'),
                },
                # 免、抵、退应退税额
                'fifteenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[21]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[21]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[21]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[21]/td[12]'),
                },
                # 按适用税率计算的纳税检查应补缴税额
                'sixteenRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[22]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[22]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[22]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[22]/td[12]'),
                },
                # 应抵扣税额合计
                'seventeenRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[23]/td[7]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[23]/td[8]'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[23]/td[10]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[23]/td[12]'),
                },
                # 实际抵扣税额
                'eighteenRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[24]/td[7]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[24]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[24]/td[10]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[24]/td[12]/input'),
                },
                # 应纳税额
                'nineteenRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[25]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[25]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[25]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[25]/td[12]/input'),
                },
                # 期末留抵税额
                'twentyRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[26]/td[7]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[26]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[26]/td[10]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[26]/td[12]'),
                },
                # 简易计税办法计算的应纳税额
                'twentyOneRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[27]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[27]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[27]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[27]/td[12]/input'),
                },
                # 按简易计税办法计算的纳税检查应补缴税额
                'twentyTwoRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[28]/td[7]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[28]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[28]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[28]/td[12]'),
                },
                # 应纳税额减征额
                'twentyThreeRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[29]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[29]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[29]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[29]/td[12]/input'),
                },
                # 应纳税额合计
                'twentyFourRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[30]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[30]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[30]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[30]/td[12]/input'),
                },
            },
            'thirdTable': {
                # 期初未缴税额（多缴为负数）
                'twentyFiveRow': {
                    'commonlyMonth': (FORM_INIT, r'//tr[31]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[31]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[31]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[31]/td[12]/input'),
                },
                # 实收出口开具专用缴款书退税额
                'twentySixRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[32]/td[7]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[32]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[32]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[32]/td[12]'),
                },
                # 本期已缴税额
                'twentySevenRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[33]/td[7]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[33]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[33]/td[10]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[33]/td[12]/input'),
                },
                # ①分次预缴税额
                'twentyEightRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[34]/td[7]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[34]/td[8]'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[34]/td[10]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[34]/td[12]'),
                },
                # ②出口开具专用缴款书预缴税额
                'twentyNineRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[35]/td[7]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[35]/td[8]'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[35]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[35]/td[12]'),
                },
                # ③本期缴纳上期应纳税额
                'thirtyRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[36]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[36]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[36]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[36]/td[12]/input'),
                },
                # ④本期缴纳欠缴税额
                'thirtyOneRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[37]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[37]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[37]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[37]/td[12]/input'),
                },
                # 期末未缴税额（多缴为负数）
                'thirtyTwoRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[38]/td[7]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[38]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[38]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[38]/td[12]/input'),
                },
                # 其中：欠缴税额（≥0）
                'thirtyThreeRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[39]/td[7]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[39]/td[8]'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[39]/td[10]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[39]/td[12]'),
                },
                # 本期应补(退)税额
                'thirtyFourRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[40]/td[7]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[40]/td[8]'),
                    'signAndRetreatMonth': (FORM_GET, r'//tr[40]/td[10]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[40]/td[12]'),
                },
                # 即征即退实际退税额
                'thirtyFiveRow': {
                    'commonlyMonth': (FORM_NO, r'//tr[41]/td[7]'),
                    'commonlyYear': (FORM_NO, r'//tr[41]/td[8]'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[41]/td[10]/input'),
                    'signAndRetreatYear': (FORM_INIT, r'//tr[41]/td[12]/input'),
                },
                # 期初未缴查补税额
                'thirtySixRow': {
                    'commonlyMonth': (FORM_INIT, r'//tr[42]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[42]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[42]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[42]/td[12]'),
                },
                # 本期入库查补税额
                'thirtySevenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[43]/td[7]/input'),
                    'commonlyYear': (FORM_INIT, r'//tr[43]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[43]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[43]/td[12]'),
                },
                # 期末未缴查补税额
                'thirtyEightRow': {
                    'commonlyMonth': (FORM_GET, r'//tr[44]/td[7]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[44]/td[8]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[44]/td[10]'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[44]/td[12]'),
                },
            },
        },

        # 增值税 一般纳税人 附表1
        '5002': {
            'firstTable': {
                # 13%税率的货物及加工修理修配劳务（一、一般计税方法计税）
                'oneRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[4]/td[7]/input'),  # 开具增值税专用发票 销售额
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[4]/td[8]/input'),  # 开具增值税专用发票 销项(应纳)税额
                    'otherSalesAmount': (FORM_GET, r'//tr[4]/td[9]/input'),  # 开具其他发票 销售额
                    'otherSalesTax': (FORM_GET, r'//tr[4]/td[10]/input'),  # 开具其他发票 销项(应纳)税额
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[4]/td[11]/input'),  # 未开具发票 销售额
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[4]/td[12]/input'),  # 未开具发票 销项(应纳)税额
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[4]/td[13]/input'),  # 纳税检查调整 销售额
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[4]/td[14]/input'),  # 纳税检查调整 销项(应纳)税额
                    'totalSalesAmount': (FORM_GET, r'//tr[4]/td[15]/input'),  # 合计 销售额
                    'totalSalesTax': (FORM_GET, r'//tr[4]/td[16]/input'),  # 合计 销项（应缴）税额
                    'totalPriceTax': (FORM_NO, r'//tr[4]/td[17]'),  # 合计 价税合计
                    'actualDeductionAmount': (FORM_NO, r'//tr[4]/td[18]'),  # 服务、不动产和无形资产扣除项目本期实际扣除金额
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[4]/td[19]'),  # 扣除后 含税(免税)销售额
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[4]/td[20]'),  # 扣除后 销项(应纳)税额
                },
                # 13%税率的服务、不动产和无形资产
                'twoRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[5]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[5]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[5]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[5]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[5]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[5]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[5]/td[13]/input'),
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[5]/td[14]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[5]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[5]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[5]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[5]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[5]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[5]/td[20]/input'),
                },
                # 13%税率
                # 'threeRow': {
                #     'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[6]/td[3]/input'),
                #     'valueAddedTaxSalesTax': (FORM_GET, r'//tr[6]/td[4]/input'),
                #     'otherSalesAmount': (FORM_GET, r'//tr[6]/td[5]/input'),
                #     'otherSalesTax': (FORM_GET, r'//tr[6]/td[6]/input'),
                #     'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[6]/td[7]/input'),
                #     'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[6]/td[8]/input'),
                #     'taxInspectionSalesAmount': (FORM_FILL, r'//tr[6]/td[9]/input'),
                #     'taxInspectionSalesTax': (FORM_FILL, r'//tr[6]/td[10]/input'),
                #     'totalSalesAmount': (FORM_GET, r'//tr[6]/td[11]/input'),
                #     'totalSalesTax': (FORM_GET, r'//tr[6]/td[12]/input'),
                #     'totalPriceTax': (FORM_NO, r'//tr[6]/td[13]/input'),
                #     'actualDeductionAmount': (FORM_NO, r'//tr[6]/td[14]/input'),
                #     'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[6]/td[15]/input'),
                #     'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[6]/td[16]/input'),
                # },
                # 9%税率的货物及加工修理修配劳务（一、一般计税方法计税）
                'threeRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[7]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[7]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[7]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[7]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[7]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[7]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[7]/td[13]/input'),
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[7]/td[14]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[7]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[7]/td[16]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[7]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[7]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[7]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[7]/td[20]'),
                },
                # 9%税率的服务、不动产和无形资产（一、一般计税方法计税）
                'fourRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[8]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[8]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[8]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[8]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[8]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[8]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[8]/td[13]/input'),
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[8]/td[14]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[8]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[8]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[8]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[8]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[8]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[8]/td[20]/input'),
                },
                # 6%税率（一、一般计税方法计税）
                'fiveRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[9]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[9]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[9]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[9]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[9]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[9]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[9]/td[13]/input'),
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[9]/td[14]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[9]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[9]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[9]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[9]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[9]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[9]/td[20]/input'),
                },
                # 即征即退货物及加工修理修配劳务（一、一般计税方法计税）
                'sixRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[10]/td[7]'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[10]/td[8]'),
                    'otherSalesAmount': (FORM_NO, r'//tr[10]/td[9]'),
                    'otherSalesTax': (FORM_NO, r'//tr[10]/td[10]'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[10]/td[11]'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[10]/td[12]'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[10]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[10]/td[14]'),
                    'totalSalesAmount': (FORM_FILL, r'//tr[10]/td[15]/input'),
                    'totalSalesTax': (FORM_FILL, r'//tr[10]/td[16]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[10]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[10]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[10]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[10]/td[20]'),
                },
                # 即征即退服务、不动产和无形资产（一、一般计税方法计税）
                'sevenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[11]/td[7]'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[11]/td[8]'),
                    'otherSalesAmount': (FORM_NO, r'//tr[11]/td[9]'),
                    'otherSalesTax': (FORM_NO, r'//tr[11]/td[10]'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[11]/td[11]'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[11]/td[12]'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[11]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[11]/td[14]'),
                    'totalSalesAmount': (FORM_FILL, r'//tr[11]/td[15]/input'),
                    'totalSalesTax': (FORM_FILL, r'//tr[11]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[11]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[11]/td[18]/input'),  # 服务、不动产和无形资产扣除项目本期实际扣除金额
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[11]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[11]/td[20]/input'),
                },
            },

            'secondTable': {
                # 6%征收率
                'eightRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[12]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[12]/td[8]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[12]/td[9]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[12]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[12]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[12]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[12]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[12]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[12]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[12]/td[16]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[12]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[12]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[12]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[12]/td[20]'),
                },
                # 5%征收率的货物及加工修理修配劳务
                'nineARow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[13]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[13]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[13]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[13]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[13]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[13]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[13]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[13]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[13]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[13]/td[16]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[13]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[13]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[13]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[13]/td[20]'),
                },
                # 5%征收率的服务、不动产和无形资产
                'nineBRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[14]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[14]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[14]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[14]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[14]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[14]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[14]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[14]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[14]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[14]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[14]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[14]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[14]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[14]/td[20]/input'),
                },
                # 4%征收率
                'tenRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[15]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[15]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[15]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[15]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[15]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[15]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[15]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[15]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[15]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[15]/td[16]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[15]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[15]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[15]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[15]/td[20]'),
                },
                # 3%征收率的货物及加工修理修配劳务
                'elevenRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[16]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[16]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[16]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[16]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[16]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[16]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[16]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[16]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[16]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[16]/td[16]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[16]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[16]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[16]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[16]/td[20]'),
                },
                # 3%征收率的服务、不动产和无形资产
                'twelveRow': {
                    'valueAddedTaxSalesAmount': (FORM_GET, r'//tr[17]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_GET, r'//tr[17]/td[8]/input'),
                    'otherSalesAmount': (FORM_GET, r'//tr[17]/td[9]/input'),
                    'otherSalesTax': (FORM_GET, r'//tr[17]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[17]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[17]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[17]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[17]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[17]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[17]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[17]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[17]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[17]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[17]/td[20]/input'),
                },
                # 预征率   %
                'thirteenARow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[18]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[18]/td[8]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[18]/td[9]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[18]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[18]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[18]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[18]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[18]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[18]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[18]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[18]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[18]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[18]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_FILL, r'//tr[18]/td[20]/input'),
                },
                # 预征率   %
                'thirteenBRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[19]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[19]/td[8]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[19]/td[9]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[19]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[19]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[19]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[19]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[19]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[19]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[19]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[19]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[19]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[19]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_FILL, r'//tr[19]/td[20]/input'),
                },
                # 预征率   %
                'thirteenCRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[20]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[20]/td[8]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[20]/td[9]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[20]/td[10]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[20]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[20]/td[12]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[20]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[20]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[20]/td[15]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[20]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[20]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[20]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[20]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_FILL, r'//tr[20]/td[20]/input'),
                },
                # 即征即退货物及加工修理修配劳务（二、简易计税方法计税）
                'fourteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[21]/td[7]'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[21]/td[8]'),
                    'otherSalesAmount': (FORM_NO, r'//tr[21]/td[9]'),
                    'otherSalesTax': (FORM_NO, r'//tr[21]/td[10]'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[21]/td[11]'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[21]/td[12]'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[21]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[21]/td[14]'),
                    'totalSalesAmount': (FORM_FILL, r'//tr[21]/td[15]/input'),
                    'totalSalesTax': (FORM_FILL, r'//tr[21]/td[16]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[21]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[21]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[21]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[21]/td[20]'),
                },
                # 即征即退服务、不动产和无形资产（二、简易计税方法计税）
                'fifteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[22]/td[7]'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[22]/td[8]'),
                    'otherSalesAmount': (FORM_NO, r'//tr[22]/td[9]'),
                    'otherSalesTax': (FORM_NO, r'//tr[22]/td[10]'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[22]/td[11]'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[22]/td[12]'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[22]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[22]/td[14]'),
                    'totalSalesAmount': (FORM_FILL, r'//tr[22]/td[15]/input'),
                    'totalSalesTax': (FORM_FILL, r'//tr[22]/td[16]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[22]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[22]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[22]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[22]/td[20]/input'),
                },
            },

            'thirdTable': {
                # 货物及加工修理修配劳务（三、免抵退税）
                'sixteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[23]/td[7]'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[23]/td[8]'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[23]/td[9]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[23]/td[10]'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[23]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[23]/td[12]'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[23]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[23]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[23]/td[15]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[23]/td[16]'),
                    'totalPriceTax': (FORM_NO, r'//tr[23]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[23]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[23]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[23]/td[20]'),
                },
                # 服务、不动产和无形资产（三、免抵退税）
                'seventeenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[24]/td[7]'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[24]/td[8]'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[24]/td[9]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[24]/td[10]'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[24]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[24]/td[12]'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[24]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[24]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[24]/td[15]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[24]/td[16]'),
                    'totalPriceTax': (FORM_GET, r'//tr[24]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[24]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[24]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[24]/td[20]'),
                },
            },

            'fourthTable': {
                # 货物及加工修理修配劳务（四、免税）
                'eighteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[25]/td[7]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[25]/td[8]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[25]/td[9]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[25]/td[10]'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[25]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[25]/td[12]'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[25]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[25]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[25]/td[15]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[25]/td[16]'),
                    'totalPriceTax': (FORM_NO, r'//tr[25]/td[17]'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[25]/td[18]'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[25]/td[19]'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[25]/td[20]'),

                },
                # 服务、不动产和无形资产（四、免税）
                'nineteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[26]/td[7]'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[26]/td[8]'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[26]/td[9]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[26]/td[10]'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[26]/td[11]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[26]/td[12]'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[26]/td[13]'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[26]/td[14]'),
                    'totalSalesAmount': (FORM_GET, r'//tr[26]/td[15]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[26]/td[16]'),
                    'totalPriceTax': (FORM_GET, r'//tr[26]/td[17]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[26]/td[18]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[26]/td[19]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[26]/td[20]'),
                },
            },
        },

        # 增值税 一般纳税人 附表2
        '5003': {
            'firstTable': {
                # （一）认证相符的增值税专用发票
                'oneRow': {
                    'amount': (FORM_GET, r'//tr[3]/td[4]/input'),  # 份数
                    'money': (FORM_GET, r'//tr[3]/td[5]/input'),  # 金额
                    'taxAmount': (FORM_GET, r'//tr[3]/td[6]/input'),  # 税额
                },
                # 其中：本期认证相符且本期申报抵扣
                'twoRow': {
                    'amount': (FORM_GET, r'//tr[4]/td[4]/input'),  # 份数
                    'money': (FORM_GET, r'//tr[4]/td[5]/input'),  # 金额
                    'taxAmount': (FORM_GET, r'//tr[4]/td[6]/input'),  # 税额
                },
                # 前期认证相符且本期申报抵扣
                'threeRow': {
                    'amount': (FORM_FILL, r'//tr[5]/td[4]/input'),  # 份数
                    'money': (FORM_FILL, r'//tr[5]/td[5]/input'),  # 金额
                    'taxAmount': (FORM_FILL, r'//tr[5]/td[6]/input'),  # 税额
                },
                # （二）其他扣税凭证
                'fourRow': {
                    'amount': (FORM_GET, r'//tr[6]/td[4]/input'),  # 份数
                    'money': (FORM_GET, r'//tr[6]/td[5]/input'),  # 金额
                    'taxAmount': (FORM_GET, r'//tr[6]/td[6]/input'),  # 税额
                },
                # 其中：海关进口增值税专用缴款书
                'fiveRow': {
                    'amount': (FORM_FILL, r'//tr[7]/td[4]/input'),  # 份数
                    'money': (FORM_FILL, r'//tr[7]/td[5]/input'),  # 金额
                    'taxAmount': (FORM_FILL, r'//tr[7]/td[6]/input'),  # 税额
                },
                # 农产品收购发票或者销售发票
                'sixRow': {
                    'amount': (FORM_FILL, r'//tr[8]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[8]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[8]/td[6]/input'),
                },
                # 代扣代缴税收缴款凭证
                'sevenRow': {
                    'amount': (FORM_FILL, r'//tr[9]/td[4]/input'),
                    'money': (FORM_NO, r'//tr[9]/td[5]'),
                    'taxAmount': (FORM_FILL, r'//tr[9]/td[6]/input'),
                },
                # 加计扣除农产品进项税额
                'eightARow': {
                    'amount': (FORM_NO, r'//tr[10]/td[4]'),
                    'money': (FORM_NO, r'//tr[10]/td[5]'),
                    'taxAmount': (FORM_FILL, r'//tr[10]/td[6]/input'),
                },
                # 其他
                'eightBRow': {
                    'amount': (FORM_FILL, r'//tr[11]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[11]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[11]/td[6]/input'),
                },
                # （三）本期用于购建不动产的扣税凭证
                'nineRow': {
                    'amount': (FORM_FILL, r'//tr[12]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[12]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[12]/td[6]/input'),
                },
                # （四）本期用于抵扣的旅客运输服务扣税凭证
                'tenRow': {
                    'amount': (FORM_FILL, r'//tr[13]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[13]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[13]/td[6]/input'),
                },
                # （五）外贸企业进项税额抵扣证明
                'elevenRow': {
                    'amount': (FORM_NO, r'//tr[14]/td[4]'),
                    'money': (FORM_NO, r'//tr[14]/td[5]'),
                    'taxAmount': (FORM_FILL, r'//tr[14]/td[6]/input'),
                },
                # 当期申报抵扣进项税额合计
                'twelveRow': {
                    'amount': (FORM_GET, r'//tr[15]/td[4]/input'),
                    'money': (FORM_GET, r'//tr[15]/td[5]/input'),
                    'taxAmount': (FORM_GET, r'//tr[15]/td[6]/input'),
                },
            },
            'secondTable': {
                # 本期进项税额转出额
                'oneRow': {
                    'taxAmount': (FORM_GET, r'//tr[18]/td[4]/input'),
                },
                # 其中：免税项目用
                'twoRow': {
                    'taxAmount': (FORM_FILL, r'//tr[19]/td[4]/input'),
                },
                # 集体福利、个人消费
                'threeRow': {
                    'taxAmount': (FORM_FILL, r'//tr[20]/td[4]/input'),
                },
                # 非正常损失
                'fourRow': {
                    'taxAmount': (FORM_FILL, r'//tr[21]/td[4]/input'),
                },
                # 简易计税方法征税项目用
                'fiveRow': {
                    'taxAmount': (FORM_FILL, r'//tr[22]/td[4]/input'),
                },
                # 免抵退税办法不得抵扣的进项税额
                'sixRow': {
                    'taxAmount': (FORM_FILL, r'//tr[23]/td[4]/input'),
                },
                # 纳税检查调减进项税额
                'sevenRow': {
                    'taxAmount': (FORM_FILL, r'//tr[24]/td[4]/input'),
                },
                # 红字专用发票信息表注明的进项税额
                'eightRow': {
                    'taxAmount': (FORM_FILL, r'//tr[25]/td[4]/input'),
                },
                # 上期留抵税额抵减欠税
                'nineRow': {
                    'taxAmount': (FORM_FILL, r'//tr[26]/td[4]/input'),
                },
                # 上期留抵税额退税
                'tenRow': {
                    'taxAmount': (FORM_FILL, r'//tr[27]/td[4]/input'),
                },
                # 其他应作进项税额转出的情形
                'elevenRow': {
                    'taxAmount': (FORM_FILL, r'//tr[38]/td[4]/input'),
                },
            },
            'thirdTable': {
                # （一）认证相符的增值税专用发票
                'oneRow': {
                    'amount': (FORM_NO, r'//tr[31]/td[4]'),
                    'money': (FORM_NO, r'//tr[31]/td[5]'),
                    'taxAmount': (FORM_NO, r'//tr[31]/td[6]'),
                },
                # 期初已认证相符但未申报抵扣
                'twoRow': {
                    'amount': (FORM_FILL, r'//tr[32]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[32]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[32]/td[6]/input'),
                },
                # 本期认证相符且本期未申报抵扣
                'threeRow': {
                    'amount': (FORM_FILL, r'//tr[33]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[33]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[33]/td[6]/input'),
                },
                # 期末已认证相符但未申报抵扣
                'fourRow': {
                    'amount': (FORM_FILL, r'//tr[34]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[34]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[34]/td[6]/input'),
                },
                # 其中：按照税法规定不允许抵扣
                'fiveRow': {
                    'amount': (FORM_FILL, r'//tr[35]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[35]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[35]/td[6]/input'),
                },
                # （二）其他扣税凭证
                'sixRow': {
                    'amount': (FORM_GET, r'//tr[36]/td[4]/input'),
                    'money': (FORM_GET, r'//tr[36]/td[5]/input'),
                    'taxAmount': (FORM_GET, r'//tr[36]/td[6]/input'),
                },
                # 其中：海关进口增值税专用缴款书
                'sevenRow': {
                    'amount': (FORM_FILL, r'//tr[37]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[37]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[37]/td[6]/input'),
                },
                # 农产品收购发票或者销售发票
                'eightRow': {
                    'amount': (FORM_FILL, r'//tr[38]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[38]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[38]/td[6]/input'),
                },
                # 代扣代缴税收缴款凭证
                'nineRow': {
                    'amount': (FORM_FILL, r'//tr[39]/td[4]/input'),
                    'money': (FORM_NO, r'//tr[39]/td[5]'),
                    'taxAmount': (FORM_FILL, r'//tr[39]/td[6]/input'),
                },
                # 其他
                'tenRow': {
                    'amount': (FORM_FILL, r'//tr[40]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[40]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[40]/td[6]/input'),
                },
                #
                'elevenRow': {
                    'amount': (FORM_NO, r'//tr[41]/td[4]'),
                    'money': (FORM_NO, r'//tr[41]/td[5]'),
                    'taxAmount': (FORM_NO, r'//tr[41]/td[6]'),
                },
            },
            'fourthTable': {
                # 本期认证相符的增值税专用发票
                'oneRow': {
                    'amount': (FORM_FILL, r'//tr[44]/td[4]/input'),
                    'money': (FORM_FILL, r'//tr[44]/td[5]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[44]/td[6]/input'),
                },
                # 代扣代缴税额
                'twoRow': {
                    'amount': (FORM_NO, r'//tr[45]/td[4]'),
                    'money': (FORM_NO, r'//tr[45]/td[5]'),
                    'taxAmount': (FORM_FILL, r'//tr[45]/td[6]/input'),
                },
            },
        },

        # 增值税 一般纳税人 附表3
        '5006': {
            'firstTable': {
                # 13%税率的项目
                'oneRow': {
                    'dutyFreeAmount': (FORM_GET, r'//tr[4]/td[3]/input'),  # 本期应税服务价税合计额(免税销售额)
                    'initialAmount': (FORM_INIT, r'//tr[4]/td[4]/input'),  # 应税服务扣除项目 期初余额
                    'currentPeriodAmount': (FORM_FILL, r'//tr[4]/td[5]/input'),  # 应税服务扣除项目 本期发生额
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[4]/td[6]/input'),  # 应税服务扣除项目 本期应扣除金额
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[4]/td[7]/input'),  # 应税服务扣除项目 本期实际扣除金额
                    'endAmount': (FORM_GET, r'//tr[4]/td[8]/input'),  # 应税服务扣除项目 期末余额
                },
                # 9%税率的项目
                'twoRow': {
                    'dutyFreeAmount': (FORM_GET, r'//tr[5]/td[3]/input'),
                    'initialAmount': (FORM_INIT, r'//tr[5]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[5]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[5]/td[7]/input'),
                    'endAmount': (FORM_GET, r'//tr[5]/td[8]/input'),
                },
                # 6%税率的项目(不含金融商品转让)
                'threeRow': {
                    'dutyFreeAmount': (FORM_GET, r'//tr[6]/td[3]/input'),
                    'initialAmount': (FORM_INIT, r'//tr[6]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[6]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[6]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[6]/td[7]/input'),
                    'endAmount': (FORM_GET, r'//tr[6]/td[8]/input'),
                },
                # 6%税率的金融商品转让项目
                'fourRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[7]/td[3]/input'),
                    'initialAmount': (FORM_INIT, r'//tr[7]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[7]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[7]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[7]/td[7]/input'),
                    'endAmount': (FORM_GET, r'//tr[7]/td[8]/input'),
                },
                # 5%征收率的项目
                'fiveRow': {
                    'dutyFreeAmount': (FORM_GET, r'//tr[8]/td[3]/input'),
                    'initialAmount': (FORM_INIT, r'//tr[8]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[8]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[8]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[8]/td[7]/input'),
                    'endAmount': (FORM_GET, r'//tr[8]/td[8]/input'),
                },
                # 3%税率的项目
                'sixRow': {
                    'dutyFreeAmount': (FORM_GET, r'//tr[9]/td[3]/input'),
                    'initialAmount': (FORM_INIT, r'//tr[9]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[9]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[9]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[9]/td[7]/input'),
                    'endAmount': (FORM_GET, r'//tr[9]/td[8]/input'),
                },
                # 免抵退税的项目
                'sevenRow': {
                    'dutyFreeAmount': (FORM_GET, r'//tr[10]/td[3]/input'),
                    'initialAmount': (FORM_INIT, r'//tr[10]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[10]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[10]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[10]/td[7]/input'),
                    'endAmount': (FORM_GET, r'//tr[10]/td[8]/input'),
                },
                # 免税的项目
                'eightRow': {
                    'dutyFreeAmount': (FORM_GET, r'//tr[11]/td[3]/input'),
                    'initialAmount': (FORM_INIT, r'//tr[11]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[11]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[11]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[11]/td[7]/input'),
                    'endAmount': (FORM_GET, r'//tr[11]/td[8]/input'),
                },
            },
        },

        # 增值税 一般纳税人 附表4
        '5007': {
            # 一、税额抵扣情况
            'firstTable': {
                # 增值税税控系统专用设备费及技术维护费
                'oneRow': {
                    'initialAmount': (FORM_INIT, r'//tr[4]/td[4]/input'),  # 期初余额
                    'currentPeriodAmount': (FORM_FILL, r'//tr[4]/td[5]/input'),  # 本期发生额
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[4]/td[7]/input'),  # 本期应抵减税额
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[4]/td[9]/input'),  # 本期实际抵减税额
                    'endAmount': (FORM_GET, r'//tr[4]/td[11]/input'),  # 期末余额
                },
                # 分支机构预征缴纳税款
                'twoRow': {
                    'initialAmount': (FORM_INIT, r'//tr[5]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[5]/td[7]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[5]/td[9]/input'),
                    'endAmount': (FORM_GET, r'//tr[5]/td[11]/input'),
                },
                # 建筑服务预征缴纳税款
                'threeRow': {
                    'initialAmount': (FORM_INIT, r'//tr[6]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[6]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[6]/td[7]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[6]/td[9]/input'),
                    'endAmount': (FORM_GET, r'//tr[6]/td[11]/input'),
                },
                # 销售不动产预征缴纳税款
                'fourRow': {
                    'initialAmount': (FORM_INIT, r'//tr[7]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[7]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[7]/td[7]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[7]/td[9]/input'),
                    'endAmount': (FORM_GET, r'//tr[7]/td[11]/input'),
                },
                # 出租不动产预征缴纳税款
                'fiveRow': {
                    'initialAmount': (FORM_INIT, r'//tr[8]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[8]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[8]/td[7]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[8]/td[9]/input'),
                    'endAmount': (FORM_GET, r'//tr[8]/td[11]/input'),
                },
            },
            # 二、加计抵减情况
            'secondTable': {
                # 一般项目加计抵减额计算
                'oneRow': {
                    'initialAmount': (FORM_INIT, r'//tr[12]/td[4]/input'),  # 期初余额
                    'currentPeriodAmount': (FORM_FILL, r'//tr[12]/td[5]/input'),  # 本期发生额
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[12]/td[7]/input'),  # 本期调减额
                    'currentPeriodMayDeductedAmount': (FORM_GET, r'//tr[12]/td[9]/input'),  # 本期可抵减额
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[12]/td[10]/input'),  # 本期实际抵减额
                    'endAmount': (FORM_GET, r'//tr[12]/td[11]/input'),  # 期末余额
                },
                # 即征即退项目加计抵减额计算
                'twoRow': {
                    'initialAmount': (FORM_INIT, r'//tr[13]/td[4]/input'),  # 期初余额
                    'currentPeriodAmount': (FORM_FILL, r'//tr[13]/td[5]/input'),  # 本期发生额
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[13]/td[7]/input'),  # 本期调减额
                    'currentPeriodMayDeductedAmount': (FORM_GET, r'//tr[13]/td[9]/input'),  # 本期可抵减额
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[13]/td[10]/input'),  # 本期实际抵减额
                    'endAmount': (FORM_GET, r'//tr[13]/td[11]/input'),  # 期末余额
                },
                # 合计
                'threeRow': {
                    'initialAmount': (FORM_GET, r'//tr[14]/td[4]/input'),  # 期初余额
                    'currentPeriodAmount': (FORM_GET, r'//tr[14]/td[5]/input'),  # 本期发生额
                    'currentPeriodDeductedAmount': (FORM_GET, r'//tr[14]/td[7]/input'),  # 本期调减额
                    'currentPeriodMayDeductedAmount': (FORM_GET, r'//tr[14]/td[9]/input'),  # 本期可抵减额
                    'currentPeriodActualDeductionAmount': (FORM_GET, r'//tr[14]/td[10]/input'),  # 本期实际抵减额
                    'endAmount': (FORM_GET, r'//tr[14]/td[11]/input'),  # 期末余额
                }
            },
        },

        # 增值税 一般纳税人 附表5 表5删除20190430
        # '5008': {
        #     'firstTable': {
        #         'oneRow': {
        #             'startPeriodDeductibleImmovableTax': (FORM_FILL, r'//tr[3]/td[1]/input'),  # 期初待抵扣不动产进项税额
        #             'currentPeriodImmovableTaxIncrementAmount': (FORM_FILL, r'//tr[3]/td[2]/input'),  # 本期不动产进项税额增加额
        #             'currentPeriodDeductibleImmovableTax': (FORM_FILL, r'//tr[3]/td[3]/input'),  # 本期可抵扣不动产进项税额
        #             'currentPeriodInDeductedImmovableTax': (FORM_FILL, r'//tr[3]/td[4]/input'),  # 本期转入的待抵扣不动产进项税额
        #             'currentPeriodOutDeductedImmovableTax': (FORM_FILL, r'//tr[3]/td[5]/input'),  # 本期转出的待抵扣不动产进项税额
        #             'endDeductedImmovableTax': (FORM_FILL, r'//tr[3]/td[6]/input'),  # 期末待抵扣不动产进项税额
        #         },
        #     },
        # },

        # 增值税减免税申报表
        '5010': {
            'secondTable': {
                'project': (FORM_INIT, r'//tr[{tr_no}]/td[1]', 'select'),  # 减免代码
                'currentPeriodAmount': (FORM_INIT, r'//tr[{tr_no}]/td[5]/input'),  # 期初余额
                'currentPeriodProduceAmount': (FORM_FILL, r'//tr[{tr_no}]/td[6]/input'),  # 本期发生额
                'currentPeriodActualDeductionTax': (FORM_FILL, r'//tr[{tr_no}]/td[8]/input'),  # 本期实际抵减税额
            },
            'fourthTable': {
                'project': (FORM_INIT, r'//tr[{tr_no}]/td[1]', 'select'),  # 免税代码
                'freeTaxProjectSaleAmount': (FORM_FILL, r'//tr[{tr_no}]/td[5]/input'),  # # 免征增值税项目销售额
                'currentPeriodActualDeductionTax': (FORM_FILL, r'//tr[{tr_no}]/td[6]/input'),  # 免税销售额扣除项目本期实际扣除金额
                'freeTaxSaleAmountTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[8]/input'),  # 免税销售额对应的进项税额
                'freeTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[9]/input'),  # 免税额
            }
        },

        # 营改增税负分析测算明细表
        '5009': {
            'template': {
                'project': (FORM_FILL, r'//tr[{tr_no}]/td[1]/select'),  # 应税项目代码及名称
                'incrementTax': (FORM_FILL, r'//tr[{tr_no}]/td[5]/select'),  # 增值税税率或征收率
                'businessTax': (FORM_FILL, r'//tr[{tr_no}]/td[6]/select'),  # 营业税税率
                'zeroTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[7]/input'),  # 不含税销售额
                'serviceCurrentPeriodDeductionAmount': (FORM_FILL, r'//tr[{tr_no}]/td[10]/input'),
                # 服务、不动产和无形资产扣除项目本期实际扣除金额
                'currentPeriodAmount': (FORM_FILL, r'//tr[{tr_no}]/td[14]/input'),  # 期初余额
                'currentPeriodProduceAmount': (FORM_FILL, r'//tr[{tr_no}]/td[15]/input'),  # 本期发生额
                'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[{tr_no}]/td[17]/input'),  # 本期实际扣除金额
            }
        },
    }


# 增值税小规模纳税人
def get_local_added_small():
    return {
        '5004': {
            'firstTable': {
                # （一） 应征增值税不含税销售额（3%征收率）
                'oneRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[4]/td[3]/input'),  # 货物及劳务（本期数）
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[4]/td[4]/input'),  # 服务、不动产和无形资产（本期数）
                    'goodsLabourYear': (FORM_GET, r'//tr[4]/td[5]/input'),  # 货物及劳务(本年累计)
                    'serviceImmovableYear': (FORM_GET, r'//tr[4]/td[6]/input'),  # 服务、不动产和无形资产(本年累计)
                },

                # 税务机关代开的增值税专用发票不含税销售额
                'twoRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[5]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[5]/td[4]/input'),
                    'goodsLabourYear': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'serviceImmovableYear': (FORM_FILL, r'//tr[5]/td[6]/input'),
                },
                # 税控器具开具的普通发票不含税销售额
                'threeRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[6]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[6]/td[4]/input'),
                    'goodsLabourYear': (FORM_FILL, r'//tr[6]/td[5]/input'),
                    'serviceImmovableYear': (FORM_FILL, r'//tr[6]/td[6]/input'),
                },
                # （二）应征增值税不含税销售额（5%征收率）
                'fourRow': {
                    'goodsLabourMonth': (FORM_NO, r'//tr[7]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[7]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[7]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[7]/td[6]/input'),
                },
                # 税务机关代开的增值税专用发票不含税销售额
                'fiveRow': {
                    'goodsLabourMonth': (FORM_NO, r'//tr[8]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[8]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[8]/td[5]/input'),
                    'serviceImmovableYear': (FORM_FILL, r'//tr[8]/td[6]/input'),
                },
                # 税控器具开具的普通发票不含税销售额
                'sixRow': {
                    'goodsLabourMonth': (FORM_NO, r'//tr[9]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[9]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[9]/td[5]/input'),
                    'serviceImmovableYear': (FORM_FILL, r'//tr[9]/td[6]/input'),
                },
                # （三）销售使用过的固定资产不含税销售额
                'sevenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[10]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_NO, r'//tr[10]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[10]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[10]/td[6]/input'),
                },
                # 其中：税控器具开具的普通发票不含税销售额
                'eightRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[12]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_NO, r'//tr[12]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[12]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[12]/td[6]/input'),
                },
                # （四）免税销售额
                'nineRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[13]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[13]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[13]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[13]/td[6]/input'),
                },
                # 其中：小微企业免税销售额
                'tenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[14]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[14]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[14]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[14]/td[6]/input'),
                },
                # 未达起征点销售额
                'elevenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[15]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[15]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[15]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[15]/td[6]/input'),
                },
                # 其他免税销售额
                'twelveRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[16]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[16]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[16]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[16]/td[6]/input'),
                },
                # （五）出口免税销售额
                'thirteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[17]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[17]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[17]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[17]/td[6]/input'),
                },
                # 其中：税控器具开具的普通发票销售额
                'fourteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[18]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[18]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[18]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[18]/td[6]/input'),
                },
                # 核定销售额 2019.4.1
                'fourteenARow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[19]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[19]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[19]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[19]/td[6]/input'),
                },
            },
            'secondTable': {
                # 本期应纳税额
                'fifteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[20]/td[4]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[20]/td[5]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[20]/td[6]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[20]/td[7]/input'),
                },
                # 核定应纳税额 2019.4.1
                'fifteenARow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[21]/td[4]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[21]/td[5]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[21]/td[6]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[21]/td[7]/input'),
                },
                # 本期应纳税额减征额
                'sixteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[22]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[22]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[22]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[22]/td[6]/input'),
                },
                # 本期免税额
                'seventeenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[23]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[23]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[23]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[23]/td[6]/input'),
                },
                # 其中：小微企业免税额
                'eighteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[24]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[24]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[24]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[24]/td[6]/input'),
                },
                # 未达起征点免税额
                'nineteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[25]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[25]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[25]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[25]/td[6]/input'),
                },
                # 应纳税额合计
                'twentyRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[26]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[26]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[26]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[26]/td[6]/input'),
                },
                # 本期预缴税额
                'twentyOneRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[27]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[27]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[27]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[27]/td[6]/input'),
                },
                # 本期应补（退）税额
                'twentyTwoRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[28]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[28]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[28]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[28]/td[6]/input'),
                },
            },
            # 本期销售不动产的销售额
            'thirdTable': {
                'twentyThreeRow': {
                    'projectValue': (FORM_NO, r'//tr[1]/td[2]/input'),
                },
            },
        },
        '5005': {
            'firstTable': {
                # 应税行为（3%征收率）扣除额计算
                'twoRow': {
                    'keyOne': (FORM_FILL, r'//tr[4]/td[1]/input'),
                    'keyTwo': (FORM_FILL, r'//tr[4]/td[2]/input'),
                    'keyThree': (FORM_FILL, r'//tr[4]/td[3]/input'),
                    'keyFour': (FORM_FILL, r'//tr[4]/td[4]/input'),
                }
            },
            'secondTable': {
                # 应税行为（3%征收率）计税销售额计算
                'twoRow': {
                    'keyOne': (FORM_FILL, r'//tr[8]/td[1]/input'),
                    'keyTwo': (FORM_FILL, r'//tr[8]/td[2]/input'),
                    'keyThree': (FORM_FILL, r'//tr[8]/td[3]/input'),
                    'keyFour': (FORM_FILL, r'//tr[8]/td[4]/input'),
                }
            },
            'thirdTable': {
                # 应税行为（5%征收率）扣除额计算
                'twoRow': {
                    'keyOne': (FORM_FILL, r'//tr[12]/td[1]/input'),
                    'keyTwo': (FORM_FILL, r'//tr[12]/td[2]/input'),
                    'keyThree': (FORM_FILL, r'//tr[12]/td[3]/input'),
                    'keyFour': (FORM_FILL, r'//tr[12]/td[4]/input'),
                }
            },
            'fourthTable': {
                # 应税行为（5%征收率）计税销售额计算
                'twoRow': {
                    'keyOne': (FORM_FILL, r'//tr[16]/td[1]/input'),
                    'keyTwo': (FORM_FILL, r'//tr[16]/td[2]/input'),
                    'keyThree': (FORM_FILL, r'//tr[16]/td[3]/input'),
                    'keyFour': (FORM_FILL, r'//tr[16]/td[4]/input'),
                }
            },
        },
        # 增值税减免税申报表
        '5010': {
            'secondTable': {
                'project': (FORM_FILL, r'//tr[{tr_no}]/td[1]/select'),  # 减免代码
                'currentPeriodAmount': (FORM_FILL, r'//tr[{tr_no}]/td[3]/input'),  # 期初余额
                'currentPeriodProduceAmount': (FORM_FILL, r'//tr[{tr_no}]/td[4]/input'),  # 本期发生额
                'currentPeriodActualDeductionTax': (FORM_FILL, r'//tr[{tr_no}]/td[6]/input'),  # 本期实际抵减税额
            },
            'fourthTable': {
                'project': (FORM_FILL, r'//tr[{tr_no}]/td[1]/select'),  # 减免代码
                'currentPeriodAmount': (FORM_FILL, r'//tr[{tr_no}]/td[3]/input'),  # 免征增值税项目销售额
                'currentPeriodProduceAmount': (FORM_FILL, r'//tr[{tr_no}]/td[4]/input'),  # 免税销售额扣除项目本期实际扣除金额
                'currentPeriodActualDeductionTax': (FORM_FILL, r'//tr[{tr_no}]/td[6]/input'),  # 免税销售额对应的进项税额
            },
        },
    }


# 通用申报表
def get_commonly_table():
    return {
        'oneRow': {
            'taxable': (FORM_FILL, r'//tr[2]/td[7]/input'),  # 应税项
            'deduction': (FORM_FILL, r'//tr[2]/td[8]/input'),  # 减除项
            'reliefPropertyCode': (FORM_FILL, r'//tr[2]/td[14]/select'),  # 减免性质代码
            'currentTaxDeduction': (FORM_FILL, r'//tr[2]/td[15]/input'),  # 减免税（费）额
            'currentPeriodTaxPaid': (FORM_FILL, r'//tr[2]/td[16]/input'),  # 本期已缴税（费）额
        },
    }


# 通用申报表-残疾人就业保障金
def get_disabled_worker_table():
    return {
        'oneRow': {
            'taxable': (FORM_FILL, r'//tr[2]/td[7]/input'),  # 应税项
            'deduction': (FORM_FILL, r'//tr[2]/td[8]/input'),  # 减除项
            'reliefPropertyCode': (FORM_FILL, r'//tr[2]/td[14]/select'),  # 减免性质代码
            'currentTaxDeduction': (FORM_FILL, r'//tr[2]/td[15]/input'),  # 减免税（费）额
            'currentPeriodTaxPaid': (FORM_FILL, r'//tr[2]/td[20]/input'),  # 本期已缴税（费）额
        },
    }


# 通用申报表-水利建设基金
def get_water_build_table():
    return {
        'oneRow': {
            'taxableItems': (FORM_FILL, r'//tr[2]/td[7]/input'),  # 应税项
            'deductionItem': (FORM_FILL, r'//tr[2]/td[8]/input'),  # 减除项
            'reductionProperties': (FORM_FILL, r'//tr[2]/td[14]/select'),  # 减免性质代码
            'currentTaxDeduction': (FORM_FILL, r'//tr[2]/td[15]/input'),  # 减免税（费）额
            'amountTaxPaidCurrentPeriod': (FORM_FILL, r'//tr[2]/td[20]/input'),  # 本期已缴税（费）额
        },
    }


# 通用申报表-工会经费
def get_labour_union_table():
    return {
        'oneRow': {
            'taxableItems': (FORM_FILL, r'//tr[2]/td[7]/input'),  # 应税项
            'deductionItem': (FORM_FILL, r'//tr[2]/td[8]/input'),  # 减除项
            'reducedPropertyCode': (FORM_FILL, r'//tr[2]/td[14]/select'),  # 减免性质代码
            'currentTaxRelief': (FORM_FILL, r'//tr[2]/td[15]/input'),  # 减免税（费）额
            'amountOfTaxPaidCurrentPeriod': (FORM_FILL, r'//tr[2]/td[20]/input'),  # 本期已缴税（费）额
        },
    }


# 附加税表（行数不固定）
def get_additional_table():
    return {
        'template': {
            'project': (FORM_INIT, r'//tr[{tr_no}]/td[2]/input'),  # 征收项目
            'productName': (FORM_INIT, r'//tr[{tr_no}]/td[3]/input'),  # 征收品目
            'commonlyIncrementTax': (FORM_FILL, r'//tr[{tr_no}]/td[4]/input'),  # 一般增值税
            'exemptionTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[5]/input'),  # 免抵税额
            'tax': (FORM_INIT, r'//tr[{tr_no}]/td[9]/input'),  # 税率 （征收率）
            'reductionCode': (FORM_FILL, r'//tr[{tr_no}]/td[11]', 'select'),  # 减免性质代码
            'reductionAmount': (FORM_FILL, r'//tr[{tr_no}]/td[16]/input'),  # 减免额
            'currentPeriodPaidTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[17]/input'),  # 本期已缴税（费）额
        }
    }


# 印花税表（行数不固定）
def get_stamp_duty_table():
    return {
        'template': {
            'project': (FORM_INIT, r'//tr[{tr_no}]/td[1]/select'),
            'taxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[2]/input'),  # 计税金额或件数
            'approvedTaxBasis': (FORM_INIT, r'//tr[{tr_no}]/td[3]/input'),  # 核定依据
            'approvedRatio': (FORM_INIT, r'//tr[{tr_no}]/td[4]/input'),  # 核定比例
            'applicableTaxRate': (FORM_INIT, r'//tr[{tr_no}]/td[5]/input'),  # 适用税率
            'currentPeriodPaidTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[7]/input'),  # 本期已缴税额
            'reliefPropertyCode': (FORM_FILL, r'//tr[{tr_no}]/td[8]', 'select'),  # 减免性质代码
            'deductionTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[9]/input'),  # 减免税额
        },
    }


# 企业所得税A类
def corporate_income_tax_A():
    return {
        # 《A200000中华人民共和国企业所得税月（季）度预缴纳税申报表（A类，2018年版）》
        '8001': {
            'firstTable': {
                # 预缴方式
                'oneRow': {
                    # 按照实际利润额预缴
                    # 按照上一纳税年度应纳税所得额平均额预缴
                    # 按照税务机关确定的其他方法预缴
                    'projectValue': (FORM_NO, r'//tr[1]/td[2]/input'),
                },
                # 企业类型
                'twoRow': {
                    # 一般企业
                    # 跨地区经营汇总纳税企业
                    # 跨地区经营汇总纳税企业
                    'projectValue': (FORM_NO, r'//tr[2]/td[2]'),
                },
                'threeRow': {
                    # 一般企业
                    # 总机构
                    # 分支机构
                    'projectValue': (FORM_NO, r'//tr[2]/td[2]'),
                },
            },
            'secondTable': {
                # 营业收入
                'oneRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[6]/td[3]/input'),  # 本年累计金额
                },
                # 营业成本
                'twoRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[7]/td[3]/input'),  # 本年累计金额
                },
                # 利润总额
                'threeRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[8]/td[3]/input'),  # 本年累计金额
                },
                # 加：特定业务计算的应纳税所得额
                'fourRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[9]/td[3]/input'),  # 本年累计金额
                },
                # 减：不征税收入
                'fiveRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[10]/td[3]/input'),  # 本年累计金额
                },
                # 减：免税收入、减计收入、所得减免等优惠金额（填写A201010）
                'sixRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[11]/td[3]/input'),  # 本年累计金额
                },
                # 减：固定资产加速折旧（扣除）调减额（填写A201020）
                'sevenRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[12]/td[3]/input'),  # 本年累计金额
                },
                # 减：弥补以前年度亏损
                'eightRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[13]/td[3]/input'),  # 本年累计金额
                },
                # 实际利润额（3+4-5-6-7-8） \ 按照上一纳税年度应纳税所得额平均额确定的应纳税所得额
                'nineRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[14]/td[3]/input'),  # 本年累计金额
                },
                # 税率(25%)
                'tenRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[15]/td[3]/input'),  # 本年累计金额
                },
                # 应纳所得税额（9×10）
                'elevenRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[16]/td[3]/input'),  # 本年累计金额
                },
                # 减：减免所得税额（填写A201030）
                'twelveRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[17]/td[3]/input'),  # 本年累计金额
                },
                # 减：实际已缴纳所得税额
                'thirteenRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[18]/td[3]/input'),  # 本年累计金额
                },
                # 减：特定业务预缴（征）所得税额
                'fourteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[19]/td[3]/input'),  # 本年累计金额
                },
                # 本期应补（退）所得税额（11-12-13-14） \ 税务机关确定的本期应纳所得税额
                'fifteenRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[20]/td[3]/input'),  # 本年累计金额
                },
            },
            'thirdTable': {
                # 总机构填报  总机构本期分摊应补（退）所得税额（17+18+19）
                'oneRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[22]/td[3]/input'),  # 本年累计金额
                },
                # 总机构填报  其中：总机构分摊应补（退）所得税额（15×总机构分摊比例__%）
                'twoRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[23]/td[3]/input'),  # 本年累计金额
                },
                # 总机构填报  财政集中分配应补（退）所得税额（15×财政集中分配比例__%）
                'threeRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[24]/td[3]/input'),  # 本年累计金额
                },
                # 总机构填报  财政集中分配应补（退）所得税额（15×财政集中分配比例__%）
                'fourRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[25]/td[3]/input'),  # 本年累计金额
                },
                # 分支机构填报  分支机构本期分摊比例
                'fiveRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[26]/td[3]/input'),  # 本年累计金额
                },
                # 分支机构本期分摊应补（退）所得税额
                'sixRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[27]/td[3]/input'),  # 本年累计金额
                },
            },
            'fourthTable': {
                # 'oneRow': {
                #     'projectOne': (FORM_FILL, r'//tr[2]/td[2]/input'),  # 小型微利企业（radio）
                #     'projectTwo': (FORM_FILL, r'//tr[2]/td[4]/input'),  # 科技型中小企业（radio）
                # },
                # 'twoRow': {
                #     'projectOne': (FORM_FILL, r'//tr[3]/td[2]/input'),  # 高新技术企业（radio）
                #     'projectTwo': (FORM_FILL, r'//tr[3]/td[4]/input'),  # 技术入股递延纳税事项（radio）
                # },
                # 'threeRow': {
                #     'projectOne': (FORM_FILL, r'//tr[4]/td[2]/input'),  # 期末从业人数（text）
                # },
                'oneRow': {
                    'projectOne': (FORM_FILL, r'//tr[5]/td[2]/input'),  # 高新技术企业
                    'projectTwo': (FORM_FILL, r'//tr[5]/td[4]/input'),  # 科技型中小企业
                },

            },
            'fifthTable': {
                'twoRow': {
                    'projectOne': (FORM_FILL, r'//tr[6]/td[2]/input'),  # 技术入股递延纳税事项
                },
            },
            'sixthTable': {
                'oneRow': {
                    'projectOne': (FORM_FILL, r'//tr[8]/td[2]/input'),  # 季初从业人数
                    'projectTwo': (FORM_FILL, r'//tr[8]/td[4]/input'),  # 季末从业人数
                },
                'twoRow': {
                    'projectOne': (FORM_FILL, r'//tr[9]/td[2]/input'),  # 季初资产总额（万元）
                    'projectTwo': (FORM_FILL, r'//tr[9]/td[4]/input'),  # 季末资产总额（万元）
                },
                'threeRow': {
                    'projectOne': (FORM_FILL, r'//tr[10]/td[2]/input'),  # 国家限制或禁止行业
                    'projectTwo': (FORM_FILL, r'//tr[10]/td[4]/input'),  # 小型微利企业
                },
            },
        },
        # 《A201010免税收入、减计收入、所得减免等优惠明细表》
        '8002': {
            'firstTable': {
                # 一、免税收入（2+3+6+7+…+15）
                'oneRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[2]/td[3]/input'),
                },
                # （一）国债利息收入免征企业所得税
                'twoRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[3]/td[3]/input'),
                },
                # （二）符合条件的居民企业之间的股息、红利等权益性投资收益免征企业所得税
                'threeRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[4]/td[3]/input'),
                },
                # 其中：内地居民企业通过沪港通投资且连续持有H股满12个月取得的股息红利所得免征企业所得税
                'fourRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[5]/td[3]/input'),
                },
                # 内地居民企业通过深港通投资且连续持有H股满12个月取得的股息红利所得免征企业所得税
                'fiveRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[6]/td[3]/input'),
                },
                # （三）符合条件的非营利组织的收入免征企业所得税
                'sixRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[7]/td[3]/input'),
                },
                # （四）符合条件的非营利组织（科技企业孵化器）的收入免征企业所得税
                'sevenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[8]/td[3]/input'),
                },
                # （五）符合条件的非营利组织（国家大学科技园）的收入免征企业所得税
                'eightRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[9]/td[3]/input'),
                },
                # （六）中国清洁发展机制基金取得的收入免征企业所得税
                'nineRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[10]/td[3]/input'),
                },
                # （七）投资者从证券投资基金分配中取得的收入免征企业所得税
                'tenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[11]/td[3]/input'),
                },
                # （八）取得的地方政府债券利息收入免征企业所得税
                'elevenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[12]/td[3]/input'),
                },
                # （九）中国保险保障基金有限责任公司取得的保险保障基金等收入免征企业所得税
                'twelveRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[13]/td[3]/input'),
                },
                # （十）中国奥委会取得北京冬奥组委支付的收入免征企业所得税
                'thirteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[14]/td[3]/input'),
                },
                # （十一）中国残奥委会取得北京冬奥组委分期支付的收入免征企业所得税
                'fourteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[15]/td[3]/input'),
                },
                # （十二）其他
                'fifteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[16]/td[3]/input'),
                },
                # 二、减计收入（17+18+22+23）
                'sixteenRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[17]/td[3]/input'),
                },
                # （一）综合利用资源生产产品取得的收入在计算应纳税所得额时减计收入
                'seventeenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[18]/td[3]/input'),
                },
                # （二）金融、保险等机构取得的涉农利息、保费减计收入（19+20+21）
                'eighteenRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[19]/td[3]/input'),
                },
                # 1.金融机构取得的涉农贷款利息收入在计算应纳税所得额时减计收入
                'nineteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[20]/td[3]/input'),
                },
                # 2.保险机构取得的涉农保费收入在计算应纳税所得额时减计收入
                'twentyRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[21]/td[3]/input'),
                },
                # 3.小额贷款公司取得的农户小额贷款利息收入在计算应纳税所得额时减计收入
                'twentyOneRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[22]/td[3]/input'),
                },
                # （三）取得铁路债券利息收入减半征收企业所得税
                'twentyTwoRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[23]/td[3]/input'),
                },
                # （四）其他
                'twentyThreeRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[24]/td[3]/input'),
                },
                # 三、加计扣除（25+26+27+28）
                'twentyFourRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[25]/td[3]/input'),
                },
                # （一）开发新技术、新产品、新工艺发生的研究开发费用加计扣除
                'twentyFiveRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[26]/td[3]/input'),
                },
                # （二）科技型中小企业开发新技术、新产品、新工艺发生的研究开发费用加计扣除
                'twentySixRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[27]/td[3]/input'),
                },
                # （三）企业为获得创新性、创意性、突破性的产品进行创意设计活动而发生的相关费用加计扣除
                'twentySevenRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[28]/td[3]/input'),
                },
                # （四）安置残疾人员所支付的工资加计扣除
                'twentyEightRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[29]/td[3]/input'),
                },
                # 四、所得减免（30+33+34+35+36+37+38+39+40）
                'twentyNineRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[30]/td[3]/input'),
                },
                # （一）从事农、林、牧、渔业项目的所得减免征收企业所得税（31+32）
                'thirtyRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[31]/td[3]/input'),
                },
                # 1.免税项目
                'thirtyOneRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[32]/td[3]/input'),
                },
                # 2.减半征收项目
                'thirtyTwoRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[33]/td[3]/input'),
                },
                # （二）从事国家重点扶持的公共基础设施项目投资经营的所得定期减免企业所得税
                'thirtyThreeRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[34]/td[3]/input'),
                },
                # （三）从事符合条件的环境保护、节能节水项目的所得定期减免企业所得税
                'thirtyFourRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[35]/td[3]/input'),
                },
                # （四）符合条件的技术转让所得减免征收企业所得税
                'thirtyFiveRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[36]/td[3]/input'),
                },
                # （五）实施清洁发展机制项目的所得定期减免企业所得税
                'thirtySixRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[37]/td[3]/input'),
                },
                # （六）符合条件的节能服务公司实施合同能源管理项目的所得定期减免企业所得税
                'thirtySevenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[38]/td[3]/input'),
                },
                # （七）线宽小于130纳米的集成电路生产项目的所得减免企业所得税
                'thirtyEightRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[39]/td[3]/input'),
                },
                # （八）线宽小于65纳米或投资额超过150亿元的集成电路生产项目的所得减免企业所得税
                'thirtyNineRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[40]/td[3]/input'),
                },
                # （九）其他
                'fortyRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[41]/td[3]/input'),
                },
                # 合计（1+16+24+29）
                'fortyOneRow': {
                    'currentYearCumulativeAmount': (FORM_GET, r'//tr[42]/td[3]/input'),
                },
            },
        },
        # 《A201020固定资产加速折旧(扣除)优惠明细表》
        '8003': {
            'firstTable': {
                'oneRow': {
                    'project': '一、固定资产加速折旧（不含一次性扣除，2+3）',
                    'assetsOriginalAmount': (FORM_GET, r'//tr[4]/td[3]/input'),                    # 资产原值
                    'depreciationAmount': (FORM_GET, r'//tr[4]/td[4]/input'),                      # 账载折旧金额
                    'commonlyDepreciationAmount': (FORM_GET, r'//tr[4]/td[5]/input'),              # 按照税收一般规定计算的折旧金额
                    'accelerateDepreciationAmount': (FORM_GET, r'//tr[4]/td[6]/input'),            # 享受加速折旧优惠计算的折旧金额
                    'taxReductionAmount': (FORM_GET, r'//tr[4]/td[7]/input'),                      # 纳税调减金额
                    'accelerateDepreciationDiscountAmount': (FORM_GET, r'//tr[4]/td[8]/input'),    # 享受加速折旧优惠金额
                },
                'twoRow': {
                    'project': '（一）重要行业固定资产加速折旧',
                    'assetsOriginalAmount': (FORM_FILL, r'//tr[5]/td[3]/input'),
                    'depreciationAmount': (FORM_FILL, r'//tr[5]/td[4]/input'),
                    'commonlyDepreciationAmount': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'accelerateDepreciationAmount': (FORM_FILL, r'//tr[5]/td[6]/input'),
                    'taxReductionAmount': (FORM_FILL, r'//tr[5]/td[7]/input'),  # 纳税调减金额
                    'accelerateDepreciationDiscountAmount': (FORM_GET, r'//tr[5]/td[8]/input'),
                },
                'threeRow': {
                    'project': '（二）其他行业研发设备加速折旧',
                    'assetsOriginalAmount': (FORM_FILL, r'//tr[6]/td[3]/input'),
                    'depreciationAmount': (FORM_FILL, r'//tr[6]/td[4]/input'),
                    'commonlyDepreciationAmount': (FORM_FILL, r'//tr[6]/td[5]/input'),
                    'accelerateDepreciationAmount': (FORM_FILL, r'//tr[6]/td[6]/input'),
                    'taxReductionAmount': (FORM_FILL, r'//tr[6]/td[7]/input'),  # 纳税调减金额
                    'accelerateDepreciationDiscountAmount': (FORM_GET, r'//tr[6]/td[8]/input'),
                },
                'fourRow': {
                    'project': '二、固定资产一次性扣除',
                    'assetsOriginalAmount': (FORM_FILL, r'//tr[7]/td[3]/input'),
                    'depreciationAmount': (FORM_FILL, r'//tr[7]/td[4]/input'),
                    'commonlyDepreciationAmount': (FORM_FILL, r'//tr[7]/td[5]/input'),
                    'accelerateDepreciationAmount': (FORM_FILL, r'//tr[7]/td[6]/input'),
                    'taxReductionAmount': (FORM_FILL, r'//tr[7]/td[7]/input'),
                    'accelerateDepreciationDiscountAmount': (FORM_GET, r'//tr[7]/td[8]/input'),
                },
                'fiveRow': {
                    'project': '合计（1+4）',
                    'assetsOriginalAmount': (FORM_GET, r'//tr[8]/td[3]/input'),
                    'depreciationAmount': (FORM_GET, r'//tr[8]/td[4]/input'),
                    'commonlyDepreciationAmount': (FORM_GET, r'//tr[8]/td[5]/input'),
                    'accelerateDepreciationAmount': (FORM_GET, r'//tr[8]/td[6]/input'),
                    'taxReductionAmount': (FORM_GET, r'//tr[8]/td[7]/input'),
                    'accelerateDepreciationDiscountAmount': (FORM_GET, r'//tr[8]/td[8]/input'),
                },
            },
        },
        # 《A201030减免所得税优惠明细表》
        '8004': {
            'firstTable': {
                # 一、符合条件的小型微利企业减免企业所得税
                'oneRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[2]/td[3]/input'),
                },
                # 二、国家需要重点扶持的高新技术企业减按15%的税率征收企业所得税
                'twoRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[3]/td[3]/input'),
                },
                # 三、经济特区和上海浦东新区新设立的高新技术企业在区内取得的所得定期减免企业所得税
                'threeRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[4]/td[3]/input'),
                },
                # 四、受灾地区农村信用社免征企业所得税
                'fourRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[5]/td[3]/input'),
                },
                # 五、动漫企业自主开发、生产动漫产品定期减免企业所得税
                'fiveRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[6]/td[3]/input'),
                },
                # 六、线宽小于0.8微米（含）的集成电路生产企业减免企业所得税
                'sixRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[7]/td[3]/input'),
                },
                # 七、线宽小于0.25微米的集成电路生产企业减按15%税率征收企业所得税
                'sevenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[8]/td[3]/input'),
                },
                # 八、投资额超过80亿元的集成电路生产企业减按15%税率征收企业所得税
                'eightRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[9]/td[3]/input'),
                },
                # 九、线宽小于0.25微米的集成电路生产企业减免企业所得税
                'nineRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[10]/td[3]/input'),
                },
                # 十、投资额超过80亿元的集成电路生产企业减免企业所得税
                'tenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[11]/td[3]/input'),
                },
                # 十一、线宽小于130纳米的集成电路生产企业减免企业所得税
                'elevenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[12]/td[3]/input'),
                },
                # 十二、线宽小于65纳米或投资额超过150亿元的集成电路生产企业减免企业所得税
                'twelveRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[13]/td[3]/input'),
                },
                # 十三、新办集成电路设计企业减免企业所得税
                'thirteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[14]/td[3]/input'),
                },
                # 十四、国家规划布局内集成电路设计企业可减按10%的税率征收企业所得税
                'fourteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[15]/td[3]/input'),
                },
                # 十五、符合条件的软件企业减免企业所得税
                'fifteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[16]/td[3]/input'),
                },
                # 十六、国家规划布局内重点软件企业可减按10%的税率征收企业所得税
                'sixteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[17]/td[3]/input'),
                },
                # 十七、符合条件的集成电路封装、测试企业定期减免企业所得税
                'seventeenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[18]/td[3]/input'),
                },
                # 十八、符合条件的集成电路关键专用材料生产企业、集成电路专用设备生产企业定期减免企业所得税
                'eighteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[19]/td[3]/input'),
                },
                # 十九、经营性文化事业单位转制为企业的免征企业所得税
                'nineteenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[20]/td[3]/input'),
                },
                # 二十、符合条件的生产和装配伤残人员专门用品企业免征企业所得税
                'twentyRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[21]/td[3]/input'),
                },
                # 二十一、技术先进型服务企业减按15%的税率征收企业所得税
                'twentyOneRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[22]/td[3]/input'),
                },
                # 二十二、服务贸易类技术先进型服务企业减按15%的税率征收企业所得税
                'twentyTwoRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[23]/td[3]/input'),
                },
                # 二十三、设在西部地区的鼓励类产业企业减按15%的税率征收企业所得税
                'twentyThreeRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[24]/td[3]/input'),
                },
                # 二十四、新疆困难地区新办企业定期减免企业所得税
                'twentyFourRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[25]/td[3]/input'),
                },
                # 二十五、新疆喀什、霍尔果斯特殊经济开发区新办企业定期免征企业所得税
                'twentyFiveRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[26]/td[3]/input'),
                },
                # 二十六、广东横琴、福建平潭、深圳前海等地区的鼓励类产业企业减按15%税率征收企业所得
                'twentySixRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[27]/td[3]/input'),
                },
                # 二十七、北京冬奥组委、北京冬奥会测试赛赛事组委会免征企业所得税
                'twentySevenRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[28]/td[3]/input'),
                },
                # 二十八、其他
                'twentyEightRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[29]/td[3]/input'),
                },
                # 二十九、民族自治地方的自治机关对本民族自治地方的企业应缴纳的企业所得税中属于地方分享的部分减征或免征（  □ 免征    □ 减征:减征幅度____%  ）
                'twentyNineRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[30]/td[3]/input'),
                },
                # 合计(1+2+3+4+5+6+…+29)
                'thirtyRow': {
                    'currentYearCumulativeAmount': (FORM_FILL, r'//tr[31]/td[3]/input'),
                },
            },
        },
    }


# 企业所得税B类
def corporate_income_tax_B():
    return {
        'firstTable': {
            'oneRow': {
                'value': (FORM_FILL, r'//tr[1]/td[2]/span'),  # 确定征收方式
            }
        },
        'secondTable': {
            # 收入总额
            'oneRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[3]/td[3]/input'),  # 本年累计金额
            },
            # 减：不征税收入
            'twoRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[4]/td[3]/input'),  # 本年累计金额
            },
            # 减：免税收入（4+5+8+9）
            'threeRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[5]/td[3]/input'),  # 本年累计金额
            },
            # 国债利息收入免征企业所得税
            'fourRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[6]/td[3]/input'),  # 本年累计金额
            },
            # 符合条件的居民企业之间的股息、红利等权益性投资收益免征企业所得税
            'fiveRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[7]/td[3]/input'),  # 本年累计金额
            },
            # 其中： 通过沪港通投资且连续持有H股满12个月取得的股息红利所得免征企业所得税
            'sixRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[8]/td[3]/input'),  # 本年累计金额
            },
            # 通过深港通投资且连续持有H股满12个月取得的股息红利所得免征企业所得税
            'sevenRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[9]/td[3]/input'),  # 本年累计金额
            },
            # 投资者从证券投资基金分配中取得的收入免征企业所得税
            'eightRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[10]/td[3]/input'),  # 本年累计金额
            },
            # 取得的地方政府债券利息收入免征企业所得税
            'nineRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[11]/td[3]/input'),  # 本年累计金额
            },
            # 应税收入额（1-2-3） \ 成本费用总额
            'tenRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[12]/td[3]/input'),  # 本年累计金额
            },
            # 税务机关核定的应税所得率（%）
            'elevenRow': {
                'currentYearCumulativeAmount': (FORM_NO, r'//tr[13]/td[3]/input'),  # 本年累计金额
            },
            # 应纳税所得额（第10×11行） \ [第10行÷（1-第11行）×第11行]
            'twelveRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[14]/td[3]/input'),  # 本年累计金额
            },
            # 税率（25%）
            'thirteenRow': {
                'currentYearCumulativeAmount': (FORM_NO, r'//tr[15]/td[3]/input'),  # 本年累计金额
            },
            # 应纳所得税额（12×13）
            'fourteenRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[16]/td[3]/input'),  # 本年累计金额
            },
            # 减：符合条件的小型微利企业减免企业所得税
            'fifteenRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[17]/td[3]/input'),  # 本年累计金额
            },
            # 减：实际已缴纳所得税额
            'sixteenRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[18]/td[3]/input'),  # 本年累计金额
            },
            # 本期应补（退）所得税额（14-15-16） \ 税务机关核定本期应纳所得税额
            'seventeenRow': {
                'currentYearCumulativeAmount': (FORM_FILL, r'//tr[19]/td[3]/input'),  # 本年累计金额
            },
        },
        'thirdTable': {
            'oneRow': {
                'projectOne': (FORM_FILL, r'//tr[24]/td[2]/input'),  # 季初从业人数
                'projectTwo': (FORM_FILL, r'//tr[24]/td[4]/input'),  # 季末从业人数
            },
            'twoRow': {
                'projectOne': (FORM_FILL, r'//tr[25]/td[2]/input'),  # 季初资产总额（万元）
                'projectTwo': (FORM_FILL, r'//tr[25]/td[4]/input'),  # 季末资产总额（万元）
            },
        },
        'fourthTable': {
            'oneRow': {
                'projectOne': (FORM_FILL, r'//tr[26]/td[2]/input'),  # 国家限制或禁止行业
                'projectTwo': (FORM_FILL, r'//tr[26]/td[4]/input'),  # 小型微利企业
            },
        },
    }


def culture_table():
    return {
        # 《文化事业建设费申报表》（营改增）
        '10001': {
            'firstTable': {
                # 应征收入
                'oneRow': {
                    'numberMonths': (FORM_FILL, r'//tr[2]//td[4]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[2]//td[5]/input'),  # 本年累计
                },
                # 免征收入
                'twoRow': {
                    'numberMonths': (FORM_FILL, r'//tr[3]//td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[3]//td[4]/input'),  # 本年累计
                }
            },
            'secondTable': {
                # 减除项目期初金额
                'threeRow': {
                    'numberMonths': (FORM_FILL, r'//tr[4]/td[4]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_NO, r'//tr[4]/td[5]/input'),  # 本年累计
                },
                # 减除项目本期发生额
                'fourRow': {
                    'numberMonths': (FORM_FILL, r'//tr[5]//td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[5]/td[4]/input'),  # 本年累计
                },
                # 应征收入减除额
                'fiveRow': {
                    'numberMonths': (FORM_FILL, r'//tr[6]//td[4]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[6]/td[5]/input'),  # 本年累计
                },
                # 免征收入减除额
                'sixRow': {
                    'numberMonths': (FORM_FILL, r'//tr[7]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[7]/td[4]/input'),  # 本年累计
                },
                # 减除项目期末余额
                'sevenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[8]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'/tr[8]/td[3]/input'),  # 本年累计
                },
                # 计费销售额
                'eightRow': {
                    'numberMonths': (FORM_FILL, r'//tr[9]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[9]/td[4]/input'),  # 本年累计
                },
                # 费率
                'nineRow': {
                    'numberMonths': (FORM_FILL, r'//tr[10]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_NO, r'//tr[10]/td[4]/input'),  # 本年累计
                },
                # 应缴费额
                'tenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[11]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[11]/td[4]/input'),  # 本年累计
                },
            },
            'thirdTable': {
                # 期初未缴费额(多缴为负)
                'elevenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[12]/td[4]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_NO, r'//tr[12]/td[5]/input'),  # 本年累计
                },
                # 本期已缴费额
                'twelveRow': {
                    'numberMonths': (FORM_FILL, r'//tr[13]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[13]/td[4]/input'),  # 本年累计
                },
                # 其中：本期预缴费额
                'thirteenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[14]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[14]/td[4]/input'),  # 本年累计
                },
                # 本期缴纳上期费额
                'fourteenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[15]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[15]/td[4]/input'),  # 本年累计
                },
                # 本期缴纳欠费额
                'fifteenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[16]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//td[16]/td[4]/input'),  # 本年累计
                },
                # 期末未缴费额(多缴为负)
                'sixteenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[17]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[17]/td[4]/input'),  # 本年累计
                },
                #  其中：欠缴费额（≧0）
                'seventeenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[18]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_NO, r'//tr[18]/td[4]/input'),  # 本年累计
                },
                #  本期应补(退)费额
                'eighteenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[19]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_NO, r'//tr[19]/td[4]/input'),  # 本年累计
                },
                #  本期检查已补缴费额
                'nineteenRow': {
                    'numberMonths': (FORM_FILL, r'//tr[20]/td[3]/input'),  # 本月(期)数
                    'thisYearCumulative': (FORM_GET, r'//tr[20]/td[4]/input'),  # 本年累计
                },
            },
            # 永远荀泽否
            # 'fourthTable': {
            #     'firstTable': {
            #         'oneRow': {
            #             'whetherDeclareAgent': (FORM_FILL, r''),  # 是否选择代理申报
            #         },
            #     }
            # }
        },
        '10002': {
            # 应税服务扣除项目清单（行数不固定）
            'template': {
                'taxpayerIdentificationNumberIssuingParty': (FORM_FILL, r'//tr[{tr_no}]/td[2]/input'),  # 开票方纳税人识别号
                'nameInvoicingParty': (FORM_FILL, r'//tr[{tr_no}]/td[3]/input'),  # 开票方单位名称
                'serviceItemName': (FORM_FILL, r'//tr[{tr_no}]/td[4]/input'),  # 服务项目名称
                'proofType': (FORM_FILL, r'//tr[{tr_no}]/td[5]/select'),  # 凭证种类
                'certificateNumber': (FORM_FILL, r'//tr[{tr_no}]/td[6]/input'),  # 凭证号码
                'amount': (FORM_FILL, r'//tr[{tr_no}]/td[7]/input'),  # 金额
            },
        },
    }

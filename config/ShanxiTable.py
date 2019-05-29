FORM_FILL = 1  # 向表格中填充
FORM_GET = 2  # 从表格中获取
FORM_NO = 3  # 不操作


# 财务报表 小企业会计准则
def get_local_finance_small():
    return {
        'zichanfuzhaibiao': {
            '10010000': {
                'AssetTotal': (FORM_NO, r'//tr[2]/td[3]/input'),  # 流动资产
                'AssetInitial': (FORM_NO, r'//tr[2]/td[4]/input'),  # 流动资产
                'DebtsTotal': (FORM_NO, r'//tr[2]/td[7]/input'),  # 流动负债
                'DebtsInitial': (FORM_NO, r'//tr[2]/td[8]/input'),  # 流动负债
            },
            '10010010': {
                'AssetTotal': (FORM_FILL, r'//tr[3]/td[3]/input'),  # 货币资金 期末余额
                'AssetInitial': (FORM_GET, r'//tr[3]/td[4]/input'),  # 货币资金 年初余额
                'DebtsTotal': (FORM_FILL, r'//tr[3]/td[7]/input'),  # 短期借款 期末余额
                'DebtsInitial': (FORM_GET, r'//tr[3]/td[8]/input'),  # 短期借款 年初余额
            },
            '10010020': {
                'AssetTotal': (FORM_FILL, r'//tr[4]/td[3]/input'),  # 短期投资
                'AssetInitial': (FORM_GET, r'//tr[4]/td[4]/input'),  # 短期投资
                'DebtsTotal': (FORM_FILL, r'//tr[4]/td[7]/input'),  # 应付票据
                'DebtsInitial': (FORM_GET, r'//tr[4]/td[8]/input'),  # 应付票据
            },
            '10010030': {
                'AssetTotal': (FORM_FILL, r'//tr[5]/td[3]/input'),  # 应收票据
                'AssetInitial': (FORM_GET, r'//tr[5]/td[4]/input'),  # 应收票据
                'DebtsTotal': (FORM_FILL, r'//tr[5]/td[7]/input'),  # 应付账款
                'DebtsInitial': (FORM_GET, r'//tr[5]/td[8]/input'),  # 应付账款
            },
            '10010040': {
                'AssetTotal': (FORM_FILL, r'//tr[6]/td[3]/input'),  # 应收账款
                'AssetInitial': (FORM_GET, r'//tr[6]/td[4]/input'),  # 应收账款
                'DebtsTotal': (FORM_FILL, r'//tr[6]/td[7]/input'),  # 预收账款
                'DebtsInitial': (FORM_GET, r'//tr[6]/td[8]/input'),  # 预收账款
            },
            '10010050': {
                'AssetTotal': (FORM_FILL, r'//tr[7]/td[3]/input'),  # 预付账款
                'AssetInitial': (FORM_GET, r'//tr[7]/td[4]/input'),  # 预付账款
                'DebtsTotal': (FORM_FILL, r'//tr[7]/td[7]/input'),  # 应付职工薪酬
                'DebtsInitial': (FORM_GET, r'//tr[7]/td[8]/input'),  # 应付职工薪酬
            },
            '10010060': {
                'AssetTotal': (FORM_FILL, r'//tr[8]/td[3]/input'),  # 应收股利
                'AssetInitial': (FORM_GET, r'//tr[8]/td[4]/input'),  # 应收股利
                'DebtsTotal': (FORM_FILL, r'//tr[8]/td[7]/input'),  # 应交税费
                'DebtsInitial': (FORM_GET, r'//tr[8]/td[8]/input'),  # 应交税费
            },
            '10010070': {
                'AssetTotal': (FORM_FILL, r'//tr[9]/td[3]/input'),  # 应收利息
                'AssetInitial': (FORM_GET, r'//tr[9]/td[4]/input'),  # 应收利息
                'DebtsTotal': (FORM_FILL, r'//tr[9]/td[7]/input'),  # 应付利息
                'DebtsInitial': (FORM_GET, r'//tr[9]/td[8]/input'),  # 应付利息
            },
            '10010080': {
                'AssetTotal': (FORM_FILL, r'//tr[10]/td[3]/input'),  # 其他应收款
                'AssetInitial': (FORM_GET, r'//tr[10]/td[4]/input'),  # 其他应收款
                'DebtsTotal': (FORM_FILL, r'//tr[10]/td[7]/input'),  # 应付利润
                'DebtsInitial': (FORM_GET, r'//tr[10]/td[8]/input'),  # 应付利润
            },
            '10010090': {
                'AssetTotal': (FORM_FILL, r'//tr[11]/td[3]/input'),  # 存货
                'AssetInitial': (FORM_GET, r'//tr[11]/td[4]/input'),  # 存货
                'DebtsTotal': (FORM_FILL, r'//tr[11]/td[7]/input'),  # 其他应付款
                'DebtsInitial': (FORM_GET, r'//tr[11]/td[8]/input'),  # 其他应付款
            },
            '10010100': {
                'AssetTotal': (FORM_FILL, r'//tr[12]/td[3]/input'),  # 其中：原材料
                'AssetInitial': (FORM_GET, r'//tr[12]/td[4]/input'),  # 其中：原材料
            },
            '10010110': {
                'AssetTotal': (FORM_FILL, r'//tr[13]/td[3]/input'),  # 在产品
                'AssetInitial': (FORM_GET, r'//tr[13]/td[4]/input'),  # 在产品
            },
            '10010120': {
                'AssetTotal': (FORM_FILL, r'//tr[14]/td[3]/input'),  # 库存商品
                'AssetInitial': (FORM_GET, r'//tr[14]/td[4]/input'),  # 库存商品
            },
            '10010130': {
                'AssetTotal': (FORM_FILL, r'//tr[15]/td[3]/input'),  # 周转材料
                'AssetInitial': (FORM_GET, r'//tr[15]/td[4]/input'),  # 周转材料
            },
            '10010140': {
                'AssetTotal': (FORM_FILL, r'//tr[16]/td[3]/input'),  # 其他流动资产
                'AssetInitial': (FORM_GET, r'//tr[16]/td[4]/input'),  # 其他流动资产
                'DebtsTotal': (FORM_FILL, r'//tr[12]/td[7]/input'),  # 其他流动负债
                'DebtsInitial': (FORM_GET, r'//tr[12]/td[8]/input'),  # 其他流动负债
            },
            '10010150': {
                'AssetTotal': (FORM_GET, r'//tr[17]/td[3]/input'),  # 流动资产合计
                'AssetInitial': (FORM_GET, r'//tr[17]/td[4]/input'),  # 流动资产合计
                'DebtsTotal': (FORM_GET, r'//tr[13]/td[7]/input'),  # 流动负债合计
                'DebtsInitial': (FORM_GET, r'//tr[13]/td[8]/input'),  # 流动负债合计
            },
            '10010160': {
                'AssetTotal': (FORM_NO, r'//tr[18]/td[3]/input'),  # 非流动资产
                'AssetInitial': (FORM_NO, r'//tr[18]/td[4]/input'),  # 非流动资产
                'DebtsTotal': (FORM_NO, r'//tr[14]/td[7]/input'),  # 非流动负债
                'DebtsInitial': (FORM_NO, r'//tr[14]/td[8]/input'),  # 非流动负债
            },
            '10010170': {
                'AssetTotal': (FORM_FILL, r'//tr[19]/td[3]/input'),  # 长期债券投资
                'AssetInitial': (FORM_GET, r'//tr[19]/td[4]/input'),  # 长期债券投资
                'DebtsTotal': (FORM_FILL, r'//tr[15]/td[7]/input'),  # 长期借款
                'DebtsInitial': (FORM_GET, r'//tr[15]/td[8]/input'),  # 长期借款
            },
            '10010180': {
                'AssetTotal': (FORM_FILL, r'//tr[20]/td[3]/input'),  # 长期股权投资
                'AssetInitial': (FORM_GET, r'//tr[20]/td[4]/input'),  # 长期股权投资
                'DebtsTotal': (FORM_FILL, r'//tr[16]/td[7]/input'),  # 长期应付款
                'DebtsInitial': (FORM_GET, r'//tr[16]/td[8]/input'),  # 长期应付款
            },
            '10010190': {
                'AssetTotal': (FORM_FILL, r'//tr[21]/td[3]/input'),  # 固定资产原价
                'AssetInitial': (FORM_GET, r'//tr[21]/td[4]/input'),  # 固定资产原价
                'DebtsTotal': (FORM_FILL, r'//tr[17]/td[7]/input'),  # 递延收益
                'DebtsInitial': (FORM_GET, r'//tr[17]/td[8]/input'),  # 递延收益
            },
            '10010200': {
                'AssetTotal': (FORM_FILL, r'//tr[22]/td[3]/input'),  # 减：累计折旧
                'AssetInitial': (FORM_GET, r'//tr[22]/td[4]/input'),  # 减：累计折旧
                'DebtsTotal': (FORM_FILL, r'//tr[18]/td[7]/input'),  # 其他非流动负债
                'DebtsInitial': (FORM_GET, r'//tr[18]/td[8]/input'),  # 其他非流动负债
            },
            '10010210': {
                'AssetTotal': (FORM_NO, r'//tr[23]/td[3]/input'),  # 固定资产账面价值
                'AssetInitial': (FORM_NO, r'//tr[23]/td[4]/input'),  # 固定资产账面价值
                'DebtsTotal': (FORM_NO, r'//tr[19]/td[7]/input'),  # 非流动负债合计
                'DebtsInitial': (FORM_NO, r'//tr[19]/td[8]/input'),  # 非流动负债合计
            },
            '10010220': {
                'AssetTotal': (FORM_FILL, r'//tr[24]/td[3]/input'),  # 在建工程
                'AssetInitial': (FORM_GET, r'//tr[24]/td[4]/input'),  # 在建工程
                'DebtsTotal': (FORM_GET, r'//tr[20]/td[7]/input'),  # 负债合计
                'DebtsInitial': (FORM_GET, r'//tr[20]/td[8]/input'),  # 负债合计
            },
            '10010230': {
                'AssetTotal': (FORM_FILL, r'//tr[25]/td[3]/input'),  # 工程物资
                'AssetInitial': (FORM_GET, r'//tr[25]/td[4]/input'),  # 工程物资
            },
            '10010240': {
                'AssetTotal': (FORM_FILL, r'//tr[26]/td[3]/input'),  # 固定资产清理
                'AssetInitial': (FORM_GET, r'//tr[26]/td[4]/input'),  # 固定资产清理
            },
            '10010250': {
                'AssetTotal': (FORM_FILL, r'//tr[27]/td[3]/input'),  # 生产性生物资产
                'AssetInitial': (FORM_GET, r'//tr[27]/td[4]/input'),  # 生产性生物资产
                'DebtsTotal': (FORM_NO, r'//tr[27]/td[7]/input'),  # 所有者权益（或股东权益）
                'DebtsInitial': (FORM_NO, r'//tr[27]/td[8]/input'),  # 所有者权益（或股东权益）
            },
            '10010260': {
                'AssetTotal': (FORM_FILL, r'//tr[28]/td[3]/input'),  # 无形资产
                'AssetInitial': (FORM_GET, r'//tr[28]/td[4]/input'),  # 无形资产
                'DebtsTotal': (FORM_FILL, r'//tr[28]/td[7]/input'),  # 实收资本（或股本）
                'DebtsInitial': (FORM_GET, r'//tr[28]/td[8]/input'),  # 实收资本（或股本）
            },
            '10010270': {
                'AssetTotal': (FORM_FILL, r'//tr[29]/td[3]/input'),  # 开发支出
                'AssetInitial': (FORM_GET, r'//tr[29]/td[4]/input'),  # 开发支出
                'DebtsTotal': (FORM_FILL, r'//tr[29]/td[7]/input'),  # 资本公积
                'DebtsInitial': (FORM_GET, r'//tr[29]/td[8]/input'),  # 资本公积
            },
            '10010280': {
                'AssetTotal': (FORM_FILL, r'//tr[30]/td[3]/input'),  # 长期待摊费用
                'AssetInitial': (FORM_GET, r'//tr[30]/td[4]/input'),  # 长期待摊费用
                'DebtsTotal': (FORM_FILL, r'//tr[30]/td[7]/input'),  # 盈余公积
                'DebtsInitial': (FORM_GET, r'//tr[30]/td[8]/input'),  # 盈余公积
            },
            '10010290': {
                'AssetTotal': (FORM_FILL, r'//tr[31]/td[3]/input'),  # 其他非流动资产
                'AssetInitial': (FORM_GET, r'//tr[31]/td[4]/input'),  # 其他非流动资产
                'DebtsTotal': (FORM_FILL, r'//tr[31]/td[7]/input'),  # 未分配利润
                'DebtsInitial': (FORM_GET, r'//tr[31]/td[8]/input'),  # 未分配利润
            },
            '10010300': {
                'AssetTotal': (FORM_GET, r'//tr[32]/td[3]/input'),  # 非流动资产合计
                'AssetInitial': (FORM_GET, r'//tr[32]/td[4]/input'),  # 非流动资产合计
                'DebtsTotal': (FORM_GET, r'//tr[32]/td[7]/input'),  # 所有者权益（或股东权益）合计
                'DebtsInitial': (FORM_GET, r'//tr[32]/td[8]/input'),  # 所有者权益（或股东权益）合计
            },
            '10010310': {
                'AssetTotal': (FORM_GET, r'//tr[33]/td[3]/input'),  # 资产合计
                'AssetInitial': (FORM_GET, r'//tr[33]/td[4]/input'),  # 资产合计
                'DebtsTotal': (FORM_GET, r'//tr[33]/td[7]/input'),  # 负债和所有者权益（或股东权益）总计
                'DebtsInitial': (FORM_GET, r'//tr[33]/td[8]/input'),  # 负债和所有者权益（或股东权益）总计
            },
        },
        'lirunbiao': {
            # 一、营业收入
            '10020000': {
                'Amount': (FORM_FILL, r'//tr[2]/td[3]/input'),  # 本月金额
                'YearTotal': (FORM_GET, r'//tr[2]/td[4]/input'),  # 本年累计金额
            },
            # 减：营业成本
            '10020010': {
                'Amount': (FORM_FILL, r'//tr[3]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[3]/td[4]/input'),
            },
            # 税金及附加
            '10020020': {
                'Amount': (FORM_FILL, r'//tr[4]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[4]/td[4]/input'),
            },
            # 其中：消费税
            '10020030': {
                'Amount': (FORM_FILL, r'//tr[5]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[5]/td[4]/input'),
            },
            # 营业税
            '10020040': {
                'Amount': (FORM_FILL, r'//tr[6]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[6]/td[4]/input'),
            },
            # 城市维护建设税
            '10020050': {
                'Amount': (FORM_FILL, r'//tr[7]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[7]/td[4]/input'),
            },
            # 资源税
            '10020060': {
                'Amount': (FORM_FILL, r'//tr[8]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[8]/td[4]/input'),
            },
            # 土地增值税
            '10020070': {
                'Amount': (FORM_FILL, r'//tr[9]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[9]/td[4]/input'),
            },
            # 城镇土地使用税、房产税、车船税、印花税
            '10020080': {
                'Amount': (FORM_FILL, r'//tr[10]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[10]/td[4]/input'),
            },
            # 教育费附加、矿产资源补偿费、排污费
            '10020090': {
                'Amount': (FORM_FILL, r'//tr[11]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[11]/td[4]/input'),
            },
            # 销售费用
            '10020100': {
                'Amount': (FORM_FILL, r'//tr[12]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[12]/td[4]/input'),
            },
            # 其中：商品维修费
            '10020110': {
                'Amount': (FORM_FILL, r'//tr[13]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[13]/td[4]/input'),
            },
            # 广告费和业务宣传费
            '10020120': {
                'Amount': (FORM_FILL, r'//tr[14]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[14]/td[4]/input'),
            },
            # 管理费用
            '10020130': {
                'Amount': (FORM_FILL, r'//tr[15]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[15]/td[4]/input'),
            },
            # 其中：开办费
            '10020140': {
                'Amount': (FORM_FILL, r'//tr[16]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[16]/td[4]/input'),
            },
            # 业务招待费
            '10020150': {
                'Amount': (FORM_FILL, r'//tr[17]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[17]/td[4]/input'),
            },
            # 研究费用
            '10020160': {
                'Amount': (FORM_FILL, r'//tr[18]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[18]/td[4]/input'),
            },
            # 财务费用
            '10020170': {
                'Amount': (FORM_FILL, r'//tr[19]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[19]/td[4]/input'),
            },
            # 其中：利息费用（收入以－号填列）
            '10020180': {
                'Amount': (FORM_FILL, r'//tr[20]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[20]/td[4]/input'),
            },
            # 加：投资收益（亏损以－号填列）
            '10020190': {
                'Amount': (FORM_FILL, r'//tr[21]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[21]/td[4]/input'),
            },
            # 加：投资收益（亏损以－号填列）
            '10020200': {
                'Amount': (FORM_GET, r'//tr[22]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[22]/td[4]/input'),
            },
            #  加：营业外收入
            '10020210': {
                'Amount': (FORM_FILL, r'//tr[23]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[23]/td[4]/input'),
            },
            #  其中：政府补助
            '10020220': {
                'Amount': (FORM_FILL, r'//tr[24]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[24]/td[4]/input'),
            },
            #  减：营业外支出
            '10020230': {
                'Amount': (FORM_FILL, r'//tr[25]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[25]/td[4]/input'),
            },
            #  其中：坏账损失
            '10020240': {
                'Amount': (FORM_FILL, r'//tr[26]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[26]/td[4]/input'),
            },
            #  无法收回的长期债券投资损失
            '10020250': {
                'Amount': (FORM_FILL, r'//tr[27]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[27]/td[4]/input'),
            },
            #  无法收回的长期股权投资损失
            '10020260': {
                'Amount': (FORM_FILL, r'//tr[28]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[28]/td[4]/input'),
            },
            # 自然灾害等不可抗力因素造成的损失
            '10020270': {
                'Amount': (FORM_FILL, r'//tr[29]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[29]/td[4]/input'),
            },
            #  税收滞纳金
            '10020280': {
                'Amount': (FORM_FILL, r'//tr[30]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[30]/td[4]/input'),
            },
            #  三、利润总额（亏损总额以－号填列）
            '10020290': {
                'Amount': (FORM_GET, r'//tr[31]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[31]/td[4]/input'),
            },
            #  减：所得税费用
            '10020300': {
                'Amount': (FORM_FILL, r'//tr[32]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[32]/td[4]/input'),
            },
            # 四、净利润（净亏损以－号填列）
            '10020310': {
                'Amount': (FORM_GET, r'//tr[33]/td[3]/input'),
                'YearTotal': (FORM_GET, r'//tr[33]/td[4]/input'),
            },
        },
        'xianjinliuliangbiao': {
            # 一、经营活动产生的现金流量
            '10030000': {
                'Amount': (FORM_NO, r'//tr[2]/td[3]/input'),  # 本月金额
                'InitalAmount': (FORM_NO, r'//tr[2]/td[4]/input'),  # 本年累计金额
            },
            # 销售产成品、商品、提供劳务收到的现金
            '10030010': {
                'Amount': (FORM_FILL, r'//tr[3]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[3]/td[4]/input'),
            },
            # 收到其他与经营活动有关的现金
            '10030020': {
                'Amount': (FORM_FILL, r'//tr[4]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[4]/td[4]/input'),
            },
            # 购买原材料、商品、接受劳务支付的现金
            '10030030': {
                'Amount': (FORM_FILL, r'//tr[5]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[5]/td[4]/input'),
            },
            # 支付的职工薪酬
            '10030040': {
                'Amount': (FORM_FILL, r'//tr[6]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[6]/td[4]/input'),
            },
            # 支付的税费
            '10030050': {
                'Amount': (FORM_FILL, r'//tr[7]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[7]/td[4]/input'),
            },
            # 支付其他与经营活动有关的现金
            '10030060': {
                'Amount': (FORM_FILL, r'//tr[8]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[8]/td[4]/input'),
            },
            # 经营活动产生的现金流量净额
            '10030070': {
                'Amount': (FORM_GET, r'//tr[9]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[9]/td[4]/input'),
            },
            '10030080': {
                'Amount': (FORM_NO, r'//tr[10]/td[3]/input'),
                'InitalAmount': (FORM_NO, r'//tr[10]/td[4]/input'),
            },
            # 收回短期投资、长期债券投资和长期股权投资收到的现金
            '10030090': {
                'Amount': (FORM_FILL, r'//tr[11]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[11]/td[4]/input'),
            },
            # 取得投资收益收到的现金
            '10030100': {
                'Amount': (FORM_FILL, r'//tr[12]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[12]/td[4]/input'),
            },
            # 处置固定资产、无形资产和其他非流动资产收回的现金净额
            '10030110': {
                'Amount': (FORM_FILL, r'//tr[13]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[13]/td[4]/input'),
            },
            # 短期投资、长期债券投资和长期股权投资支付的现金
            '10030120': {
                'Amount': (FORM_FILL, r'//tr[14]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[14]/td[4]/input'),
            },
            # 购建固定资产、无形资产和其他非流动资产支付的现金
            '10030130': {
                'Amount': (FORM_FILL, r'//tr[15]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[15]/td[4]/input'),
            },
            # 投资活动产生的现金流量净额
            '10030140': {
                'Amount': (FORM_GET, r'//tr[16]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[16]/td[4]/input'),
            },
            # 三、筹资活动产生的现金流量：
            '10030150': {
                'Amount': (FORM_NO, r'//tr[17]/td[3]/input'),
                'InitalAmount': (FORM_NO, r'//tr[17]/td[4]/input'),
            },
            # 取得借款收到的现金
            '10030160': {
                'Amount': (FORM_FILL, r'//tr[18]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[18]/td[4]/input'),
            },
            # 吸收投资者投资收到的现金
            '10030170': {
                'Amount': (FORM_FILL, r'//tr[19]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[19]/td[4]/input'),
            },
            # 偿还借款本金支付的现金
            '10030180': {
                'Amount': (FORM_FILL, r'//tr[20]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[20]/td[4]/input'),
            },
            # 偿还借款利息支付的现金
            '10030190': {
                'Amount': (FORM_FILL, r'//tr[21]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[21]/td[4]/input'),
            },
            # 分配利润支付的现金
            '10030200': {
                'Amount': (FORM_FILL, r'//tr[22]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[22]/td[4]/input'),
            },
            # 筹资活动产生的现金流量净额
            '10030210': {
                'Amount': (FORM_GET, r'//tr[23]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[23]/td[4]/input'),
            },
            # 四、现金净增加额
            '10030220': {
                'Amount': (FORM_GET, r'//tr[24]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[24]/td[4]/input'),
            },
            # 加：期初现金余额
            '10030230': {
                'Amount': (FORM_FILL, r'//tr[25]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[25]/td[4]/input'),
            },
            # 五、期末现金余额
            '10030240': {
                'Amount': (FORM_GET, r'//tr[26]/td[3]/input'),
                'InitalAmount': (FORM_GET, r'//tr[26]/td[4]/input'),
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
                    'commonlyMonth': (FORM_FILL, r'//tr[3]/td[4]/input'),  # 一般项目 本月
                    'commonlyYear': (FORM_GET, r'//tr[3]/td[5]/input'),  # 一般项目 本年
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[3]/td[6]/input'),  # 即征即退项目 本月
                    'signAndRetreatYear': (FORM_GET, r'//tr[3]/td[7]/input'),  # 即征即退项目 本年
                },
                # 其中：应税货物销售额
                'twoRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[4]/td[3]/input'),  # 一般项目 本月
                    'commonlyYear': (FORM_GET, r'//tr[4]/td[4]/input'),  # 一般项目 本年
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[4]/td[5]/input'),  # 即征即退项目 本月
                    'signAndRetreatYear': (FORM_GET, r'//tr[4]/td[6]/input'),  # 即征即退项目 本年
                },
                # 应税劳务销售额
                'threeRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[5]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[5]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[5]/td[6]/input'),
                },
                # 纳税检查调整的销售额
                'fourRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[6]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[6]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[6]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[6]/td[6]/input'),
                },
                # （二）按简易办法计税销售额
                'fiveRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[7]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[7]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[7]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[7]/td[6]/input'),
                },
                # 其中：纳税检查调整的销售额
                'sixRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[8]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[8]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[8]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[8]/td[6]/input'),
                },
                # （三）免、抵、退办法出口销售额
                'sevenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[9]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[9]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[9]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[9]/td[6]/input'),
                },
                # （四）免税销售额
                'eightRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[10]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[10]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[10]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[10]/td[6]/input'),
                },
                # 其中：免税货物销售额
                'nineRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[11]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[11]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[11]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[11]/td[6]/input'),
                },
                # 免税劳务销售额
                'tenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[12]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[12]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[12]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[12]/td[6]/input'),
                },
            },
            'secondTable': {
                # 销项税额
                'elevenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[13]/td[4]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[13]/td[5]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[13]/td[6]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[13]/td[7]/input'),
                },
                # 进项税额
                'twelveRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[14]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[14]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[14]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[14]/td[6]/input'),
                },
                # 上期留抵税额
                'thirteenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[15]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[15]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[15]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[15]/td[6]/input'),
                },
                # 进项税额转出
                'fourteenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[16]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[16]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[16]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[16]/td[6]/input'),
                },
                # 免、抵、退应退税额
                'fifteenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[17]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[17]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[17]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[17]/td[6]/input'),
                },
                # 按适用税率计算的纳税检查应补缴税额
                'sixteenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[18]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[18]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[18]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[18]/td[6]/input'),
                },
                # 应抵扣税额合计
                'seventeenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[19]/td[3]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[19]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[19]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[19]/td[6]/input'),
                },
                # 实际抵扣税额
                'eighteenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[20]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[20]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[20]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[20]/td[6]/input'),
                },
                # 应纳税额
                'nineteenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[21]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[21]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[21]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[21]/td[6]/input'),
                },
                # 期末留抵税额
                'twentyRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[22]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[22]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[22]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[22]/td[6]/input'),
                },
                # 简易计税办法计算的应纳税额
                'twentyOneRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[23]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[23]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[23]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[23]/td[6]/input'),
                },
                # 按简易计税办法计算的纳税检查应补缴税额
                'twentyTwoRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[24]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[24]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[24]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[24]/td[6]/input'),
                },
                # 应纳税额减征额
                'twentyThreeRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[25]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[25]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[25]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[25]/td[6]/input'),
                },
                # 应纳税额合计
                'twentyFourRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[26]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[26]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[26]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[26]/td[6]/input'),
                },
            },
            'thirdTable': {
                # 期初未缴税额（多缴为负数）
                'twentyFiveRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[27]/td[4]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[27]/td[5]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[27]/td[6]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[27]/td[7]/input'),
                },
                # 实收出口开具专用缴款书退税额
                'twentySixRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[28]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[28]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[28]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[28]/td[6]/input'),
                },
                # 本期已缴税额
                'twentySevenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[29]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[29]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[29]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[29]/td[6]/input'),
                },
                # ①分次预缴税额
                'twentyEightRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[30]/td[3]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[30]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[30]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[30]/td[6]/input'),
                },
                # ②出口开具专用缴款书预缴税额
                'twentyNineRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[31]/td[3]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[31]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[31]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[31]/td[6]/input'),
                },
                # ③本期缴纳上期应纳税额
                'thirtyRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[32]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[32]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[32]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[32]/td[6]/input'),
                },
                # ④本期缴纳欠缴税额
                'thirtyOneRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[33]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[33]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[33]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[33]/td[6]/input'),
                },
                # 期末未缴税额（多缴为负数）
                'thirtyTwoRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[34]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[34]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[34]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[34]/td[6]/input'),
                },
                # 其中：欠缴税额（≥0）
                'thirtyThreeRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[35]/td[3]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[35]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[35]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[35]/td[6]/input'),
                },
                # 本期应补(退)税额
                'thirtyFourRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[36]/td[3]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[36]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[36]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[36]/td[6]/input'),
                },
                # 即征即退实际退税额
                'thirtyFiveRow': {
                    'commonlyMonth': (FORM_NO, r'//tr[37]/td[3]/input'),
                    'commonlyYear': (FORM_NO, r'//tr[37]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_FILL, r'//tr[37]/td[5]/input'),
                    'signAndRetreatYear': (FORM_GET, r'//tr[37]/td[6]/input'),
                },
                # 期初未缴查补税额
                'thirtySixRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[38]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[38]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[38]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[38]/td[6]/input'),
                },
                # 本期入库查补税额
                'thirtySevenRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[39]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[39]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[39]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[39]/td[6]/input'),
                },
                # 期末未缴查补税额
                'thirtyEightRow': {
                    'commonlyMonth': (FORM_FILL, r'//tr[40]/td[3]/input'),
                    'commonlyYear': (FORM_GET, r'//tr[40]/td[4]/input'),
                    'signAndRetreatMonth': (FORM_NO, r'//tr[40]/td[5]/input'),
                    'signAndRetreatYear': (FORM_NO, r'//tr[40]/td[6]/input'),
                },
            },
        },

        # 增值税 一般纳税人 附表1
        '5002': {
            'firstTable': {
                # 16%税率的货物及加工修理修配劳务（一、一般计税方法计税）
                'oneRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[4]/td[5]/input'),  # 开具增值税专用发票 销售额
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[4]/td[6]/input'),  # 开具增值税专用发票 销项(应纳)税额
                    'otherSalesAmount': (FORM_FILL, r'//tr[4]/td[7]/input'),  # 开具其他发票 销售额
                    'otherSalesTax': (FORM_FILL, r'//tr[4]/td[8]/input'),  # 开具其他发票 销项(应纳)税额
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[4]/td[9]/input'),  # 未开具发票 销售额
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[4]/td[10]/input'),  # 未开具发票 销项(应纳)税额
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[4]/td[11]/input'),  # 纳税检查调整 销售额
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[4]/td[12]/input'),  # 纳税检查调整 销项(应纳)税额
                    'totalSalesAmount': (FORM_GET, r'//tr[4]/td[13]/input'),  # 合计 销售额
                    'totalSalesTax': (FORM_GET, r'//tr[4]/td[14]/input'),  # 合计 销项（应缴）税额
                    'totalPriceTax': (FORM_NO, r'//tr[4]/td[15]/input'),  # 合计 价税合计
                    'actualDeductionAmount': (FORM_NO, r'//tr[4]/td[16]/input'),  # 服务、不动产和无形资产扣除项目本期实际扣除金额
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[4]/td[17]/input'),  # 扣除后 含税(免税)销售额
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[4]/td[18]/input'),  # 扣除后 销项(应纳)税额
                },
                # 16%税率的服务、不动产和无形资产
                'twoRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[5]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[5]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[5]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[5]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[5]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[5]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[5]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[5]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[5]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[5]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[5]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[5]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[5]/td[16]/input'),
                },
                # 13%税率
                'threeRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[6]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[6]/td[4]/input'),
                    'otherSalesAmount': (FORM_NO, r'//tr[6]/td[5]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[6]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[6]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[6]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[6]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[6]/td[10]/input'),
                    'totalSalesAmount': (FORM_NO, r'//tr[6]/td[11]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[6]/td[12]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[6]/td[13]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[6]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[6]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[6]/td[16]/input'),
                },
                # 10%税率的货物及加工修理修配劳务（一、一般计税方法计税）
                'fourARow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[7]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[7]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[7]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[7]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[7]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[7]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[7]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[7]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[7]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[7]/td[12]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[7]/td[13]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[7]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[7]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[7]/td[16]/input'),
                },
                # 10%税率的服务、不动产和无形资产（一、一般计税方法计税）
                'fourBRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[8]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[8]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[8]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[8]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[8]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[8]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[8]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[8]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[8]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[8]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[8]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[8]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[8]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[8]/td[16]/input'),
                },
                # 6%税率（一、一般计税方法计税）
                'fiveRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[9]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[9]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[9]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[9]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[9]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[9]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_FILL, r'//tr[9]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_FILL, r'//tr[9]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[9]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[9]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[9]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[9]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[9]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[9]/td[16]/input'),
                },
                # 即征即退货物及加工修理修配劳务（一、一般计税方法计税）
                'sixRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[10]/td[4]/input'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[10]/td[5]/input'),
                    'otherSalesAmount': (FORM_NO, r'//tr[10]/td[6]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[10]/td[7]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[10]/td[8]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[10]/td[9]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[10]/td[10]/input'),
                    'taxInspectionSalesTax': (FORM_GET, r'//tr[10]/td[11]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[10]/td[12]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[10]/td[13]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[10]/td[14]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[10]/td[15]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[10]/td[16]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[10]/td[17]/input'),
                },
                # 即征即退服务、不动产和无形资产（一、一般计税方法计税）
                'sevenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[11]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[11]/td[4]/input'),
                    'otherSalesAmount': (FORM_NO, r'//tr[11]/td[5]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[11]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[11]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[11]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[11]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_GET, r'//tr[11]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[11]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[11]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[11]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[11]/td[14]/input'),  # 服务、不动产和无形资产扣除项目本期实际扣除金额
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[11]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[11]/td[16]/input'),
                },
            },

            'secondTable': {
                # 6%征收率
                'eightRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[12]/td[5]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[12]/td[6]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[12]/td[7]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[12]/td[8]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[12]/td[9]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[12]/td[10]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[12]/td[11]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[12]/td[12]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[12]/td[13]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[12]/td[14]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[12]/td[15]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[12]/td[16]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[12]/td[17]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[12]/td[18]/input'),
                },
                # 5%征收率的货物及加工修理修配劳务
                'nineARow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[13]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[13]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[13]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[13]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[13]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[13]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[13]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[13]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[13]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[13]/td[12]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[13]/td[13]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[13]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[13]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[13]/td[16]/input'),
                },
                # 5%征收率的服务、不动产和无形资产
                'nineBRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[14]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[14]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[14]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[14]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[14]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[14]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[14]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[14]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[14]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[14]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[14]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[14]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[14]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[14]/td[16]/input'),
                },
                # 4%征收率
                'tenRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[15]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[15]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[15]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[15]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[15]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[15]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[15]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[15]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[15]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[15]/td[12]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[15]/td[13]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[15]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[15]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[15]/td[16]/input'),
                },
                # 3%征收率的货物及加工修理修配劳务
                'elevenRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[16]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[16]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[16]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[16]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[16]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[16]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[16]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[16]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[16]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[16]/td[12]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[16]/td[13]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[16]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[16]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[16]/td[16]/input'),
                },
                # 3%征收率的服务、不动产和无形资产
                'twelveRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[17]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[17]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[17]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[17]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[17]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[17]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[17]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[17]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[17]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[17]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[17]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[17]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[17]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[17]/td[16]/input'),
                },
                # 预征率   %
                'thirteenARow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[18]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[18]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[18]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[18]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[18]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[18]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[18]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[18]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[18]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[18]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[18]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[18]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[18]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[18]/td[16]/input'),
                },
                # 预征率   %
                'thirteenBRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[19]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[19]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[19]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[19]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[19]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[19]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[19]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[19]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[19]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[19]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[19]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[19]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[19]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[19]/td[16]/input'),
                },
                # 预征率   %
                'thirteenCRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[20]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[20]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[20]/td[5]/input'),
                    'otherSalesTax': (FORM_FILL, r'//tr[20]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[20]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_FILL, r'//tr[20]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[20]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[20]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[20]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[20]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[20]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[20]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[20]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[20]/td[16]/input'),
                },
                # 即征即退货物及加工修理修配劳务（二、简易计税方法计税）
                'fourteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[21]/td[4]/input'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[21]/td[5]/input'),
                    'otherSalesAmount': (FORM_NO, r'//tr[21]/td[6]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[21]/td[7]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[21]/td[8]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[21]/td[9]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[21]/td[10]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[21]/td[11]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[21]/td[12]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[21]/td[13]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[21]/td[14]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[21]/td[15]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[21]/td[16]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[21]/td[17]/input'),
                },
                # 即征即退服务、不动产和无形资产（二、简易计税方法计税）
                'fifteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[22]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[22]/td[4]/input'),
                    'otherSalesAmount': (FORM_NO, r'//tr[22]/td[5]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[22]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_NO, r'//tr[22]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[22]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[22]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_GET, r'//tr[22]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[22]/td[11]/input'),
                    'totalSalesTax': (FORM_GET, r'//tr[22]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[22]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[22]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[22]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_GET, r'//tr[22]/td[16]/input'),
                },
            },

            'thirdTable': {
                # 货物及加工修理修配劳务（三、免抵退税）
                'sixteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[23]/td[4]/input'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[23]/td[5]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[23]/td[6]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[23]/td[7]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[23]/td[8]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[23]/td[9]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[23]/td[10]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[23]/td[11]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[23]/td[12]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[23]/td[13]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[23]/td[14]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[23]/td[15]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[23]/td[16]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[23]/td[17]/input'),
                },
                # 服务、不动产和无形资产（三、免抵退税）
                'seventeenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[24]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[24]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[24]/td[5]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[24]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[24]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[24]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[24]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[24]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[24]/td[11]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[24]/td[12]/input'),
                    'totalPriceTax': (FORM_GET, r'//tr[24]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[24]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[24]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[24]/td[16]/input'),
                },
            },

            'fourthTable': {
                # 货物及加工修理修配劳务（四、免税）
                'eighteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_FILL, r'//tr[25]/td[4]/input'),
                    'valueAddedTaxSalesTax': (FORM_FILL, r'//tr[25]/td[5]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[25]/td[6]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[25]/td[7]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[25]/td[8]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[25]/td[9]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[25]/td[10]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[25]/td[11]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[25]/td[12]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[25]/td[13]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[25]/td[14]/input'),
                    'actualDeductionAmount': (FORM_NO, r'//tr[25]/td[15]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_NO, r'//tr[25]/td[16]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[25]/td[17]/input'),

                },
                # 服务、不动产和无形资产（四、免税）
                'nineteenRow': {
                    'valueAddedTaxSalesAmount': (FORM_NO, r'//tr[26]/td[3]/input'),
                    'valueAddedTaxSalesTax': (FORM_NO, r'//tr[26]/td[4]/input'),
                    'otherSalesAmount': (FORM_FILL, r'//tr[26]/td[5]/input'),
                    'otherSalesTax': (FORM_NO, r'//tr[26]/td[6]/input'),
                    'invoiceNotIssuedSalesAmount': (FORM_FILL, r'//tr[26]/td[7]/input'),
                    'invoiceNotIssuedSalesTax': (FORM_NO, r'//tr[26]/td[8]/input'),
                    'taxInspectionSalesAmount': (FORM_NO, r'//tr[26]/td[9]/input'),
                    'taxInspectionSalesTax': (FORM_NO, r'//tr[26]/td[10]/input'),
                    'totalSalesAmount': (FORM_GET, r'//tr[26]/td[11]/input'),
                    'totalSalesTax': (FORM_NO, r'//tr[26]/td[12]/input'),
                    'totalPriceTax': (FORM_NO, r'//tr[26]/td[13]/input'),
                    'actualDeductionAmount': (FORM_FILL, r'//tr[26]/td[14]/input'),
                    'afterDeductionTaxSalesAmount': (FORM_GET, r'//tr[26]/td[15]/input'),
                    'afterDeductionTaxSalesTax': (FORM_NO, r'//tr[26]/td[16]/input'),
                },
            },
        },

        # 增值税 一般纳税人 附表2
        '5003': {
            'firstTable': {
                # （一）认证相符的增值税专用发票
                'oneRow': {
                    'amount': (FORM_FILL, r'//tr[4]/td[3]/input'),  # 份数
                    'money': (FORM_FILL, r'//tr[4]/td[4]/input'),  # 金额
                    'taxAmount': (FORM_FILL, r'//tr[4]/td[5]/input'),  # 税额
                },
                # 其中：本期认证相符且本期申报抵扣
                'twoRow': {
                    'amount': (FORM_FILL, r'//tr[5]/td[3]/input'),  # 份数
                    'money': (FORM_FILL, r'//tr[5]/td[4]/input'),  # 金额
                    'taxAmount': (FORM_FILL, r'//tr[5]/td[5]/input'),  # 税额
                },
                # 前期认证相符且本期申报抵扣
                'threeRow': {
                    'amount': (FORM_FILL, r'//tr[6]/td[3]/input'),  # 份数
                    'money': (FORM_FILL, r'//tr[6]/td[4]/input'),  # 金额
                    'taxAmount': (FORM_FILL, r'//tr[6]/td[5]/input'),  # 税额
                },
                # （二）其他扣税凭证
                'fourRow': {
                    'amount': (FORM_FILL, r'//tr[7]/td[3]/input'),  # 份数
                    'money': (FORM_FILL, r'//tr[7]/td[4]/input'),  # 金额
                    'taxAmount': (FORM_FILL, r'//tr[7]/td[5]/input'),  # 税额
                },
                # 其中：海关进口增值税专用缴款书
                'fiveRow': {
                    'amount': (FORM_FILL, r'//tr[8]/td[3]/input'),  # 份数
                    'money': (FORM_FILL, r'//tr[8]/td[4]/input'),  # 金额
                    'taxAmount': (FORM_FILL, r'//tr[8]/td[5]/input'),  # 税额
                },
                # 农产品收购发票或者销售发票
                'sixRow': {
                    'amount': (FORM_FILL, r'//tr[9]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[9]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[9]/td[5]/input'),
                },
                # 代扣代缴税收缴款凭证
                'sevenRow': {
                    'amount': (FORM_FILL, r'//tr[10]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[10]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[10]/td[5]/input'),
                },
                # 加计扣除农产品进项税额
                'eightARow': {
                    'amount': (FORM_NO, r'//tr[11]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[11]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[11]/td[5]/input'),
                },
                # 其他
                'eightBRow': {
                    'amount': (FORM_FILL, r'//tr[13]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[13]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[13]/td[5]/input'),
                },
                # （三）本期用于购建不动产的扣税凭证
                'nineRow': {
                    'amount': (FORM_FILL, r'//tr[14]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[14]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[14]/td[5]/input'),
                },
                # （四）本期不动产允许抵扣进项税额
                'tenRow': {
                    'amount': (FORM_NO, r'//tr[15]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[15]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[15]/td[5]/input'),
                },
                # （五）外贸企业进项税额抵扣证明
                'elevenRow': {
                    'amount': (FORM_NO, r'//tr[16]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[16]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[16]/td[5]/input'),
                },
                # 当期申报抵扣进项税额合计
                'twelveRow': {
                    'amount': (FORM_NO, r'//tr[17]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[17]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[17]/td[5]/input'),
                },
            },
            'secondTable': {
                # 本期进项税额转出额
                'oneRow': {
                    'taxAmount': (FORM_FILL, r'//tr[20]/td[3]/input'),
                },
                # 其中：免税项目用
                'twoRow': {
                    'taxAmount': (FORM_FILL, r'//tr[21]/td[3]/input'),
                },
                # 集体福利、个人消费
                'threeRow': {
                    'taxAmount': (FORM_FILL, r'//tr[22]/td[3]/input'),
                },
                # 非正常损失
                'fourRow': {
                    'taxAmount': (FORM_FILL, r'//tr[23]/td[3]/input'),
                },
                # 简易计税方法征税项目用
                'fiveRow': {
                    'taxAmount': (FORM_FILL, r'//tr[24]/td[3]/input'),
                },
                # 免抵退税办法不得抵扣的进项税额
                'sixRow': {
                    'taxAmount': (FORM_FILL, r'//tr[25]/td[3]/input'),
                },
                # 纳税检查调减进项税额
                'sevenRow': {
                    'taxAmount': (FORM_FILL, r'//tr[26]/td[3]/input'),
                },
                # 红字专用发票信息表注明的进项税额
                'eightRow': {
                    'taxAmount': (FORM_FILL, r'//tr[27]/td[3]/input'),
                },
                # 上期留抵税额抵减欠税
                'nineRow': {
                    'taxAmount': (FORM_FILL, r'//tr[28]/td[3]/input'),
                },
                # 上期留抵税额退税
                'tenRow': {
                    'taxAmount': (FORM_FILL, r'//tr[29]/td[3]/input'),
                },
                # 其他应作进项税额转出的情形
                'elevenRow': {
                    'taxAmount': (FORM_FILL, r'//tr[30]/td[3]/input'),
                },
            },
            'thirdTable': {
                # （一）认证相符的增值税专用发票
                'oneRow': {
                    'amount': (FORM_NO, r'//tr[33]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[33]/td[4]/input'),
                    'taxAmount': (FORM_NO, r'//tr[33]/td[5]/input'),
                },
                # 期初已认证相符但未申报抵扣
                'twoRow': {
                    'amount': (FORM_FILL, r'//tr[34]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[34]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[34]/td[5]/input'),
                },
                # 本期认证相符且本期未申报抵扣
                'threeRow': {
                    'amount': (FORM_FILL, r'//tr[35]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[35]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[35]/td[5]/input'),
                },
                # 期末已认证相符但未申报抵扣
                'fourRow': {
                    'amount': (FORM_FILL, r'//tr[36]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[36]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[36]/td[5]/input'),
                },
                # 其中：按照税法规定不允许抵扣
                'fiveRow': {
                    'amount': (FORM_FILL, r'//tr[37]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[37]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[37]/td[5]/input'),
                },
                # （二）其他扣税凭证
                'sixRow': {
                    'amount': (FORM_FILL, r'//tr[38]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[38]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[38]/td[5]/input'),
                },
                # 其中：海关进口增值税专用缴款书
                'sevenRow': {
                    'amount': (FORM_FILL, r'//tr[39]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[39]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[39]/td[5]/input'),
                },
                # 农产品收购发票或者销售发票
                'eightRow': {
                    'amount': (FORM_FILL, r'//tr[40]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[40]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[40]/td[5]/input'),
                },
                # 代扣代缴税收缴款凭证
                'nineRow': {
                    'amount': (FORM_FILL, r'//tr[41]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[41]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[41]/td[5]/input'),
                },
                # 其他
                'tenRow': {
                    'amount': (FORM_FILL, r'//tr[42]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[42]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[42]/td[5]/input'),
                },
                #
                'elevenRow': {
                    'amount': (FORM_NO, r'//tr[43]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[43]/td[4]/input'),
                    'taxAmount': (FORM_NO, r'//tr[43]/td[5]/input'),
                },
            },
            'fourthTable': {
                # 本期认证相符的增值税专用发票
                'oneRow': {
                    'amount': (FORM_FILL, r'//tr[46]/td[3]/input'),
                    'money': (FORM_FILL, r'//tr[46]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[46]/td[5]/input'),
                },
                # 代扣代缴税额
                'twoRow': {
                    'amount': (FORM_NO, r'//tr[47]/td[3]/input'),
                    'money': (FORM_NO, r'//tr[47]/td[4]/input'),
                    'taxAmount': (FORM_FILL, r'//tr[47]/td[5]/input'),
                },
            },
        },

        # 增值税 一般纳税人 附表3
        '5006': {
            'firstTable': {
                # 16%税率的项目
                'oneRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[4]/td[3]/input'),  # 本期应税服务价税合计额(免税销售额)
                    'initialAmount': (FORM_GET, r'//tr[4]/td[4]/input'),  # 应税服务扣除项目 期初余额
                    'currentPeriodAmount': (FORM_FILL, r'//tr[4]/td[5]/input'),  # 应税服务扣除项目 本期发生额
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[4]/td[6]/input'),  # 应税服务扣除项目 本期应扣除金额
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[4]/td[7]/input'),  # 应税服务扣除项目 本期实际扣除金额
                    'endAmount': (FORM_FILL, r'//tr[4]/td[8]/input'),  # 应税服务扣除项目 期末余额
                },
                # 10%税率的项目
                'twoRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[5]/td[3]/input'),
                    'initialAmount': (FORM_GET, r'//tr[5]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[5]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[5]/td[7]/input'),
                    'endAmount': (FORM_FILL, r'//tr[5]/td[8]/input'),
                },
                # 6%税率的项目(不含金融商品转让)
                'threeRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[6]/td[3]/input'),
                    'initialAmount': (FORM_GET, r'//tr[6]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[6]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[6]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[6]/td[7]/input'),
                    'endAmount': (FORM_FILL, r'//tr[6]/td[8]/input'),
                },
                # 6%税率的金融商品转让项目
                'fourRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[7]/td[3]/input'),
                    'initialAmount': (FORM_GET, r'//tr[7]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[7]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[7]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[7]/td[7]/input'),
                    'endAmount': (FORM_FILL, r'//tr[7]/td[8]/input'),
                },
                # 5%征收率的项目
                'fiveRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[8]/td[3]/input'),
                    'initialAmount': (FORM_GET, r'//tr[8]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[8]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[8]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[8]/td[7]/input'),
                    'endAmount': (FORM_FILL, r'//tr[8]/td[8]/input'),
                },
                # 3%税率的项目
                'sixRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[9]/td[3]/input'),
                    'initialAmount': (FORM_GET, r'//tr[9]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[9]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[9]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[9]/td[7]/input'),
                    'endAmount': (FORM_FILL, r'//tr[9]/td[8]/input'),
                },
                # 免抵退税的项目
                'sevenRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[10]/td[3]/input'),
                    'initialAmount': (FORM_GET, r'//tr[10]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[10]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[10]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[10]/td[7]/input'),
                    'endAmount': (FORM_FILL, r'//tr[10]/td[8]/input'),
                },
                # 免税的项目
                'eightRow': {
                    'dutyFreeAmount': (FORM_FILL, r'//tr[11]/td[3]/input'),
                    'initialAmount': (FORM_GET, r'//tr[11]/td[4]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[11]/td[5]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[11]/td[6]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[11]/td[7]/input'),
                    'endAmount': (FORM_FILL, r'//tr[11]/td[8]/input'),
                },
            },
        },

        # 增值税 一般纳税人 附表4
        '5007': {
            'firstTable': {
                # 增值税税控系统专用设备费及技术维护费
                'oneRow': {
                    'initialAmount': (FORM_GET, r'//tr[3]/td[3]/input'),  # 期初余额
                    'currentPeriodAmount': (FORM_FILL, r'//tr[3]/td[4]/input'),  # 本期发生额
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[3]/td[5]/input'),  # 本期应抵减税额
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[3]/td[6]/input'),  # 本期实际抵减税额
                    'endAmount': (FORM_FILL, r'//tr[3]/td[7]/input'),  # 期末余额
                },
                # 分支机构预征缴纳税款
                'twoRow': {
                    'initialAmount': (FORM_GET, r'//tr[4]/td[3]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[4]/td[4]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[4]/td[5]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[4]/td[6]/input'),
                    'endAmount': (FORM_FILL, r'//tr[4]/td[7]/input'),
                },
                # 建筑服务预征缴纳税款
                'threeRow': {
                    'initialAmount': (FORM_GET, r'//tr[5]/td[3]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[5]/td[4]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[5]/td[6]/input'),
                    'endAmount': (FORM_FILL, r'//tr[5]/td[7]/input'),
                },
                # 销售不动产预征缴纳税款
                'fourRow': {
                    'initialAmount': (FORM_GET, r'//tr[6]/td[3]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[6]/td[4]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[6]/td[5]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[6]/td[6]/input'),
                    'endAmount': (FORM_FILL, r'//tr[6]/td[7]/input'),
                },
                # 出租不动产预征缴纳税款
                'fiveRow': {
                    'initialAmount': (FORM_GET, r'//tr[7]/td[3]/input'),
                    'currentPeriodAmount': (FORM_FILL, r'//tr[7]/td[4]/input'),
                    'currentPeriodDeductedAmount': (FORM_FILL, r'//tr[7]/td[5]/input'),
                    'currentPeriodActualDeductionAmount': (FORM_FILL, r'//tr[7]/td[6]/input'),
                    'endAmount': (FORM_FILL, r'//tr[7]/td[7]/input'),
                },
            },
        },

        # 增值税 一般纳税人 附表5
        '5008': {
            'firstTable': {
                'oneRow': {
                    'startPeriodDeductibleImmovableTax': (FORM_FILL, r'//tr[3]/td[1]/input'),  # 期初待抵扣不动产进项税额
                    'currentPeriodImmovableTaxIncrementAmount': (FORM_FILL, r'//tr[3]/td[2]/input'),  # 本期不动产进项税额增加额
                    'currentPeriodDeductibleImmovableTax': (FORM_FILL, r'//tr[3]/td[3]/input'),  # 本期可抵扣不动产进项税额
                    'currentPeriodInDeductedImmovableTax': (FORM_FILL, r'//tr[3]/td[4]/input'),  # 本期转入的待抵扣不动产进项税额
                    'currentPeriodOutDeductedImmovableTax': (FORM_FILL, r'//tr[3]/td[5]/input'),  # 本期转出的待抵扣不动产进项税额
                    'endDeductedImmovableTax': (FORM_FILL, r'//tr[3]/td[6]/input'),  # 期末待抵扣不动产进项税额
                },
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
                'currentPeriodAmount': (FORM_FILL, r'//tr[{tr_no}]/td[3]/input'),  # 期初余额
                'currentPeriodProduceAmount': (FORM_FILL, r'//tr[{tr_no}]/td[4]/input'),  # 本期发生额
                'currentPeriodActualDeductionTax': (FORM_FILL, r'//tr[{tr_no}]/td[6]/input'),  # 本期实际抵减税额
            }
        },

        # 营改增税负分析测算明细表
        '5009': {
            'template': {
                'project': (FORM_FILL, r'//tr[{tr_no}]/td[1]/select'),  # 应税项目代码及名称
                'incrementTax': (FORM_FILL, r'//tr[{tr_no}]/td[5]/select'),  # 增值税税率或征收率
                'businessTax': (FORM_FILL, r'//tr[{tr_no}]/td[6]/select'),  # 营业税税率
                'zeroTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[7]/input'),  # 不含税销售额
                'serviceCurrentPeriodDeductionAmount': (FORM_FILL, r'//tr[{tr_no}]/td[10]/input'),  # 服务、不动产和无形资产扣除项目本期实际扣除金额
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
                    'goodsLabourMonth': (FORM_FILL, r'//tr[3]/td[3]/input'),  # 货物及劳务（本期数）
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[3]/td[4]/input'),  # 服务、不动产和无形资产（本期数）
                    'goodsLabourYear': (FORM_GET, r'//tr[3]/td[5]/input'),  # 货物及劳务(本年累计)
                    'serviceImmovableYear': (FORM_GET, r'//tr[3]/td[6]/input'),  # 服务、不动产和无形资产(本年累计)
                },

                # 税务机关代开的增值税专用发票不含税销售额
                'twoRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[4]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[4]/td[4]/input'),
                    'goodsLabourYear': (FORM_FILL, r'//tr[4]/td[5]/input'),
                    'serviceImmovableYear': (FORM_FILL, r'//tr[4]/td[6]/input'),
                },
                # 税控器具开具的普通发票不含税销售额
                'threeRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[5]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[5]/td[4]/input'),
                    'goodsLabourYear': (FORM_FILL, r'//tr[5]/td[5]/input'),
                    'serviceImmovableYear': (FORM_FILL, r'//tr[5]/td[6]/input'),
                },
                # （二）应征增值税不含税销售额（5%征收率）
                'fourRow': {
                    'goodsLabourMonth': (FORM_NO, r'//tr[6]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[6]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[6]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[6]/td[6]/input'),
                },
                # 税务机关代开的增值税专用发票不含税销售额
                'fiveRow': {
                    'goodsLabourMonth': (FORM_NO, r'//tr[7]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[7]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[7]/td[5]/input'),
                    'serviceImmovableYear': (FORM_FILL, r'//tr[7]/td[6]/input'),
                },
                # 税控器具开具的普通发票不含税销售额
                'sixRow': {
                    'goodsLabourMonth': (FORM_NO, r'//tr[8]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[8]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[8]/td[5]/input'),
                    'serviceImmovableYear': (FORM_FILL, r'//tr[8]/td[6]/input'),
                },
                # （三）销售使用过的固定资产不含税销售额
                'sevenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[9]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_NO, r'//tr[9]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[9]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[9]/td[6]/input'),
                },
                # 其中：税控器具开具的普通发票不含税销售额
                'eightRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[11]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_NO, r'//tr[11]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[11]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[11]/td[6]/input'),
                },
                # （四）免税销售额
                'nineRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[12]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[12]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[12]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[12]/td[6]/input'),
                },
                # 其中：小微企业免税销售额
                'tenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[13]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[13]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[13]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[13]/td[6]/input'),
                },
                # 未达起征点销售额
                'elevenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[14]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[14]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[14]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[14]/td[6]/input'),
                },
                # 其他免税销售额
                'twelveRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[15]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[15]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[15]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[15]/td[6]/input'),
                },
                # （五）出口免税销售额
                'thirteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[16]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[16]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[16]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[16]/td[6]/input'),
                },
                # 其中：税控器具开具的普通发票销售额
                'fourteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[17]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[17]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[17]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[17]/td[6]/input'),
                },
            },
            'secondTable': {
                # 本期应纳税额
                'fifteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[18]/td[4]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[18]/td[5]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[18]/td[6]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[18]/td[7]/input'),
                },
                # 本期应纳税额减征额
                'sixteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[19]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[19]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[19]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[19]/td[6]/input'),
                },
                # 本期免税额
                'seventeenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[20]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[20]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[20]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[20]/td[6]/input'),
                },
                # 其中：小微企业免税额
                'eighteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[21]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[21]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[21]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[21]/td[6]/input'),
                },
                # 未达起征点免税额
                'nineteenRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[22]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[22]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[22]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[22]/td[6]/input'),
                },
                # 应纳税额合计
                'twentyRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[23]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[23]/td[4]/input'),
                    'goodsLabourYear': (FORM_GET, r'//tr[23]/td[5]/input'),
                    'serviceImmovableYear': (FORM_GET, r'//tr[23]/td[6]/input'),
                },
                # 本期预缴税额
                'twentyOneRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[24]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[24]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[24]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[24]/td[6]/input'),
                },
                # 本期应补（退）税额
                'twentyTwoRow': {
                    'goodsLabourMonth': (FORM_FILL, r'//tr[25]/td[3]/input'),
                    'serviceImmovableMonth': (FORM_FILL, r'//tr[25]/td[4]/input'),
                    'goodsLabourYear': (FORM_NO, r'//tr[25]/td[5]/input'),
                    'serviceImmovableYear': (FORM_NO, r'//tr[25]/td[6]/input'),
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
                'currentPeriodAmount': (FORM_FILL, r'//tr[{tr_no}]/td[3]/input'),  # 期初余额
                'currentPeriodProduceAmount': (FORM_FILL, r'//tr[{tr_no}]/td[4]/input'),  # 本期发生额
                'currentPeriodActualDeductionTax': (FORM_FILL, r'//tr[{tr_no}]/td[6]/input'),  # 本期实际抵减税额
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
            'project': (FORM_NO, r''),  # 征收项目
            'productName': (FORM_NO, r''),  # 征收品目
            'commonlyIncrementTax': (FORM_FILL, r'//tr[{tr_no}]/td[4]/input'),  # 一般增值税
            'exemptionTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[5]/input'),  # 免抵税额
            'reductionCode': (FORM_FILL, r'//tr[{tr_no}]/td[11]/select'),  # 减免性质代码
            'reductionAmount': (FORM_FILL, r'//tr[{tr_no}]/td[16]/input'),  # 减免额
            'currentPeriodPaidTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[17]/input'),  # 本期已缴税（费）额
        }
    }


# 印花税表（行数不固定）
def get_stamp_duty_table():
    return {
        'template': {
            'project': (FORM_NO, r''),
            'taxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[3]/input'),  # 计税金额或件数
            'currentPeriodPaidTaxAmount':  (FORM_FILL, r'//tr[{tr_no}]/td[9]/input'),  # 本期已缴税额
            'reliefPropertyCode': (FORM_FILL, r'//tr[{tr_no}]/td[10]/select'),  # 减免性质代码
            'deductionTaxAmount': (FORM_FILL, r'//tr[{tr_no}]/td[12]/input'),  # 减免税额
        },
    }


# 企业所得税A类
def corporate_income_tax_A():
    return {
        'firstTable': {
            # 预缴方式
            'oneRow': {
                # 按照实际利润额预缴
                # 按照上一纳税年度应纳税所得额平均额预缴
                # 按照税务机关确定的其他方法预缴
                'projectValue': (FORM_FILL, r'//tr[1]/td[2]/input'),
            },
            # 企业类型
            'twoRow': {
                # 一般企业
                # 跨地区经营汇总纳税企业
                # 跨地区经营汇总纳税企业
                'projectValue': (FORM_FILL, r'//tr[2]/td[2]'),
            },
            'threeRow': {
                # 一般企业
                # 总机构
                # 分支机构
                'projectValue': (FORM_FILL, r'//tr[2]/td[2]'),
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
            'oneRow': {
                'projectOne': (FORM_FILL, r'//tr[2]/td[2]/input'),  # 小型微利企业（radio）
                'projectTwo': (FORM_FILL, r'//tr[2]/td[4]/input'),  # 科技型中小企业（radio）
            },
            'twoRow': {
                'projectOne': (FORM_FILL, r'//tr[3]/td[2]/input'),  # 高新技术企业（radio）
                'projectTwo': (FORM_FILL, r'//tr[3]/td[4]/input'),  # 技术入股递延纳税事项（radio）
            },
            'threeRow': {
                'projectOne': (FORM_FILL, r'//tr[4]/td[2]/input'),  # 期末从业人数（text）
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
                'selectValue': (FORM_FILL, r'//tr[20]/td[3]/input'),  # 小型微利企业（radio）
                'number': (FORM_FILL, r'//tr[20]/td[6]/input'),  # 期末从业人数（text）
            },
        },
        'fourthTable': {
            'oneRow': {
                'projectOne': (FORM_FILL, r'//tr[21]//td[3]/input'),  # 所属行业明细代码（text）
                'country': (FORM_FILL, r'//tr[21]/td[6]/input'),  # 国家限制或禁止行业（radio）
            },
            'twoRow': {
                'projectOne': (FORM_FILL, r'//tr[22]/td[2]/input'),  # 从业人数（text）
                'country': (FORM_FILL, r'//tr[22]/td[4]/input'),  # 资产总额（万元）（text）
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

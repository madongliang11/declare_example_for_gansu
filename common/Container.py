"""
公共容器：存放‘常量’，可继承并重写其中的变量
"""
import os

from selenium import webdriver


class Container(object):
    """公共部分"""

    PATH = os.getcwd() + '\\'

    # 申报与反馈接口
    # DECLARE_BASE_URL = 'http://shenbao.com/server/shenbao/index.php'
    DECLARE_BASE_URL = 'http://caiwu.leesrobots.com:50082/server/shenbao'
    # DECLARE_BASE_URL = 'http://fi-test.0tb.cn/server/shenbao'
    DECLARE_IN_QUEUE_URL = DECLARE_BASE_URL + '/in_queue_v2'  # 查询path
    DECLARE_FEEDBACK_URL = DECLARE_BASE_URL + '/feedback_v2'  # 反馈path

    # 心跳地址
    HEARTBEAT_URL = 'http://caiwu.leesrobots.com:50082/server/shenbao'

    # 短信验证码接口
    PHONE_CODE_BASE_URL = 'http://47.98.117.190'
    PHONE_SEND_CODE = PHONE_CODE_BASE_URL + '/server/send-user-code'
    PHONE_GET_CODE = PHONE_CODE_BASE_URL + '/server/get-user-code'

    # 登陆状态相关
    LOGIN_ACCOUNT_ERROR = 1  # 用户名密码错误
    LOGIN_AUTH_ERROR = 2  # 认证错误（税网认证服务异常）
    LOGIN_CODE_ERROR = 3  # 验证码错误
    LOGIN_RETRY_ERROR = 4  # 重试次数过多
    LOGIN_MAX_RETRY_TIMES = 3  # 最大重试次数
    LOGIN_REQUEST_INTERVAL = 5  # 请求间隔5秒
    LOGIN_WAIT_SECOND = 300  # 等待时长5分钟
    LOGIN_SUCCESS = 0  # 登陆成功

    # 打码平台相关
    CODE_PLATFORM_BASE_URL = 'http://dama.leesrobots.com'
    CODE_PLATFORM_REQUEST_URL = CODE_PLATFORM_BASE_URL + '/captcha/get_request/'
    CODE_PLATFORM_GET_RESULT_URL = CODE_PLATFORM_BASE_URL + '/captcha/get_captcha_result/'
    CODE_PLATFORM_FEEDBACK_URL = CODE_PLATFORM_BASE_URL + '/captcha/put_captcha_web_result/'
    CODE_PLATFORM_CLIENT_ID = '427c5a953f'
    CODE_PLATFORM_SECRET_KEY = '9cadd611d22503e1d7b9428e9266f7c7'

    # 季报与月报与零申报
    DECLARE_TAX_MODEL_MONTH = 1  # 月报
    DECLARE_TAX_MODEL_SEASON = 1  # 月报
    DECLARE_IS_ZERO = 1  # 零申报

    # 地区代码
    TAX_AREA_CODE = '610100000000'
    # TAX_AREA_CODE = '130304000000'

    # 任务类型
    TASK_TYPE_DECLARE = 1  # 申报任务
    TASK_TYPE_PAYMENT = 2  # 缴款任务
    TASK_TYPE_CHECK = 3  # 检查任务
    TASK_TYPE_IDENTIFY = 4  # 税种鉴定
    TASK_TYPE_INIT = 5  # 自动初始化
    TASK_TYPE_CANCEL = 6  # 作废

    TASK_TYPE_STATUS_MAP = {
        TASK_TYPE_PAYMENT: {
            'success': 0,
            'failed': 0,
            'except': 0
        },
        TASK_TYPE_DECLARE: {
            'success': 0,
            'failed': 0,
            'except': 0
        },
        TASK_TYPE_CHECK: {
            'passed': 6,
            'all_not_declare': 4,
            'part_not_declare': 5,
            'exception': 3
        },
        TASK_TYPE_INIT: {
            'success': 5,
            'failed': 4,
            'except': 3
        },
        TASK_TYPE_IDENTIFY: {
            'success': 5,
            'failed': 4,
            'except': 3
        }
    }

    # queue表状态（反馈的status）
    TASK_RETURN_SUCCESS = 5
    TASK_RETURN_FAILED = 4
    TASK_RETURN_EXCEPT = 3

    # 申报税种对应的执行类
    TAX_CLASS_MAP = {
        1: 'Added',
        2: 'Finance',
        3: 'Additional',
        4: 'StampDuty',
        5: 'DisabledWork',
        6: 'CorporateIncomeTaxA',
        7: 'CorporateIncomeTaxB',
        8: 'WaterBuild',
        9: 'LabourUnion',
        10: 'Culture',
        11: 'AddedSmall',
        12: 'FinanceSmall',
    }

    # 任务类型对应的执行类
    # 1：税种申报，2：缴款，3：税种申报检查，4：税种鉴定，5：期初数据初始化，6：申报作废
    QUEUE_CLASS_MAP = {
        TASK_TYPE_DECLARE: 'Declare',  # 1：税种申报
        TASK_TYPE_PAYMENT: 'Payment',  # 2：缴款
        TASK_TYPE_CHECK: 'Check',  # 3：税种申报检查
        TASK_TYPE_IDENTIFY: 'TaxIdentification',  # 4：税种鉴定
        TASK_TYPE_INIT: 'TaxInit',  # 5：期初数据初始化
        TASK_TYPE_CANCEL: 'Cancel'  # 6：申报作废
    }

    # 验证码图片宽度和高度
    CODE_IMG_WIDTH = 305
    CODE_IMG_HEIGHT = 80

    # 申报表相关
    TABLE_EXISTS = 1  # 税表存在
    TABLE_NOT_EXISTS = 2  # 税表不存在
    TABLE_ALREADY_DECLARE = 3  # 该税种已经申报
    TABLE_ALREADY_DECLARE_STR = '已经申报过了'

    # 是与否
    RADIO_NO = '否'  # 0
    RADIO_YES = '是'  # 1

    # 关联任务的状态
    RELATION_STATUS_MAP = {
        TASK_TYPE_DECLARE: {

        },
        TASK_TYPE_PAYMENT: {

        },
        TASK_TYPE_CHECK: {
            'ALL_NOT_DECLARE': 4,
            'PART_NOT_DECLARE': 5,
            'PASSED': 6
        },
        TASK_TYPE_IDENTIFY: {

        },
        TASK_TYPE_INIT: {
            'EXCEPTION': 3,
            'FAILED': 4,
            'SUCCESS': 5
        },
        TASK_TYPE_CANCEL: {

        }
    }

    # 是否为测试环境
    IS_TESTING = True

    """""""""""""""""""""""""""""""""""
    """"""""""""自定义部分""""""""""""""
    """""""""""""""""""""""""""""""""""
    # 税网的
    PAGE_LOGIN_URL = 'https://etax.gansu.chinatax.gov.cn/bszm-web/apps/views/beforeLogin/indexBefore/pageIndex.html'
    PAGE_HOME_URL = 'https://etax.gansu.chinatax.gov.cn/bszm-web/apps/views/companyPage/desktopTax.html?service=https://etax.gansu.chinatax.gov.cn/bszm-web/apps/views/companyPage/desktopTax.html'

    # 申报税种在税网上对应的名字
    TAX_NAME_MAP = {
        1: '增值税纳税申报表（一般纳税人适用）',
        2: '财务报表（企业会计准则）',
        3: '附加税（费）纳税申报表',
        4: '印花税申报表',
        5: '通用申报表-残疾人就业保障金',
        6: '居民企业（查账征收）企业所得税月（季）度申报（2018年版）',
        7: '居民企业（核定征收）企业所得税月（季）度及年度申报（2018年版）',
        8: '通用申报表-水利建设基金',
        9: '通用申报表-工会经费',
        10: '文化事业建设费申报表（营改增）',
        11: '增值税纳税申报表（小规模纳税人适用）',
        12: '小企业会计准则',
    }

    """""""""""""""""""""""""""""""""""
    """""""""""""公共数据""""""""""""""
    """""""""""""""""""""""""""""""""""
    DRIVER = None  # 浏览器驱动
    COMMON_DATA = None  # 报税的公共参数，包含税号、账号、密码、队列类型、队列id
    TASK_DATA = None  # 关联任务的相关信息，申报的季报月报类型、检查的id等
    FEEDBACK = None  # 反馈数据结构
    TAX_INIT_DATA = dict()  # 税种初始化的
    IDENTIFY_INFO = list()  # 税种鉴定的数据
    CHECK_INFO = list()  # 申报检查的数据
    RELATION_STATUS = 0  # queue队列关联的任务状态，在各自的任务类中设置

    """""""""""""""""""""""""""""""""""
    """""""""""""其他"""""""""""""""""""
    """""""""""""""""""""""""""""""""""
    IN_OTHER_TABLE_PAGE = 0  # 是否在其他页面中
    NOW_TABLE_NAME = None  # 当前税种名称

    def __init__(self):
        self.init_feedback_data()

    @classmethod
    def init_data(cls, common_data, browser=None):
        cls.FEEDBACK = {
            'status': None,
            'message': None,
            'data': {
                'queue_id': None,  # 队列id
                'queue_type': None,  # 队列类型
                'relation_id': [],  # 关联的任务id
                'relation_status': None,  # 关联的任务执行状态
                'is_final': None,  # 是否是最后一条任务
                'identify_info': None,  # 税种鉴定信息
                'init_data': None,  # 自动初始化信息
                'payment': None,  # 申报任务产生的税款
                'result_img': [],  # 反馈截图列表
            },
        }

        # 启动浏览器
        if browser is None:
            return False
        elif browser == 'chrome':
            cls.DRIVER = webdriver.Chrome()
        elif browser == 'ie':
            cls.DRIVER = webdriver.Ie()
        elif browser == 'firefox':
            cls.DRIVER = webdriver.Firefox()
        else:
            return False

        cls.COMMON_DATA = common_data
        cls.TASK_DATA = None
        cls.IN_OTHER_TABLE_PAGE = 0
        cls.NOW_TABLE_NAME = None

    @staticmethod
    def init_feedback_data():
        """
        初始化反馈的数据结构
        :return:
        """
        Container.FEEDBACK = {
            'status': None,
            'message': None,
            'data': {
                'queue_id': None,  # 队列id
                'queue_type': None,  # 队列类型
                'relation_id': [],  # 关联的任务id
                'relation_status': None,  # 关联的任务执行状态
                'is_final': None,  # 是否是最后一条任务
                'identify_info': None,  # 税种鉴定信息
                'init_data': None,  # 自动初始化信息
                'payment': None,  # 申报任务产生的税款
                'result_img': [],  # 反馈截图列表
            },
        }


if __name__ == '__main__':
    print(Container.PATH)

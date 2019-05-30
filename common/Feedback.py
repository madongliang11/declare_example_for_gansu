from common.Container import Container
from common.HttpClient import HttpClient
from common.Logger import Logger


class Feedback(object):

    def __init__(self):
        self._Logger = Logger()
        self._HttpClient = HttpClient()
        self._feedback_data = {
            'task_type': 0,
            'statement_id': [],  # 流水id，数据唯一标识
            'queue_id': 0,  # 任务队列id todo 新任务表的主ID，申报和缴款没有这个ID
            'result_img': [],  # 返回的图片
            'payment': 0,  # 缴款金额
            'relation_status': 0,  # 关联任务的状态  todo 新任务才有的，申报有缴款没有这个字段
            'is_final': 0,
            'identify_info': [],  # 税种鉴定的数据
            'init_data': {},  # 初始化的数据
            'check_into': [],  # 申报检查数据
        }
        self.empty_feedback = dict(self._feedback_data)

    def update_feedback_data(self, task_type=0, statement_id=None, queue_id=0, result_img=None, payment=0,
                             relation_status=0, is_final=0, identify_info=None, init_data=None, check_into=None):
        """
        构造反馈数据
        :param task_type:
        :param statement_id:
        :param queue_id:
        :param result_img:
        :param payment:
        :param relation_status:
        :param is_final:
        :param identify_info:
        :param init_data:
        :return:
        """
        if task_type:
            self._feedback_data['task_type'] = task_type
        if statement_id is not None and type(statement_id).__name__ == 'list':
            self._feedback_data['statement_id'] = statement_id
        if task_type:
            self._feedback_data['queue_id'] = queue_id
        if result_img is not None and type(result_img).__name__ == 'list':
            self._feedback_data['result_img'] = result_img
        if payment:
            self._feedback_data['payment'] = payment
        if relation_status:
            self._feedback_data['relation_status'] = relation_status
        if is_final:
            self._feedback_data['is_final'] = is_final
        if identify_info is not None and type(identify_info).__name__ == 'list':
            self._feedback_data['identify_info'] = identify_info
        if init_data is not None and type(init_data).__name__ == 'dict':
            self._feedback_data['init_data'] = init_data
        if check_into is not None and type(check_into).__name__ == 'list':
            self._feedback_data['check_into'] = check_into

    def feedback(self, code, msg, retry_times=0):

        """
        向大查柜系统反馈
        :param code: 反馈代码 1,2,3
        :param msg: 反馈信息
        :param retry_times: 重试次数，不超过5次
        :return: 终止程序
        """
        # 重试次数不超过5次
        if retry_times > 5:
            self._Logger.to_log('error', '{}反馈重试次数过多'.format(self._feedback_data['statement_id']))
            return
        url = Container.DECLARE_FEEDBACK_URL
        method = 'POST'
        request_param = {'code': code, 'message': msg, 'data': self._feedback_data}
        result, response = self._HttpClient.to_request(url=url, method=method, request_param=request_param)
        if not result:
            self._Logger.to_log('error', response)
            retry_times += 1
            self._Logger.to_log('error', '第{}次反馈重试'.format(retry_times))
            # 递归调用反馈方法，重试机制
            self.feedback(code, msg, retry_times)
        else:
            # 每当反馈成功的时候就把类变量置空
            self._feedback_data = self.empty_feedback
            try:
                self._Logger.to_log('error', response['message'])
            except Exception as e:
                self._Logger.to_log('error', '反馈成功-数据解析失败 => ' + repr(e))


if __name__ == '__main__':
    fb = Feedback()
    fb._feedback_data = {'task_type': '4', 'statement_id': ['1'], 'queue_id': 1, 'result_img': [], 'payment': 0,
                         'relation_status': 5, 'is_final': 1, 'init_data': {},
                         'identify_info': [{'tax': '企业所得税', 'type': 6, 'project': ['应纳税所得额'], 'tax_model': 2},
                                           {'tax': '印花税', 'type': 4, 'project': ['其他营业账簿', '购销合同', '资金账簿'],
                                            'tax_model': 3},
                                           {'tax': '残疾人就业保障金', 'type': 5, 'project': ['残疾人就业保障金'], 'tax_model': 1},
                                           {'tax': '水利建设专项收入', 'type': 8, 'project': ['地方水利建设基金'], 'tax_model': 1},
                                           {'tax': '增值税', 'type': 1, 'project': ['工程服务', '商业(3%)', '有形动产经营租赁'],
                                            'tax_model': 1},
                                           {'tax': '个人所得税', 'type': 0, 'project': ['工资薪金所得'], 'tax_model': 1},
                                           {'tax': '附加税', 'type': 3, 'project': ['地方教育附加', '教育费附加', '城市维护建设税'],
                                            'tax_model': 1}],
                         'check_into': []}
    fb.feedback(1, '请求成功', 0)

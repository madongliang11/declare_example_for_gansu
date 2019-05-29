import time

from common.General import General
from common.Logger import Logger
from custom.Helper import Helper
from common.Container import Container


class Step(object):

    def __init__(self):
        self.helper = Helper()
        self.logger = Logger()
        self.driver = Container.DRIVER
        self.general = General()
        self.info = Container.TASK_DATA

    # 进入选表页面
    def in_to_select_table_page_step(self, step):
        time.sleep(5)
        try:
            # 步骤一，进入选表页面
            self.logger.to_log('info', '步骤{step}开始'.format(step=step))
            time.sleep(4)
            self.driver.refresh()
            time.sleep(3)
            self.driver.find_element_by_link_text('增值税一表集成').click()
            return True, '进入选表页面成功'
        except Exception as e:
            self.general.save_result_img()
            error_message = '步骤{step}：进入选表页面出错'.format(step=step)
            self.logger.to_log('info', error_message + '=>' + repr(e))
            return False, error_message

    # 判断账期和选择报表
    def judge_period_and_select_table_step(self, step):
        try:
            self.logger.to_log('info', '步骤{step}开始'.format(step=step))

            if len(self.driver.window_handles) > 1:
                # 超过两个窗口句柄，就关闭当前窗口，回到原始窗口
                self.logger.to_log('info', '切换窗口句柄')
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

            # 从其他申报表页面回来
            try:
                self.driver.switch_to.default_content()
                # self.driver.switch_to.frame('ifrMain')
                self.general.wait_to_frame('ifrMain')
                if self.driver.find_element_by_class_name('big_title').text == '其他申报':
                    self.helper.go_curr_period_page()
                    self.general.wait_to_frame('ifrMain')
            except Exception as e:
                print(e)

            # 关闭 增值税一般纳税人 的弹框
            try:
                self.driver.switch_to.default_content()
                self.general.wait_to_frame('ifrMain')
                self.driver.find_element_by_class_name('layui-layer-close').click()
            except:
                pass

            result_bool, result_message = self.general.wait(class_name='layui-date-input')
            if result_bool is False:
                return False, result_message

            # self.to_js()
            # time.sleep(2)
            # if not self.helper.in_period():
            #     self.helper.save_result_img()
            #     return False, '账期未到'
            self.logger.to_log('info', '账期已判断')
            if int(self.info['type']) in [2, 12]:  # 财务报表
                res_bool, res_status = self.helper.select_table_for_finance()
            else:
                res_bool, res_status = self.helper.select_table()
            if res_bool is False:
                if res_status == Container.TABLE_ALREADY_DECLARE:
                    self.general.save_result_img()
                    # 已经申报过了
                    return True, Container.TABLE_ALREADY_DECLARE_STR
                elif res_status == Container.TABLE_NOT_EXISTS:
                    self.helper.go_other_declare_page(self.info['table_name'])
                    return False, '税种不存在'
            return True, 'success'
        except Exception as e:
            self.general.save_result_img()
            error_message = '步骤{step}：判断账期和选表出错'.format(step=step)
            self.logger.to_log('info', error_message + '=>' + repr(e))
            return False, error_message

    # 进入其他申报表
    def select_other_table_step(self, step):
        time.sleep(2)
        try:
            # 步骤二，进入其他申报选表
            self.logger.to_log('info', '步骤{step}开始'.format(step=step))
            self.helper.go_other_declare_page(self.info['table_name'])
            Container.IN_OTHER_TABLE_PAGE = 1
            return True, '进入其他申报表成功'
        except Exception as e:
            self.general.save_result_img()
            error_message = '步骤{step}：进入其他申报表出错'.format(step=step)
            self.logger.to_log('info', error_message + '=>' + repr(e))
            return False, error_message

    # 切换窗口句柄
    def change_window_handle_step(self, step):
        time.sleep(2)
        try:
            self.logger.to_log('info', '步骤{step}开始'.format(step=step))
            self.driver.switch_to.window(self.driver.window_handles[1])
            try:
                self.driver.find_element_by_class_name('layui-layer-close').click()
            except:
                pass
            return True, '切换窗口句柄成功'
        except Exception as e:
            self.general.save_result_img()
            error_message = '步骤{step}：切换窗口句柄出错'.format(step=step)
            self.logger.to_log('info', error_message + '=>' + repr(e))
            return False, error_message

    # 申报步骤
    def to_declare_step(self, step):
        time.sleep(2)
        try:
            self.logger.to_log('info', '步骤{step}开始'.format(step=step))
            self.driver.switch_to.default_content()
            self.helper.to_declare(self.info['table_name'])
            self.general.save_result_img()
            return True, '执行申报步骤成功'
        except Exception as e:
            self.general.save_result_img()
            error_message = '步骤{step}：申报出错'.format(step=step)
            self.logger.to_log('info', error_message + '=>' + repr(e))
            return False, error_message

    # 缴税步骤
    def to_pay_step(self, step):
        time.sleep(2)
        try:
            self.logger.to_log('info', '步骤六开始')
            result = self.helper.to_pay()
            if result is False:
                self.logger.to_log('info', '无需缴款')
            self.general.save_result_img()
            self.logger.to_log('info', '步骤六结束')
        except Exception as e:
            self.general.save_result_img()
            error_message = '步骤{step}：缴款出错'.format(step=step) + repr(e)
            self.logger.to_log('info', error_message)
            raise Exception(error_message)

    # 获取回执步骤
    # type = [1,2,3] 1申报查询、2缴款查询、3财报查询
    def to_check_step(self, step, result_type):
        time.sleep(2)
        try:
            self.logger.to_log('info', '步骤{step}开始'.format(step=step))
            try:
                self.driver.find_element_by_class_name('layui-layer-close').click()
            except:
                pass
            self.helper.check_result(result_type)
            return True, '执行回执步骤成功'
        except Exception as e:
            self.general.save_result_img()
            error_message = '步骤{step}：获取回执出错'.format(step=step)
            self.logger.to_log('info', error_message + '=>' + repr(e))
            return False, error_message

    def to_js(self):
        js = '''
        var layer;
        layui.use(['laydate','layer'], function(){
            var sbny = tjNd + '-' +tjYf;
            var laydate = layui.laydate;
            layer = layui.layer;
            //年月选择器
            laydate.render({
                elem: '#test3'
                ,type: 'month'
                ,value: sbny
                ,isInitValue: true
                ,show: false
                ,btns: ['now', 'confirm']
                ,done: function(value, date){
                    var sksq = value; 
                    var href = window.location.href;
                    if (href.indexOf("?") > 0) {
                        href = href.substr(0, href.indexOf("?"));
                    }
                    if (href.indexOf(";") > -1) {
                        href = href.substr(0, href.indexOf(";"));
                    }
                    href = href+"?tjNd="+sksq.substr(0, 4)+"&tjYf="+sksq.substr(5, 6)+"&gdslxDm="+gdslxDm+"&token=" + token + "&yypt_nsrsbh="
                    + yypt_nsrsbh + "&appid=" + appid;
                    window.location.href = href; 
                }
            });
        });
        '''
        self.driver.execute_script(js)
        self.driver.find_element_by_class_name('layui-date-input').click()
        time.sleep(1)
        js = "document.querySelectorAll('.layui-laydate li')[3].click()"
        self.driver.execute_script(js)
        time.sleep(1)
        js = "document.querySelectorAll('.laydate-footer-btns span')[1].click()"
        self.driver.execute_script(js)
        time.sleep(1)

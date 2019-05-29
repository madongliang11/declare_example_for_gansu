"""
CA机柜的操作
"""
import time
import win32gui
from common.Analog import Analog


class Operation(object):
    def __init__(self):
        self.analog = Analog()
        self.hub_hwnd = None
        self.no_button_list = None
        self.close_button_hwnd = None
        self.switch_button_hwnd = None
        self.com_list = None

    # 获取hub句柄
    def get_hub_hwnd(self):
        self.hub_hwnd = self.analog.get_hwnd(
            window_class='WindowsForms10.Window.8.app.0.378734a', window_title='U盾多选一系统 -上海智豹出品')
        return self.hub_hwnd

    # 获取所有插口按钮句柄
    def get_no_button_list(self):
        if self.hub_hwnd is None:
            self.get_hub_hwnd()
        close_button = win32gui.FindWindowEx(
            self.hub_hwnd, None, 'WindowsForms10.BUTTON.app.0.378734a', None)
        all_no_button = win32gui.FindWindowEx(
            self.hub_hwnd, close_button, 'WindowsForms10.Window.8.app.0.378734a', None)
        self.no_button_list = self.analog.get_all_child_windows(all_no_button)
        return self.no_button_list

    # 点击插口按钮
    # param no 序号 1~100
    def click_button_in_no(self, no):
        button_total = 100
        if self.no_button_list is None:
            self.get_no_button_list()
        if 0 < no <= 100:
            no = button_total - int(no)
            button_hwnd = self.no_button_list[no]
            self.analog.simulate_click(button_hwnd)

    # 获取“全部关闭”按钮句柄
    def get_close_button_hwnd(self):
        if self.hub_hwnd is None:
            self.get_hub_hwnd()
        self.close_button_hwnd = win32gui.FindWindowEx(
            self.hub_hwnd, None, 'WindowsForms10.BUTTON.app.0.378734a', None)
        return self.close_button_hwnd

    # 点击“关闭全部”按钮
    def click_close_button(self):
        if self.close_button_hwnd is None:
            self.get_close_button_hwnd()
        self.analog.simulate_click(self.close_button_hwnd)

    # 获取打开/关闭串口开关句柄
    def get_switch_button_hwnd(self):
        if self.hub_hwnd is None:
            self.get_hub_hwnd()
        close_button_hwnd = win32gui.FindWindowEx(
            self.hub_hwnd, None, 'WindowsForms10.BUTTON.app.0.378734a', None)
        no_button_div_hwnd = win32gui.FindWindowEx(
            self.hub_hwnd, close_button_hwnd, 'WindowsForms10.Window.8.app.0.378734a', None)
        com_div_hwnd = win32gui.FindWindowEx(
            self.hub_hwnd, no_button_div_hwnd, 'WindowsForms10.Window.8.app.0.378734a', None)
        self.switch_button_hwnd = win32gui.FindWindowEx(
            self.hub_hwnd, com_div_hwnd, 'WindowsForms10.BUTTON.app.0.378734a', None)
        return self.switch_button_hwnd

    # 点击打开/关闭串口开关
    def click_switch_button(self):
        if self.switch_button_hwnd is None:
            self.get_switch_button_hwnd()
        self.analog.simulate_click(self.switch_button_hwnd)

    # 获取所有的com对象句柄
    def get_all_com_radio(self):
        if self.hub_hwnd is None:
            self.get_hub_hwnd()
        close_button_hwnd = win32gui.FindWindowEx(
            self.hub_hwnd, None, 'WindowsForms10.BUTTON.app.0.378734a', None)
        no_button_div_hwnd = win32gui.FindWindowEx(
            self.hub_hwnd, close_button_hwnd, 'WindowsForms10.Window.8.app.0.378734a', None)
        com_div_hwnd = win32gui.FindWindowEx(
            self.hub_hwnd, no_button_div_hwnd, 'WindowsForms10.Window.8.app.0.378734a', None)
        self.com_list = self.analog.get_all_child_windows(com_div_hwnd)
        return self.com_list

    # 点击com
    # param no 序号 1~6
    def click_com(self, no):
        if 0 < no <= 6:
            no -= 1
            if self.com_list is None:
                self.get_all_com_radio()
            self.analog.simulate_click(self.com_list[no])


if __name__ == '__main__':
    # 使用前请务必打开hub软件
    # 1.打开开关
    # 2.打开插口按钮
    # 3.关闭所有按钮
    # 4.打开另一个插口按钮...
    opera = Operation()
    opera.click_switch_button()
    time.sleep(1)
    opera.click_button_in_no(1)
    time.sleep(1)
    opera.click_close_button()

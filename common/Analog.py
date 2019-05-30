#
# _*_ coding:UTF-8 _*_
# pywin32基类
import win32api
import win32con
import win32gui
import win32clipboard
from ctypes import *
import time

CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '+': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0
}


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


class Analog(object):
    def __init__(self):
        pass

    # 获取鼠标坐标
    @staticmethod
    def get_mouse_point():
        po = POINT()
        windll.user32.GetCursorPos(byref(po))
        return int(po.x), int(po.y)

    # 获取窗口句柄
    # param window_class 窗口类名（使用spy++获取）
    # param window_title 窗口标题（使用spy++获取）
    @staticmethod
    def get_hwnd(window_class=None, window_title=None):
        if window_class is None and window_title is None:
            return 0
        return win32gui.FindWindow(window_class, window_title)

    # 获取子窗口句柄
    # param parent_hwnd  父级窗口
    # param window_class 窗口类名
    @staticmethod
    def get_child_hwnd(parent_hwnd, window_class):
        return win32gui.FindWindowEx(parent_hwnd, None, window_class, None)

    # 遍历子窗口
    # param parent 父级窗口句柄
    @staticmethod
    def get_all_child_windows(parent):
        if not parent:
            return
        hwnd_child_list = []
        win32gui.EnumChildWindows(
            parent, lambda hwnd, param: param.append(hwnd), hwnd_child_list)
        return hwnd_child_list

    # 获取窗口的宽度和高度
    @staticmethod
    def get_window_rect(hwnd=0):
        width = 0
        height = 0
        if hwnd != 0:
            # rect (左上角坐标x，左上角坐标y，右下角x，右下角y)
            rect = win32gui.GetWindowRect(hwnd)
            width = rect[2] - rect[0]
            height = rect[3] - rect[1]
        return width, height

    # 移动窗口
    def move_window(self, hwnd, x=0, y=0):
        width, height = self.get_window_rect(hwnd)
        win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM,
                              x, y, width, height, win32con.SWP_SHOWWINDOW)

    # 关闭窗口
    # param hwnd 窗口句柄
    @staticmethod
    def close_window(hwnd=0):
        if hwnd != 0:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    # 最大化窗口
    # param hwnd 窗口句柄
    @staticmethod
    def max_window(hwnd=0):
        if hwnd != 0:
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

    # 获取window对象标题
    # param hwnd 对象句柄
    @staticmethod
    def get_window_title(hwnd):
        if hwnd != 0:
            return win32gui.GetWindowText(hwnd)

    # 获取window对象类名
    # param hwnd 对象句柄
    @staticmethod
    def get_window_class(hwnd):
        if hwnd != 0:
            return win32gui.GetClassName(hwnd)

    # 鼠标单击
    # param x 坐标x
    # param y 坐标y
    def mouse_click(self, x=None, y=None):
        if x is not None and y is not None:
            self.mouse_move(x, y)
            time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # 使用虚拟键盘模拟鼠标点击window对象
    # param hwnd 窗口句柄
    @staticmethod
    def simulate_click(hwnd=0):
        if hwnd != 0:
            win32gui.PostMessage(hwnd, win32con.BM_CLICK,
                                 win32con.VK_LBUTTON, 0)

    # 鼠标双击
    # param x 坐标x
    # param y 坐标y
    def mouse_double_click(self, x=None, y=None):
        if x is not None and y is not None:
            self.mouse_move(x, y)
            time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # 移动鼠标
    # param x 坐标x
    # param y 坐标y
    @staticmethod
    def mouse_move(x, y):
        windll.user32.SetCursorPos(x, y)

    # 输入字符串
    # param input_string 要输入的字符串
    @staticmethod
    def key_input_string(input_string=''):
        for c in input_string:
            win32api.keybd_event(CODE[c], 0, 0, 0)
            win32api.keybd_event(CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.01)

    # 组合键
    # param keys 按键数组（代码见CODE）
    @staticmethod
    def key_input_multi(keys=[]):
        for k in keys:
            win32api.keybd_event(CODE[k], 0, 0, 0)
        time.sleep(0.5)
        for k in keys:
            win32api.keybd_event(CODE[k], 0, win32con.KEYEVENTF_KEYUP, 0)

    # 获取当前坐标rgb颜色
    # param x 坐标x
    # param y 坐标y
    @staticmethod
    def get_color(x, y):
        window_dc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
        i_color = int(win32gui.GetPixel(window_dc, x, y))
        # 返回RGB值
        # return (i_color & 0xff, (i_color >> 8) & 0xff,
        #         (i_color >> 16) & 0xff)
        return i_color

    @staticmethod
    def convert_color(color):
        if isinstance(color, tuple) and len(color) == 3:
            color = color[0] + (color[1] << 8) + (color[2] << 16)
        elif isinstance(color, int):
            color = (color & 0xff, (color >> 8) & 0xff, (color >> 16) & 0xff)
        return color

    @staticmethod
    def set_clipboard(text):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()

    @staticmethod
    def get_clipboard():
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data


import ctypes
import sys
import time

import cv2
import numpy
from PIL import ImageGrab

img_templ = cv2.imread('play_button.jpg')
THRESHOLD = 0.97


def main_loop():
    img_src = ImageGrab.grab(bbox=(80, 45, 110, 85))
    img_src = cv2.cvtColor(numpy.asarray(img_src), cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(img_src, img_templ, cv2.TM_CCOEFF_NORMED)
    min_max = cv2.minMaxLoc(result)
    print("result.min_max:", min_max)

    if min_max[1] > THRESHOLD:
        print("处于对话状态, 模拟鼠标单击")
        ctypes.windll.user32.mouse_event(2)
        time.sleep(0.1)
        ctypes.windll.user32.mouse_event(4)


if __name__ == "__main__":
    print("Hello")

    if ctypes.windll.shell32.IsUserAnAdmin():
        print("当前已经是管理员权限了")
        while True:
            main_loop()
    else:
        print("当前不是管理员权限, 请以管理员权限启动新进程....")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

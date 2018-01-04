 #-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import math
import time
import os

#定义
def pull_screenshot():
'''截取手机屏幕并发送到电脑函数'''
os.system('adb shell screencap -p /sdcard/autojump.png')
#发送截屏命令到手机
os.system('adb pull /sdcard/autojump.png .')
'''发送拉取图片到电脑命令

定义'''

def jump(distance):


'''跳跃函数
形参为距离'''
press_time = distance * 1.35
'''计算按屏幕
时间'''
press_time = int(press_time)
cmd = 'adb shell input swipe 320 410 320 410 ' + str(press_time)
'''按屏幕命令'''
print(cmd)
os.system(cmd)
'''发送
按屏幕命令'''

fig = plt.figure()
'''创建一个新的图像对象（窗口）'''
index = 0
cor = [0, 0]

pull_screenshot()
'''执行截屏函数'''
img = np.array(Image.open('autojump.png'))
Image.open'''读取图片
到名为
img
的图片数组'''

update = True
click_count = 0
cor = []


def update_data():  '''定义更新数据的函数


更新图片'''
return np.array(Image.open('autojump.png'))

im = plt.imshow(img, animated=True)
im = ''''绘制图像（数组名、动画 = 打开）'''


def updatefig(*args):
    global update
    if update:
        time.sleep(1.5)
        pull_screenshot()
        im.set_array(update_data())
        update = False
    return im,


def onClick(event):
    global update
    global ix, iy
    global click_count
    global cor
    
    # next screenshot
    
    ix, iy = event.xdata, event.ydata
    coords = []
    coords.append((ix, iy))
    print('now = ', coords)
    cor.append(coords)
    
    click_count += 1
    if click_count > 1:
        click_count = 0
        
        cor1 = cor.pop()
        cor2 = cor.pop()
        
        distance = (cor1[0][0] - cor2[0][0]) ** 2 + (cor1[0][1] - cor2[0][1]) ** 2
        distance = distance ** 0.5
        print('distance = ', distance)
        jump(distance)
        update = True


fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
#import 模块
import os
import sys
import random

#from 模块 import 功能 ：部分导入
from datetime import date

print(os.getcwd())
print(sys.platform)
print(sys.version)

name = random.choice(['python','java','c']) #从列表中随机选择数据
print(name)
print(random.random())

#100中随机产生10个数字
print(random.sample(range(100),10))

#获取今日日期
print(date.today())
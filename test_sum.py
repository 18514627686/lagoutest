def sum(*kwargs):

    total = 0

    for ele in kwargs:

        total = total + ele

    return total
'''
sum_data = lambda kwargs : [ele+ele for ele in kwargs]

print(sum_data([1,2,3]))

print(sum(1,2,3))
'''

import time

# 这个是外函数

def record_time(func):

    def wrapper(*kwargs):

        print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))

        total = func(*kwargs)

        print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))

        return total

    return wrapper

# 这个是我们真正的功能函数
@record_time
def sum(*kwargs):

    total = 0

    for ele in kwargs:

        total = total + ele

    time.sleep(2)

    return total

if __name__ == "__main__":

    # 外函数，内函数，和功能函数一起，实现了不改变功能函数的前提下，给功能函数加功能的操作。

    #print(record_time(sum)(1,2,3,4))
    print(sum(1,2,3,4))

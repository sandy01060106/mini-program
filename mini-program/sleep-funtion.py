#然後在 1 秒後打印，然後在 2、3 秒後打印，然後程序打印出消息“循環結束”並停止。

import time
a=0
while a<=3:
    print('hello')
    time.sleep(a)
    if a==3:
        print("End of the Loop")
        break
    a+=1
'''
解法二
import time
a=0
while True:
    if a<=3:
        print('hello')
        time.sleep(a)
        a += 1
    else:
        print("End of the Loop")
        break
解法三
a=0
while True:
    print('hello)
    a+=1
    if a>3:
        print("End of the Loop")
        break
    time.sleep(a)
'''
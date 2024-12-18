import random
import string
密碼長度 = int(input('請輸入想設定的密碼位數'))
數字= string.digits
英文字母 = string.ascii_letters
字母表= list(數字+英文字母)
#print(字母表)
random.shuffle(字母表)
print(字母表)
密碼=字母表[:密碼長度]
print(密碼)

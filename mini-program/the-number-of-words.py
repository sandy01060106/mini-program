'''
Create a function that takes any string as input and returns the number of words for that string.
'''
a=input('請輸入文字')

def number(str):
    #print(str.split(' '))
    #word=str.split(' ')
    #number=len(word)
    #print(number) 可簡化為下行
    print(len(str.split(' ')))
number(a)
'''
解法二
def count_words(strng):
    strng_list = strng.split()
    return len(strng_list)

print(count_words(a))
'''
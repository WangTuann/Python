import math


arr=[1,22,25,3,5,7,9,45,95,8,2]

def isOdd(i):
    return i and 1
def TichSoLe(list):
    mul = 1
    for i in list:
        if (isOdd(i) == 1) and (i%3!=0):
            mul *=i
    print(mul)
            
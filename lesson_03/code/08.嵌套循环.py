# 练习1：打印99乘法表
# i = 9
# while i > 0:
#     j = 9
#     while j > 0:
#         print(i, "x", j, "=", i * j)
#         j -= 1
#     i -= 1


# 练习2：100以内所有质数
from time import time

begin = time()
i = 2
while i <= 10000:
    num = int(i ** 0.5)
    flag = True
    while num > 1:
        if (i % num) == 0:
            flag = False
            break
        num -= 1
    if (flag):
        print(i, "是质数")
    i += 1
print(time() - begin)

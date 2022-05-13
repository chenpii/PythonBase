# 练习1：100以内奇数和
# sum = 0
# i = 10
# while i > 0:
#     if i % 2 == 1:
#         sum += i
#     i -= 1
# print("100以内奇数和:", sum)


# 练习2：100以内7的倍数之和，及个数
# sum = 0
# count = 0
# i = 100
# while i > 0:
#     if i % 7 == 0:
#         sum += i
#         count += 1
#     i -= 1
# print("100以内7的倍数之和:", sum, "，个数为：", count)


# 练习3：1000以内的水仙花数
# i = 1
# while i <1000:
#     if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
#         print(i, "是水仙花数")
#     i += 1


# 练习4：判断质数
num = int(input("请输入一个整数"))
i = int(num ** 0.5)
bool = True
while i > 1:
    if num % i == 0:
        bool = False
        break
    i -= 1
if (bool):
    print(num, "是质数")
else:
    print(num, "不是质数")

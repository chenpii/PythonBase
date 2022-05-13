# 练习1 从控制台输入一个数字，判断奇偶
# num = int(input("请输入一个整数"))
# if num % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")

# 练习2 从控制台输入年份，判断是否闰年
# year = int(input("请输入一个年份"))
# if year % 400 == 0:
#     print(year, "是闰年")
# else:
#     print(year, "不是闰年")

# 练习3 控制台输入狗的年龄，输出相当于多大人的年龄
# 狗的前2年相当于人的10.5岁，然后每增加1年就增加4岁
# age = int(input("请输入狗的年龄："))
# if age <= 2:
#     people_age = 10.5
# else:
#     people_age = 10.5 + (age - 2) * 4
# print("相当于", people_age, "岁的人")

# 练习4 键盘输入小明的期末成绩：
# 当100时，奖励一辆车
# 当[80-99]时，奖励手机
# 当[60-79]时，奖励书
# 其他时，什么也没有
# score = int(input("请输入小明的期末成绩(0-100)："))
# if score == 100:
#     print("奖励一辆车")
# elif score >= 80:
#     print("奖励手机一部")
# elif score >= 60:
#     print("奖励书一本")
# else:
#     print("奖励巴掌一个")

# 练习5 条件
# 高：180cm以上；富：50w以上；帅：500以上
# 三个条件均满足：精英
# 三个条件有真的情况:高质量
# 均不满足：普通
high = int(input("身高"))
rich = int(input("财富"))
look = int(input("长相"))
if high >= 180 and rich >= 50 and look >= 500:
    print("精英")
elif high >= 180 or rich >= 50 or look >= 500:
    print("高质量")
else:
    print("普通")

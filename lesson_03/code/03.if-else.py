# 让用户在控制台中输入年龄，若超过18岁，则输出已成年，否则输出未成年。
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已成年")
else:
    print("您还未成年")
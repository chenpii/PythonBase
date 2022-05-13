# 让用户在控制台中输入年龄，判断成年、中年、老年、退休
age = int(input("请输入您的年龄："))
if age < 18:
    print("您未成年")
elif age < 30:
    print("您已成年")
elif age < 50:
    print("您已到中年")
elif age < 60:
    print("您已老年")
else:
    print("退休的年纪")

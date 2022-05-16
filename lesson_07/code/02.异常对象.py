l=list
try:
    print(c)
    l[10]
    print(10/0)
except NameError:
    #异常处理
    print(" 出现 NameError 异常")

except ZeroDivisionError:
    print(" 出现 ZeroDivisionError 异常")

except:
    print(" 出现 其他 异常")

else:
    print("没有异常")

print("异常出现后")

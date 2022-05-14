# EMS（Employee Manager System 员工管理系统）命令行版
emps = ["\t01\tRoss\t28\t男\t纽约"]
while True:
    print("-" * 20, "欢迎使用员工管理系统", "-" * 20)
    print("请选择要做的操作：")
    print("\t1.查询员工")
    print("\t2.添加员工")
    print("\t3.删除员工")
    print("\t4.退出系统")
    user_choice = input("请选择[1-4]:")
    print("-" * 62)
    # 查询员工
    if user_choice == "1":
        print("\t序号\t姓名\t年龄\t性别\t住址")
        for emp in emps:
            print(emp)


    # 添加员工
    elif user_choice == "2":

        pass

    # 删除员工
    elif user_choice == "3":
        pass

    # 退出系统
    elif user_choice == "4":
        print("谢谢使用，再见！")
        break
    else:
        print("您的输入有误，请重新输入！")
print("-" * 62)

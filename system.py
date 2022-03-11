# 项目时间：2022/3/11 10:15
import os
filename='student.txt'
def main():
    while True:
        menu()
        choice = int(input('请选择功能：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？Y/N')
                if answer == 'y' or answer == 'Y':
                    print('感谢您的使用！')
                    break
                else:
                    continue
            if choice == 1:
                insert()
            if choice == 2:
                search()
            if choice == 3:
                delete()
            if choice == 4:
                modify()
            if choice == 5:
                sort()
            if choice == 6:
                total()
            if choice == 7:
                show()


def menu():
    print('=========================学生信息管理系统==========================')
    print(' ----------------------------功能菜单----------------------------')
    print('\t\t\t\t\t1、录入学生信息')
    print('\t\t\t\t\t2、查找学生信息')
    print('\t\t\t\t\t3、删除学生信息')
    print('\t\t\t\t\t4、修改学生信息')
    print('\t\t\t\t\t5、排序')
    print('\t\t\t\t\t6、统计学生总数')
    print('\t\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t\t0、退出系统')
    print('----------------------------------------------------------------')


def insert():
    student_lst=[]
    while  True:
        id=input('请输入ID(如1001):')
        if not id:
            continue
        name=input('请输入姓名:')
        if not name:
            continue
        try:
            english=int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩:'))
            java = int(input('请输入Java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入！')
            continue
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_lst.append(student)
        answer=input('是否继续添加？Y/N')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    save(student_lst)
    print('学生信息录入完毕！')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    pass


def delete():
    while True:
        student_id=input('请输入要删除的学生ID：')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'ID为{student_old}的学生信息已经被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()
            answer=input('是否继续删除？Y/N')
            if answer=='y'or answer=='Y':
                continue
            else:
                break
def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    main()

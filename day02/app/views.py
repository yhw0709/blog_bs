from django.db.models import Avg
# from django.shortcuts import render
from django.http import HttpResponse
from app.models import Student2, StudentInfo, Grade, Course


def create_stu():
    # 创建学生信息
    # 引入ORM概念:对象关系映射
    # 第一种
    # Student2.objects.create(s_name='Mark')
    # 第二种
    # stu = Student2()
    # stu.s_name = '王小妹'
    # stu.save()
    # 第三种
    # 初始化
    # stu = Student2()
    # stu.save()
    return HttpResponse('创建学生方法')


def select_stu():
    # 查询数据
    """

    """
    # select * from app_student
    stus = Student2.objects.all()
    # 获取学生的姓名
    for stu in stus:
        print(stu.s_name)

    # select * from xxx where s_name=''
    stu_m = Student2.objects.filter(s_name='mark')
    print(stu_m)

    # 查询年纪为19的学生
    stu_s = Student2.objects.filter(s_age=19)
    stu_names = [stu.s_name for stu in stu_s]
    for name in stu_names:
        print(name)

    # 姓名不等于xx
    # stu_e = Student2.objects.exclude(s_name='john')

    # 排序,按照id升序/降序===>asc/desc
    stus = Student2.objects.all().order_by('-id')
    # stus = Student2.objects.all().order_by('-id')---降序
    stu_info = [(stu.s_name, stu.id) for stu in stus]
    for info in stu_info:
        print(info)

    # values()
    # stus = Student2.objects.all().values('id', 's_name')

    # get(),first()
    # stus = Student2.objects.get(id=1)
    # stus = Student2.objects.filter(id=1).first()  #更加安全

    # stus = Student2.objects.filter(s_name__contains='e').values('id', 's_name')
    # stus = Student2.objects.filter(s_name__endswith='e').values('id', 's_name')
    # stus = Student2.objects.filter(s_name__startswith='M').values('id', 's_name')

    # Q(),查询姓名叫joe或者年纪=19的学生
    # stus = Student2.objects.filter(Q(s_name='joe') | Q(s_age=18)).values('id', 's_name')
    # ~   表示取非

    # 查询语文成绩比数学成绩低10分的学生信息

    # stus = Student2.objects.filter(math__gt=F('chinese') + 10).values('id', 's_name')

    avg_math = Student2.objects.aggregate(Avg('math'))
    print(avg_math)

    return HttpResponse(stus)


def delete_stu():
    # 删除
    # stu = Student2.objects.get(pk=1)
    # stu.delete()
    # Student2.objects.get(pk=2).first().delete()
    return HttpResponse('删除')


def update_stu():
    # 更新
    # stu = Student2.objects.get(pk=2)
    # stu.s_name = '帅逼'
    # stu.save()
    # 第二种
    Student2.objects.filter(id=3).update(s_age=17)
    return HttpResponse('修改')


def create_stu_info(request):
    if request.method == 'GET':
        data = {
            '18200384770': '金牛区',
            '18200384771': '金牛区',
            '18200384772': '金牛区',
            '18200384773': '金牛区',
            '18200384774': '金牛区',
        }
        for k, v in data.items():
            StudentInfo.objects.create(tel=k, address=v)
        return HttpResponse('创建副表')
    if request.method == 'POST':
        pass


def stu_add_stuinfo(request):
    if request.method == 'GET':
        # 给id为2的学生添加拓展表中id=2的信息,
        # stu = Student2.objects.get(id=2)
        # stu.stu_info_id = 2
        # stu.save()
        # 方法二
        stu = Student2.objects.get(id=6)
        stu.stu_info = StudentInfo.objects.get(id=1)
        stu.save()
        return HttpResponse('绑定学生和拓展表的关系')


def sel_tel_by_stu(request):
    if request.method == 'GET':
        # 获取id为2的学生的手机号
        # 方法一
        # stu = Student2.objects.filter(id=2).first()
        # info_id = stu.stu_info_id
        # stu_info = StudentInfo.objects.get(pk=info_id)
        # 方法二
        # stu = Student2.objects.get(id=2)
        # stu_info = stu.stu_info
        # tel = stu_info.tel
        # print(tel)
        # 方法三
        stu = Student2.objects.get(id=2)
        print(stu.stu_info.tel)

        return HttpResponse('通过学生查找手机号')


def sel_stu_by_tel(request):
    if request.method == 'GET':
        # 通过手机号查找学生
        stu_info = StudentInfo.objects.get(tel='18200384770')
        print(stu_info.stu.s_name)

        return HttpResponse('通过手机号查找学生')


def create_grade(request):
    if request.method == 'GET':
        g = Grade()
        g.g_name = 'RTX2080'
        g.save()

        return HttpResponse('创建班级')


def sel_stu_by_grade(request):
    if request.method == 'GET':
        # 查询python1805的学生，获取姓名
        g = Grade.objects.get(g_name='python1805')
        stus_names = g.stu.values('s_name')
        print(stus_names)

        stu = Student2.objects.filter(s_name='jerry').first()
        grade = stu.g.g_name
        print(grade)

        return HttpResponse('根据班级查找学生')


def create_course(request):
    if request.method == 'GET':
        c = Course()
        c.c_name = 'python'
        c.save()

        return HttpResponse('创建课程')


def create_stu_course(request):
    if request.method == 'GET':
        # 让jerry选择课程(python)
        # stu = Student2.objects.get(s_name='jerry')
        # 添加add方法
        # stu.c.add(1)

        # 添加java和id=4的学生的关联关系
        c = Course.objects.get(c_name='java')
        c.student2_set.add(4)

        return HttpResponse('创建学生课程关联')


def del_stu_course(request):
    if request.method == 'GET':
        # 删除关联
        c = Course.objects.get(c_name='java')
        c.student2_set.remove(4)

        return HttpResponse('删除学生课程关联')

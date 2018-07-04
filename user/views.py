import json,os

from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,response
from user.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from Django.my_decorator import login_required
# Create your views here.
import gvcode



#获取base64码
def get_code(request):
    base64_code,str_code = gvcode.base64()
    resp_date = {}
    bc = str(base64_code)
    resp_date['base64_code'] = bc
    resp_date['str_code'] = str_code
    return HttpResponse(json.dumps(resp_date))


def home(request):
    l = request.session.get('login_state')
    u = request.session.get('username')
    info = {}
    info['login_state'] = l
    info['user'] = u
    try:
        user = User.objects.get(username=u)
    except:
        return render(request, 'layouts/base.html', info)
    info['img'] = user.img
    return render(request,'layouts/base.html',info)
#注册
def register(request):

    if request.method == 'GET':
        msg = '欢迎注册！'
        return render(request, 'user/register.html',
                      context={'msg': msg, })

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        repassword = request.POST.get('repassword')
        str_code1 = request.POST.get('str_code1')
        str_code2 = request.POST.get('str_code2')
        if not(username and password and str_code1):
            msg = '用户名、密码、验证码不能为空！'
            return render(request, 'user/register.html',
                          context={'msg': msg, })
        if password != repassword:
            msg = '两次输入密码不一致！'
            return render(request,'user/register.html',
                          context={'msg':msg,})
        if str_code1 != str_code2:
            msg = '验证码错误！'
            return render(request,'user/register.html',
                          context={'msg':msg,})
        password = make_password(password,'password')
        print('make',password)
        try:
            user = User.objects.get(username=username)
        except:
            new_user = User(username=username, password=password)
            new_user.save()

            return redirect(login)
        # print(user)
        if user.username == username:
            msg = '该用户已存在！'
            return render(request, 'user/register.html',
                          context={'msg': msg, })
        msg = '注册成功，请登陆！'
        return render(request,'user/register.html',{'msg':msg})

#登陆
def login(request):

    if request.method == 'GET':
        msg = '欢迎登陆！'
        login_state = 0
        return render(request, 'user/login.html', {"msg": msg})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (username and password):
            msg = '用户名,密码不能为空！'
            return render(request, 'user/login.html', {"msg": msg})
        # password = make_password(password, 'password')
        print('check',password)
        try:
            user = User.objects.get(username=username)
        except:
            msg = "用户名不存在!"
            return render(request, 'user/login.html', {"msg": msg})
        if check_password(password,user.password):
            login_state = 1
            request.session['login_state'] = login_state
            request.session['username'] = user.username
            request.session['user_id'] = user.id
            # request.session['img'] = user.img
            request.session.set_expiry(6000)
            return render(request, 'layouts/base.html',
                          context={'user': user.username,
                                   'img':user.img,
                                   'login_state': login_state})
        else:
            msg = "密码错误!"
            return render(request, 'user/login.html', {"msg": msg})


#登出
def logout(request):
    login_state = 0
    request.session['login_state'] = login_state
    request.session.flush()
    return redirect(home)

#用户信息
@login_required
def user_info(request):
    l = request.session.get('login_state')
    u = request.session.get('username')
    if request.method == 'GET':
        user = User.objects.get(username=u)

        #缩放图片
        # from PIL import Image
        # im = Image.open(user.img.url)
        # w,h=im.size
        # im.thumbnail((w//4,h//4))
        info = {}
        info['login_state'] = l
        info['user'] = u
        info['email'] = user.email
        info['tel'] = user.tel
        info['sex'] = user.sex
        info['img'] = user.img

        info['age'] = user.age
        info['created_at'] = user.created_at
        return render(request,'user/user_info.html',info)

#更新信息
@login_required
def update_user_info(request):
    l = request.session.get('login_state')
    u = request.session.get('username')
    user = User.objects.get(username=u)
    info = {}

    info['login_state'] = l
    info['user'] = u
    info['email'] = user.email
    info['tel'] = user.tel
    info['sex'] = user.sex
    info['img'] = user.img
    info['age'] = user.age

    if request.method == 'GET':
        return render(request,'user/update_user_info.html',info)
    elif request.method == "POST":
        date = request.POST
        submit = date.get('save')

        if submit == '取消':
            return redirect(user_info)
        user = User.objects.get(username = u)
        tel = date.get('tel')
        email = date.get('email')
        sex = date.get('sex')
        #获取文件
        try:
            img_p = request.FILES['img']
            file = user.img.url[1:]
            print('cccccccccc',file)
            if file.split('/')[-1] == 'default.jpg':
                pass
            else:
                os.remove(file)
            # print('ddddddd',file)
        except:
            img_p = user.img
        age = date.get('age')
        user.tel = tel
        user.email = email
        user.age = age
        user.sex = sex
        user.img = img_p
        user.save()
        return redirect(user_info)
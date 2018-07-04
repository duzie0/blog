from django.shortcuts import render,redirect
from django.http import HttpResponse
from Django.my_decorator import login_required
from blog.models import Blog
from user.models import User
import datetime,pytz
# Create your views here.
@login_required
def blog(request):
    u = request.session.get('username')
    l = request.session.get('login_state')
    user = User.objects.get(username=u)
    img = user.img
    info = {}
    info['login_state'] = l
    info['user'] = u
    info['img'] = img
    blogs1 = []
    blogs2 = []
    list = []
    if request.method == 'GET':
        blogs = Blog.objects.filter(author=user)
        num = 0
        for blog in blogs[::-1]:
            num = num+1
            # tz = pytz.timezone('Asia/shanghai')
            print('ccccccccccccccc',type(blog.created_at))
            create_time = datetime.datetime.strftime(blog.created_at,'%Y-%m-%d %H:%M')
            blog.created_at = create_time
            print('aaaaaaaaaa', blog.created_at,create_time)
            blogs1.append(blog)
            list.append(blog.view_times)
        list.sort(reverse=True)
        for l in list:
            for b in blogs:
                if l == b.view_times:
                    print('aaaaaaaaaaaaaaaa',type(b.created_at),b.created_at)
                    create_time = datetime.datetime.strftime(b.created_at, '%Y-%m-%d %H:%M')
                    b.created_at = create_time
                    blogs2.append(b)
        info['blogs'] = blogs1
        info['blogs2'] = blogs2
        info['num'] = num

        return render(request,'blog/blog.html',info)
    elif request.method == 'POST':

        return  render(request,'blog/blog.html',info)

@login_required
def blog_page(request,pk):
    u = request.session.get('username')
    l = request.session.get('login_state')
    user = User.objects.get(username=u)
    img = user.img
    info = {}
    info['login_state'] = l
    info['user'] = u
    info['img'] = img
    if request.method == 'GET':
        blog = Blog.objects.get(pk=pk)
        blog.view_times = blog.view_times + 1
        info['blog'] = blog
        blog.save()
        create_time = datetime.datetime.strftime(blog.created_at, '%Y-%m-%d %H:%M')
        blog.created_at = create_time
        info['times'] = blog.view_times
        return render(request,'blog/blog_page.html',info)
    elif request.method == 'POST':

        return  render(request,'blog/blog.html',info)


@login_required
def create_blog(request):
    u = request.session.get('username')
    l = request.session.get('login_state')
    user = User.objects.get(username=u)
    img = user.img
    info = {}
    info['login_state'] = l
    info['user'] = u
    info['img'] = img
    if request.method == 'GET':
        info['msg'] = '欢迎创建新博客！'
        return render(request,'blog/create_blog.html',info)
    elif request.method == 'POST':
        data = request.POST
        submit = data.get('submit')
        title = data.get('title')
        summary = data.get('summary')
        content = data.get('content')
        if submit == '取消':
            return redirect(blog)
        error = ''
        if not title:
            error = '标题不能为空！'
        if not (summary or error):
            error = '摘要不能为空！'
        if not (content or error):
            error = '内容不能为空！'
        if error:
            info['msg'] = error
            return render(request,'blog/create_blog.html',info)
        new_blog = Blog(author=user,title=title,summary=summary,content=content)
        new_blog.save()
        info['msg'] = '创建成功！'
        return render(request,'blog/create_blog.html',info)

@login_required
def update_blog(request):
    return HttpResponse('update')
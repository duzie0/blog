from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from Django.my_decorator import login_required
from user.models import User
from .models import Album

# Create your views here.
@login_required
def album(request):
    l = request.session.get('login_state')
    u = request.session.get('username')
    user = User.objects.get(username=u)
    info = {}
    info['login_state'] = l
    info['user'] = u
    info['img'] = user.img
    return render(request,'album/album.html',info)

@login_required
def create_album(request):
    l = request.session.get('login_state')
    u = request.session.get('username')
    i = User.objects.get(username=u).img
    if request.method == 'GET':
        msg = '欢迎创建新相册！'
        return render(request, 'album/create_album.html',
                      {'msg':msg,'login_state':l,'user':u,'img':i})
    elif request.method == 'POST':
        data = request.POST
        username = request.session.get('username')
        author = User.objects.get(username=username)
        title = data.get('title')
        description = data.get('description')
        if not (title and description):
            msg = '标题和描述不能为空！'
            return render(request, 'album/create_album.html',
                          {'msg': msg, 'login_state': l, 'user': u,'img':i})
        try:
            img = request.FILES['img']
        except:
            msg = '请选择要上传的封面！'
            return render(request, 'album/create_album.html',
                          {'msg': msg, 'login_state': l, 'user': u,'img':i})
        #author 是User对象
        print('llllllllllllllllllllllllllllll')
        album = Album(author=author,title=title,description=description,
                      img=img)
        album.save()
        msg = '创建相册成功！'
        return render(request,'album/create_album.html',
                      {'msg':msg,'login_state':l,'user':u})

@login_required
def update_album(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return render(request,'album/update_album.html')
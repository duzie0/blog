from django.shortcuts import redirect


def login_required(func):
    def decorator(request,*args,**kwargs):
        if request.session.get('username'):

            return func(request,*args,**kwargs)
        else:
            return redirect('/user/login/')
    return decorator
from user import views
from django.conf.urls import url

urlpatterns =[
    url(r'^$',views.home,name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^update_user_info/$',views.update_user_info,name='update_user_info'),
    url(r'^get_code/$',views.get_code),
    url(r'^user_info/$',views.user_info,name='user_info'),
]
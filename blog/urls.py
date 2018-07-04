



from . import views
from django.conf.urls import url

urlpatterns =[
    url(r'^blog/$',views.blog,name='blog'),
    url(r'^create_blog/$',views.create_blog,name='create_blog'),
    url(r'^update_blog/$',views.update_blog,name='update_blog'),
    url(r'^blog_page/(?P<pk>[0-9]+)/$',views.blog_page,name='blog_page'),
]
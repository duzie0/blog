



from . import views
from django.conf.urls import url

urlpatterns =[
    url(r'^$',views.album,name='album'),
    url(r'^create_album/$',views.create_album,name='create_album'),
    url(r'^update_album/$',views.update_album,name='update_album'),
]
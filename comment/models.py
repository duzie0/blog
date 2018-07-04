from django.db import models
from user.models import User
from blog.models import Blog

# Create your models here.
class Comment(models.Model):

    author = models.ForeignKey(User)
    belong_to = models.ForeignKey(Blog)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    view_times = models.IntegerField(default=0)
    #-1待审核，0审核不通过，1审核通过
    check = models.IntegerField(default=-1)
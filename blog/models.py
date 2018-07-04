from django.db import models
from django.utils import timezone

from user.models import User
# Create your models here.

class Blog(models.Model):

    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    mod_at = models.DateTimeField(auto_now_add=True)
    view_times = models.IntegerField(default=0)
    #-1待审核，0审核不通过，1审核通过
    check = models.IntegerField(default=-1)
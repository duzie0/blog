from django.db import models
from user.models import User

# Create your models here.
class Album(models.Model):
    # id = models.AutoField(primary_key=True)

    author = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300,default='相册描述')
    img = models.ImageField(upload_to='photo/', default='default/default.jpg')
    # img = models.FileField(upload_to='photos/')
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        """
        返回Album对象的str表示形式
        """
        return self.title



class Photo(models.Model):
    """
    用户照片
    """
    title = models.CharField(max_length=150,null=True)
    user= models.ForeignKey(User)
    album = models.ForeignKey(Album)
    img = models.ImageField(upload_to='photo/', default='default/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        """
        返回Photo对象的str表示形式
        """
        return  self.title
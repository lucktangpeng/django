from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='类型')

class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name='书名')
    price = models.IntegerField(verbose_name="价格")
    type = models.ForeignKey(Type, models.CASCADE, verbose_name='类型')
    add_time = models.DateTimeField(auto_now_add=True)
    release_time = models.DateField(verbose_name="发布时间")
    ISBN = models.CharField(max_length=20, verbose_name="国际编码")

class Author(models.Model):
    name = models.CharField(max_length=20, verbose_name='作者名称')
    age = models.IntegerField(verbose_name="作者年龄")

class AuthorType(models.Model):
    book = models.ForeignKey(Book, models.CASCADE, verbose_name="书籍ID")
    author = models.ForeignKey(Author, models.CASCADE, verbose_name="作者ID")
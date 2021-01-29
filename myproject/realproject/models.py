from django.db import models


# Create your models here.
from django.views.generic import ListView


class Test(models.Model):
    subject = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    summary = models.TextField(max_length=1000, help_text='설명을 적으세요')
    upload_date = models.DateField(null=True, blank=True)
    acount = models.CharField(max_length=1)

    def __str__(self):
        """String for representing the Model object."""
        return self.subject


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)  # media폴더 안에 users부터 년 월 일 폴더가 만들어지고 그 안에 이미지 존재

    # image = models.ImageField(upload_to='images')  media 폴더 안에 images 폴더 안에 모두 이미지가 들어감

    def __str__(self):
        return self.title


class Product(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    product = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    exp_date = models.DateField(null=True)

    def __str__(self):
        return self.code


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')


class PostList(ListView):
    paginate_by = 5
    model = Post


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField(max_length=300, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class Pcomment(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField(max_length=300, null=True)
    make_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

from django.db import models


class Category(models.Model):

    name = models.CharField(verbose_name='이름', max_length=50)

    class Meta:
        verbose_name = '분류'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='분류', null=True, blank=True)
    title = models.CharField(verbose_name='제목', max_length=256)
    content = models.TextField(verbose_name='내용', blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        verbose_name = '글'
        ordering = ['created']

    def __str__(self):
        return self.title
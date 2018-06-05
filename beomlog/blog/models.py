import os
from django.db import models
from django.urls import reverse

from beomlog import settings


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_pic', blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def delete(self):
        if self.image:
            os.remove(self.image.path)
            return super(Post, self).delete()

        else:
            super(Post, self).delete()
            return reverse('home')
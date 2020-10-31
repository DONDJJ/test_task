from django.db import models

class Post(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=250)
    date = models.DateTimeField('Время создания')


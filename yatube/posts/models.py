# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    # Описываем поля модели и их типы
    # Тип: CharField (строка с ограничением длины)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        out_text: str = f'{self.title}'
        return (out_text)


class Post(models.Model):
    # Тип: TextField
    text = models.TextField()
    # Тип поля: DateTimeField, для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(auto_now_add=True)
    # Тип: ForeignKey, ссылка на модель User
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
        )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE
        )

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Menu(models.Model):
    name = models.CharField("имя", max_length=50, unique=True)
    description = models.CharField("описание", max_length=250)

    class Meta:
        verbose_name = "Основное Меню"
        verbose_name_plural = "Основное Меню"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField("имя", max_length=25, unique=True)
    description = models.CharField("описание", max_length=250)
    url = models.CharField("url-адрес", max_length=500, blank=True)
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name="меню",
        help_text=("к какой позиции основного меню пренадлежит"),
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="родитель",
        help_text=("является ли потомком одного из подпунктов"),
    )

    class Meta:
        verbose_name = "Подпункт"
        verbose_name_plural = "Подпункты"

    def __str__(self):
        return self.name

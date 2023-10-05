from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class MenuHeader(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Menu Header - {self.name}"

    class Meta:
        verbose_name = "Заголовок меню"
        verbose_name_plural = "Заголовки меню"


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(to=MenuHeader,
                             on_delete=models.CASCADE,
                             related_name="first_child",
                             verbose_name="Объект MenuHeader",
                             )
    parent = models.ForeignKey(to="tree_menu.MenuItem",
                               on_delete=models.CASCADE,
                               related_name="child_list",
                               blank=True,
                               verbose_name="Объект MenuItem. Не обязателен если указан menu",
                               null=True
                               )

    def __str__(self):
        return f"MenuItem - {self.name} "

    class Meta:
        verbose_name = "Элемент меню"
        verbose_name_plural = "Элементы меню"

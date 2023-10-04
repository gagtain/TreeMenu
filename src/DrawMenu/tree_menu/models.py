from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class MenuHeader(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Menu Header - {self.name}"


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(to=MenuHeader,
                             on_delete=models.CASCADE,
                             related_name="first_child",
                             blank=True,
                             verbose_name="Объект MenuHeader. Не обязателен если указан parent",
                             null=True
                             )
    parent = models.ForeignKey(to="tree_menu.MenuItem",
                               on_delete=models.CASCADE,
                               related_name="child_list",
                               blank=True,
                               verbose_name="Объект MenuItem. Не обязателен если указан menu",
                               null=True
                               )

    # def validate_item(self):
    #     if not self.parent and not self.menu:
    #         raise ValidationError("Поле parent и menu пусты, необходимо указать минимум один из них")


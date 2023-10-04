# Generated by Django 4.2.5 on 2023-10-04 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0002_alter_menuitem_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_child', to='tree_menu.menuheader', verbose_name='Объект MenuHeader. Не обязателен если указан parent'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_list', to='tree_menu.menuitem', verbose_name='Объект MenuItem. Не обязателен если указан menu'),
        ),
    ]
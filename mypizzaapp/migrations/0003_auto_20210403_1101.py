# Generated by Django 3.1.7 on 2021-04-03 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypizzaapp', '0002_auto_20210403_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mypizzastore',
            old_name='pizza_sizes',
            new_name='pizza_size',
        ),
    ]
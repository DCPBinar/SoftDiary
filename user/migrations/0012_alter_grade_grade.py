# Generated by Django 3.2.9 on 2021-11-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20211121_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.IntegerField(),
        ),
    ]
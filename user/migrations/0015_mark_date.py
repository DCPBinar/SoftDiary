# Generated by Django 3.2.9 on 2021-11-23 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_testmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='date',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
    ]
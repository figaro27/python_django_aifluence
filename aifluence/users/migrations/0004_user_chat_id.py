# Generated by Django 3.0 on 2020-09-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200113_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.IntegerField(default=0, verbose_name='QB chat id'),
        ),
    ]
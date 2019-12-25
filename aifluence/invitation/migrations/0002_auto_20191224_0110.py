# Generated by Django 3.0 on 2019-12-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='influencer_platform',
            field=models.CharField(choices=[('IN', 'Instagram'), ('FA', 'Facebook'), ('TW', 'Twitter')], default='IN', max_length=2),
        ),
    ]

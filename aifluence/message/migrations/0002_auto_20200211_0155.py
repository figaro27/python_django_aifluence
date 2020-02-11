# Generated by Django 3.0 on 2020-02-11 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0011_auto_20200210_0420'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.Campaign'),
        ),
        migrations.AlterField(
            model_name='message',
            name='discussion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.Discussion'),
        ),
    ]
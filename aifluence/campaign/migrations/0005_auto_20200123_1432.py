# Generated by Django 3.0 on 2020-01-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_contract_discussion'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_budget',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_status',
            field=models.CharField(choices=[('OF', 'Offered'), ('AC', 'Accepted'), ('RE', 'Rejected'), ('CA', 'Cancelled'), ('CO', 'Completed')], default='OF', max_length=2),
        ),
    ]
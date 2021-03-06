# Generated by Django 3.0 on 2020-01-17 16:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0002_auto_20191226_1215'),
        ('users', '0003_auto_20200113_1828'),
        ('campaign', '0003_auto_20200116_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('influencer_platform', models.CharField(choices=[('IN', 'Instagram'), ('FA', 'Facebook'), ('TW', 'Twitter')], default='IN', max_length=2)),
                ('posting_suggestion', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.Campaign')),
                ('influencer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Influencer')),
                ('invitation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invitation.Invitation')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_terms', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('contract_status', models.CharField(choices=[('OF', 'Offered'), ('AC', 'Accepted'), ('RE', 'Rejected'), ('CA', 'Cancelled'), ('CO', 'Completed')], default='OT', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discussion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.Discussion')),
            ],
        ),
    ]

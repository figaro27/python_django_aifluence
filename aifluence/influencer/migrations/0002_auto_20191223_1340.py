# Generated by Django 3.0 on 2019-12-23 13:40

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='basics',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='earnings',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='engagements',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='interests',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='locations',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='personality_traits',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='sentiments',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-07-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdFund', '0011_auto_20220706_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='projectreports',
            name='project_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectreports',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

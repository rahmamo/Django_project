# Generated by Django 3.2.13 on 2022-07-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdFund', '0009_auto_20220706_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='donations',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='donations',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210423_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]

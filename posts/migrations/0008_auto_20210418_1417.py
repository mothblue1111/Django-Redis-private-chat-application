# Generated by Django 3.1.7 on 2021-04-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_privacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='privacy',
            field=models.CharField(choices=[('public', 'Public'), ('friends', 'Friends'), ('private', 'Only Me')], max_length=10),
        ),
    ]

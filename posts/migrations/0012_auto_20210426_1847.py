# Generated by Django 3.1.7 on 2021-04-26 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_comment_comment_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_Likes',
            new_name='comment_likes',
        ),
    ]
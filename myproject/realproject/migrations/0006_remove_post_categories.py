# Generated by Django 3.1.3 on 2021-01-11 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realproject', '0005_category_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
    ]
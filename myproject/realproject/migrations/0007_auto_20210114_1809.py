# Generated by Django 3.1.3 on 2021-01-14 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realproject', '0006_remove_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='realproject.Category'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='Pcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=300, null=True)),
                ('make_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realproject.post')),
            ],
        ),
    ]

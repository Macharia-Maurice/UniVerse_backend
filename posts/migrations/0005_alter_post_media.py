# Generated by Django 5.0.6 on 2024-05-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.ImageField(blank=True, null=True, upload_to='media/posts', verbose_name='Post Media'),
        ),
    ]

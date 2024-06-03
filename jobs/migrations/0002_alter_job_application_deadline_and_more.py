# Generated by Django 5.0.6 on 2024-06-03 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_userprofile_profile_picture'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='application_deadline',
            field=models.DateTimeField(verbose_name='Application Deadline'),
        ),
        migrations.AlterField(
            model_name='job',
            name='application_procedure',
            field=models.TextField(verbose_name='Application Procedure'),
        ),
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='accounts.userprofile', verbose_name='Job Owner'),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='job',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Created At'),
        ),
    ]

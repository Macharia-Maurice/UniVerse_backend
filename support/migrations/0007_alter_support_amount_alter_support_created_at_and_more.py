# Generated by Django 5.0.6 on 2024-06-06 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_follower'),
        ('support', '0006_alter_support_amount_alter_support_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='support',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='support',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='support',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support', to='accounts.userprofile', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='support',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='support',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]

# Generated by Django 2.2.15 on 2022-11-04 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0002_auto_20221104_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
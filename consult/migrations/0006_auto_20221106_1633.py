# Generated by Django 2.2.15 on 2022-11-06 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0005_auto_20221106_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultation',
            old_name='categphone',
            new_name='category',
        ),
    ]

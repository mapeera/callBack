# Generated by Django 2.2.15 on 2022-11-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0007_transaction_total_collected'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='description',
            field=models.CharField(default='construction', max_length=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='location',
            field=models.CharField(default='Nyanama', max_length=10),
        ),
    ]
# Generated by Django 3.2.9 on 2022-02-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]

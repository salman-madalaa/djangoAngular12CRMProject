# Generated by Django 4.0.2 on 2022-02-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='units',
            field=models.IntegerField(max_length=50),
        ),
    ]
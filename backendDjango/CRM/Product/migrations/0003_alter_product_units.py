# Generated by Django 4.0.2 on 2022-02-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_product_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='units',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerOrder', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerorder',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='orderDate',
            field=models.DateField(),
        ),
    ]
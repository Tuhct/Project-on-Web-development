# Generated by Django 3.0.4 on 2022-12-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20221211_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='order_time',
            field=models.DateField(auto_now=True),
        ),
    ]
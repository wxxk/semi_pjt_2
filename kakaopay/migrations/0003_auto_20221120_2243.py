# Generated by Django 3.2.13 on 2022-11-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakaopay', '0002_auto_20221120_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderlistfinal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

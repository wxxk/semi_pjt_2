# Generated by Django 3.2.13 on 2022-11-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
    ]
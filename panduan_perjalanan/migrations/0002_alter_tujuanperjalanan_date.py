# Generated by Django 4.1 on 2022-10-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panduan_perjalanan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tujuanperjalanan',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
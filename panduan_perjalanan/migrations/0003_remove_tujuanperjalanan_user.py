# Generated by Django 4.1 on 2022-10-29 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panduan_perjalanan', '0002_alter_tujuanperjalanan_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tujuanperjalanan',
            name='user',
        ),
    ]
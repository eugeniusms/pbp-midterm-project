# Generated by Django 4.1 on 2022-11-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TujuanPerjalanan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("kota_asal", models.CharField(max_length=100)),
                ("kota_destinasi", models.CharField(max_length=100)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
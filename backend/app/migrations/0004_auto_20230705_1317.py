# Generated by Django 3.2.19 on 2023-07-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_clothe_tshirt'),
    ]

    operations = [
        migrations.AddField(
            model_name='pant',
            name='count',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='sock',
            name='count',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='count',
            field=models.IntegerField(default=10),
        ),
    ]
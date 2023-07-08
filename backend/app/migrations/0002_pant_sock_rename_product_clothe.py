# Generated by Django 4.2.2 on 2023-07-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=25)),
                ('discount', models.CharField(max_length=10)),
                ('second_price', models.CharField(max_length=10)),
                ('pic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='sock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=25)),
                ('discount', models.CharField(max_length=10)),
                ('second_price', models.CharField(max_length=10)),
                ('pic', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Clothe',
        ),
    ]
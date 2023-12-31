# Generated by Django 4.2.3 on 2023-07-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('pic', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(default=10)),
                ('material', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.ManyToManyField(to='api.category')),
                ('size', models.ManyToManyField(to='api.size')),
            ],
        ),
    ]

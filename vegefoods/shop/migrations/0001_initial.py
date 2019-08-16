# Generated by Django 2.2.1 on 2019-08-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vegtables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('kind', models.CharField(max_length=255, unique=True)),
                ('prise', models.DecimalField(decimal_places=2, max_digits=6)),
                ('detail', models.TextField(blank=True, default='')),
                ('count', models.PositiveIntegerField(default=0)),
                ('wishlist', models.BooleanField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]

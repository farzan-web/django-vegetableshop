# Generated by Django 2.2.1 on 2019-08-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190812_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
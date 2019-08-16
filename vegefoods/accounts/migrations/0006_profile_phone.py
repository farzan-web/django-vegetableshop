# Generated by Django 2.2.1 on 2019-08-12 14:22

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190812_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
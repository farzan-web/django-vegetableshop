# Generated by Django 2.2.1 on 2019-08-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190812_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state_country',
            field=models.CharField(blank=True, choices=[('france', 'France'), ('iran', 'Iran'), ('philippines', 'Philippines'), ('hongkong', 'Hongkong'), ('japan', 'Japan'), ('unitedkingdom', 'United kingdom'), ('unitedstates', 'United states')], default='France', max_length=10),
        ),
    ]
# Generated by Django 2.2.1 on 2019-08-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20190815_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state_country',
            field=models.CharField(choices=[('france', 'France'), ('iran', 'Iran'), ('philippines', 'Philippines'), ('hongkong', 'Hongkong'), ('japan', 'Japan'), ('unitedkingdom', 'United kingdom'), ('unitedstates', 'United states')], default='france', max_length=10),
        ),
    ]
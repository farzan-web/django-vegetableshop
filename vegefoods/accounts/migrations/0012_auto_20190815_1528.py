# Generated by Django 2.2.1 on 2019-08-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190812_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state_country',
            field=models.CharField(blank=True, choices=[('france', 'France'), ('iran', 'Iran'), ('philippines', 'Philippines'), ('hongkong', 'Hongkong'), ('japan', 'Japan'), ('unitedkingdom', 'United kingdom'), ('unitedstates', 'United states')], default='france', max_length=10),
        ),
    ]

# Generated by Django 2.2.1 on 2019-08-12 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_auto_20190812_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_country', models.CharField(blank=True, choices=[('france', 'France'), ('iran', 'Iran'), ('philippines', 'Philippines'), ('hongkong', 'Hongkong'), ('japan', 'Japan'), ('unitedkingdom', 'United kingdom'), ('unitedstates', 'United states')], default='France', max_length=10)),
                ('address', models.TextField(blank=True, default='')),
                ('phone_number', models.PositiveIntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

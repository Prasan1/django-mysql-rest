# Generated by Django 3.0.4 on 2020-03-17 07:12

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester', models.CharField(default='', editable=False, max_length=31)),
                ('request_date', models.DateField(verbose_name='date requested')),
                ('active', models.BooleanField(default=True)),
                ('payload', django_mysql.models.JSONField(default=dict)),
            ],
            options={
                'db_table': 'Service',
                'ordering': ['-request_date', 'requester'],
                'get_latest_by': 'request_date',
            },
        ),
    ]

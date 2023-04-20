# Generated by Django 4.1.7 on 2023-04-11 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('search_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('professional_id', models.PositiveIntegerField(null=False, blank=False)),
                ('client_id', models.PositiveIntegerField(null=False, blank=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now))
            ],
            options={
                'db_table': 'SearchHistory',
            },
        ),
    ]

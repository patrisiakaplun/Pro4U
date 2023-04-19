# Generated by Django 4.2 on 2023-04-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('professional_id', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('likes', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'Images',
            },
        ),
    ]

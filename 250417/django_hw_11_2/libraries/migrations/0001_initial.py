# Generated by Django 4.2.11 on 2025-04-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.TextField(max_length=10)),
                ('author', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
    ]

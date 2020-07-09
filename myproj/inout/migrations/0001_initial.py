# Generated by Django 3.0.6 on 2020-06-06 06:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('ticketnum', models.IntegerField()),
                ('first_row', models.CharField(max_length=100, validators=[django.core.validators.int_list_validator])),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inout', '0007_status_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_status', models.CharField(max_length=500)),
            ],
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inout', '0005_auto_20200607_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='save_random_number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Random_Number', models.IntegerField()),
            ],
        ),
    ]
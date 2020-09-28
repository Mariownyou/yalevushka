# Generated by Django 3.1.1 on 2020-09-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_mark', models.CharField(max_length=200)),
                ('is_visited', models.BooleanField()),
                ('car_rare', models.IntegerField()),
            ],
        ),
    ]

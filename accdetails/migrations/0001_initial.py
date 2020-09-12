# Generated by Django 3.0.7 on 2020-09-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('UserName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
                ('pan_number', models.IntegerField()),
                ('aadhar_number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('Gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Others')], max_length=1)),
            ],
        ),
    ]

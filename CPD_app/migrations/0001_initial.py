# Generated by Django 3.1.2 on 2021-08-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10)),
                ('otp', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('photo_id_proof', models.CharField(max_length=30)),
                ('aadhaar_number', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('year_of_birth', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
    ]

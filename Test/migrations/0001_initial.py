# Generated by Django 5.0.6 on 2024-07-02 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=200)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Contact', models.BigIntegerField()),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.user')),
            ],
        ),
    ]

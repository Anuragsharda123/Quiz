# Generated by Django 5.0.6 on 2024-07-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0005_alter_result_rank_alter_result_total_attempted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Percentile',
            field=models.FloatField(null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-14 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0006_alter_result_percentile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='img_Solution',
            field=models.ImageField(null=True, upload_to='uploads/products/'),
        ),
        migrations.AddField(
            model_name='question',
            name='text_Solution',
            field=models.CharField(null=True),
        ),
    ]

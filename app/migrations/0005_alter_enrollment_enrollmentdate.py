# Generated by Django 5.1.1 on 2024-09-07 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_headinstructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='enrollmentdate',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 3.2 on 2021-04-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_business_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='fire_dept',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

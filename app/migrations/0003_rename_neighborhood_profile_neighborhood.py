# Generated by Django 3.2 on 2021-04-10 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_business_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Neighborhood',
            new_name='neighborhood',
        ),
    ]

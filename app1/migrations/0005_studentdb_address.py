# Generated by Django 3.2.6 on 2021-08-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_studentdb_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdb',
            name='Address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

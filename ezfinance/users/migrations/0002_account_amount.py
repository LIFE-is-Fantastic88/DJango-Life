# Generated by Django 2.2.5 on 2020-02-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='amount',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

# Generated by Django 2.2.5 on 2020-03-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EzFinance_Account', '0026_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 2.2.5 on 2020-04-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EzFinance_Account', '0034_job_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply',
            name='job_reject',
            field=models.BooleanField(default=False),
        ),
    ]

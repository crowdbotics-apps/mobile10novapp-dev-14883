# Generated by Django 2.2.17 on 2020-11-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201110_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='kjjjl',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='kjkjkl',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]

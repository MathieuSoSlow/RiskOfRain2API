# Generated by Django 2.1.7 on 2019-05-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_remove_character_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='icon',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='icon',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='icon',
            field=models.CharField(max_length=512),
        ),
    ]

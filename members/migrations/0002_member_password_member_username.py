# Generated by Django 4.1.7 on 2023-03-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]

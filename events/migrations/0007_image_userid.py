# Generated by Django 4.1.7 on 2023-03-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='userId',
            field=models.IntegerField(max_length=30, null=True),
        ),
    ]
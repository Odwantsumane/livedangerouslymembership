# Generated by Django 4.1.7 on 2023-03-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_messages_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='header_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

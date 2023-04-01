# Generated by Django 4.1.7 on 2023-03-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_image_camping_image_alter_image_canoeing_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_campingg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/camping/gear/')),
            ],
        ),
        migrations.CreateModel(
            name='Image_canoeingg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/canoeing/gear/')),
            ],
        ),
        migrations.CreateModel(
            name='Image_hikingg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/hiking/gear/')),
            ],
        ),
        migrations.CreateModel(
            name='Image_skydivingg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/skydiving/gear/')),
            ],
        ),
    ]

# Generated by Django 3.1 on 2023-03-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
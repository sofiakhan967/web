# Generated by Django 4.0.6 on 2022-07-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

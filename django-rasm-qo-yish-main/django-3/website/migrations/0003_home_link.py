# Generated by Django 4.0.4 on 2022-05-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_home_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='link',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]

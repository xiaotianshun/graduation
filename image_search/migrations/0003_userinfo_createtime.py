# Generated by Django 4.0.3 on 2022-04-13 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_search', '0002_rename_nikename_userinfo_nikename'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='createtime',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

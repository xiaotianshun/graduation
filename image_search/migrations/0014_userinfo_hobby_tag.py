# Generated by Django 4.0.3 on 2022-04-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_search', '0013_imageinfo_all_tag_imagetag'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='hobby_tag',
            field=models.CharField(default='', max_length=128, verbose_name='兴趣标签'),
        ),
    ]

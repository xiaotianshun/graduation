# Generated by Django 4.0.3 on 2022-04-29 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_search', '0012_alter_userinfo_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageinfo',
            name='all_tag',
            field=models.CharField(default='', max_length=128, verbose_name='图片标签'),
        ),
        migrations.CreateModel(
            name='ImageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, default='', max_length=64, verbose_name='标签')),
                ('score', models.DecimalField(decimal_places=10, max_digits=11, verbose_name='分数')),
                ('imageinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_search.imageinfo', verbose_name='图片信息')),
            ],
        ),
    ]

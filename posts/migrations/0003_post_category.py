# Generated by Django 3.2.18 on 2023-05-09 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
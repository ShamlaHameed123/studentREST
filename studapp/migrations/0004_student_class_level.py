# Generated by Django 3.1.5 on 2021-01-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0003_auto_20210125_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Class_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0006_remove_student_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

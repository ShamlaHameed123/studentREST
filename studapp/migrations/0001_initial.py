# Generated by Django 3.1.5 on 2021-01-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('First_name', models.TextField()),
                ('Last_name', models.TextField()),
                ('Date_of_birth', models.TextField()),
                ('Email', models.TextField(null=True)),
                ('Class', models.DateTimeField(auto_now=True)),
                ('Parent_name', models.TextField(unique=True)),
                ('Phone_number', models.IntegerField(unique=True)),
                ('DateAdded', models.DateTimeField(auto_now=True)),
                ('DateUpdated', models.DateTimeField(auto_now=True)),
                ('Year_joined', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.0.4 on 2021-10-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.TextField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]

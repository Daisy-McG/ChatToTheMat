# Generated by Django 3.1.5 on 2021-02-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_rooms', '0003_auto_20210203_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=80, null=True)),
                ('message', models.CharField(max_length=1500)),
                ('time', models.DateTimeField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
# Generated by Django 3.2.3 on 2021-05-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='anonimus', max_length=50, verbose_name='Имя')),
                ('message', models.TextField(max_length=1000, verbose_name='Сообщение')),
            ],
        ),
    ]

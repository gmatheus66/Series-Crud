# Generated by Django 2.2.4 on 2019-08-30 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title of Serie', max_length=100)),
                ('description', models.TextField(help_text='Description of Serie', max_length=255)),
            ],
        ),
    ]

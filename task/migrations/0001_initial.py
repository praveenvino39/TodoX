# Generated by Django 3.1.2 on 2020-10-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('is_done', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('finished_date', models.DateTimeField()),
            ],
        ),
    ]

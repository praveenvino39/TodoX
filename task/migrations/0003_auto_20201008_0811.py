# Generated by Django 3.1.2 on 2020-10-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
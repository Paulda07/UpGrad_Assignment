# Generated by Django 2.1.7 on 2019-03-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20190307_0537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['-due_date']},
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateTimeField(default='2019-03-07 06:18:45'),
        ),
    ]

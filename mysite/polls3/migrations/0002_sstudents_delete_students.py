# Generated by Django 4.1.7 on 2023-03-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('second_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]

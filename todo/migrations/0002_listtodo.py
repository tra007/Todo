# Generated by Django 4.0.4 on 2022-04-26 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=150)),
                ('start', models.TimeField()),
                ('finish', models.TimeField()),
                ('don', models.BooleanField(default=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.datetime')),
            ],
        ),
    ]

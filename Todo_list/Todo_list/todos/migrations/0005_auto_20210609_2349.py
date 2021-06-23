# Generated by Django 3.2.4 on 2021-06-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20210607_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='categories',
            field=models.ManyToManyField(to='todos.Categories'),
        ),
    ]

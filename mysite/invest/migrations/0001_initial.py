# Generated by Django 3.1.8 on 2022-11-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datedb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='month')),
            ],
        ),
        migrations.CreateModel(
            name='sharePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('date', models.DateField(verbose_name='month')),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
# Generated by Django 3.0.4 on 2020-09-03 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
    ]

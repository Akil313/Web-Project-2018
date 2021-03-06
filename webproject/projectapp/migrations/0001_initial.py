# Generated by Django 2.0.4 on 2018-04-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=250)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'ordering': ('rating',),
            },
        ),
    ]

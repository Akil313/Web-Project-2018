# Generated by Django 2.0.4 on 2018-04-29 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='projectapp.Service'),
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-28 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sixthquestions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sixthquestion',
            name='sixth_thirteen',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

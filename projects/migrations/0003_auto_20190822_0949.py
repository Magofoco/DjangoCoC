# Generated by Django 2.2.3 on 2019-08-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_is_audited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_audited',
            field=models.TextField(default='No'),
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-09 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('initialquestions', '0003_auto_20190809_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='initialquestion',
            old_name='intial_two',
            new_name='initial_two',
        ),
    ]
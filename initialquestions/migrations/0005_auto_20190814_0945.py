# Generated by Django 2.2.3 on 2019-08-14 09:45

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('initialquestions', '0004_auto_20190809_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialquestion',
            name='initial_two',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Primary Care', 'Primary Care'), ('Secondary Care', 'Secondary Care'), ('Tertiary Care', 'Tertiary Care'), ('Individual Care of Self', 'Individual Care of Self'), ('Triage', 'Triage'), ('For the purposes of population screening', 'For the purposes of population screening'), ('Other', 'Other')], max_length=119),
        ),
    ]

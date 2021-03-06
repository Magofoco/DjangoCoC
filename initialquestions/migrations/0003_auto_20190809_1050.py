# Generated by Django 2.2.3 on 2019-08-09 10:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('initialquestions', '0002_auto_20190809_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialquestion',
            name='initial_one',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Diagnostic', 'Diagnostic'), ('Therapeutic', 'Therapeutic'), ('Population health', 'Population health'), ('Care-based', 'Care-based'), ('Triage', 'Triage'), ('Self-care', 'Self-care'), ('Health promotion', 'Health promotion'), ('Remote Monitoring', 'Remote Monitoring'), ('Remote Consultation', 'Remote Consultation'), ('Other', 'Other')], max_length=129),
        ),
        migrations.AlterField(
            model_name='initialquestion',
            name='intial_two',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Primary Care', 'Primary Care'), ('Secondary Care', 'Secondary Care'), ('Tertiary Care', 'Tertiary Careh'), ('Individual Care of Self', 'Individual Care of Self'), ('Triage', 'Triage'), ('For the purposes of population screening', 'For the purposes of population screening'), ('Other', 'Other')], max_length=119),
        ),
    ]

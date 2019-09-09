# Generated by Django 2.1.3 on 2019-07-07 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firstquestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_one', models.TextField()),
                ('first_two', models.TextField()),
                ('first_three', models.TextField()),
                ('first_four', models.TextField()),
                ('first_five', models.TextField()),
                ('first_six', models.TextField()),
                ('first_seven', models.TextField()),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]

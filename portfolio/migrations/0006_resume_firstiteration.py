# Generated by Django 4.2.4 on 2023-09-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_resume_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='firstIteration',
            field=models.BooleanField(default=False),
        ),
    ]

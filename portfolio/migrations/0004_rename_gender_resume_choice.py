# Generated by Django 4.2.4 on 2023-09-04 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_introduction_email_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='gender',
            new_name='choice',
        ),
    ]
# Generated by Django 4.0.1 on 2022-03-05 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FamilDetail',
            new_name='FamilyDetail',
        ),
    ]
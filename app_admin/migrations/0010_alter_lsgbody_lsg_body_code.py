# Generated by Django 4.0.3 on 2022-03-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0009_rename_state_lsgbody_district_lsgbody_lsg_body_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lsgbody',
            name='lsg_body_code',
            field=models.IntegerField(max_length=80),
        ),
    ]

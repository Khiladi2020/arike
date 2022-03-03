# Generated by Django 4.0.3 on 2022-03-03 15:03

from django.db import migrations


STATES = ["Andhra Pradesh", "Karnataka", "Assam", "Bihar",
          "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh"]
DISTRICTS = ["District 1", "District 2", "District 3"]


def populate_data(apps, schema_editor):
    State = apps.get_model('app_admin', 'State')
    District = apps.get_model('app_admin', 'District')

    for state in STATES:
        # create state
        new_state = State(name=state)
        new_state.save()

        # Create districts for concerned state
        for district in DISTRICTS:
            new_district = District(name=district, state=new_state)
            new_district.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0007_alter_state_name'),
    ]

    operations = [
        migrations.RunPython(populate_data)
    ]

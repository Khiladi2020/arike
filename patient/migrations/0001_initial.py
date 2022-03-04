# Generated by Django 4.0.1 on 2022-03-04 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_admin', '0012_alter_appuser_groups_alter_appuser_user_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('icds_code', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('landmark', models.CharField(blank=True, max_length=80)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=80)),
                ('emergency_phone_number', models.IntegerField()),
                ('expired_time', models.DateTimeField(blank=True, null=True)),
                ('ward', models.CharField(max_length=80)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.facility')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('care_type', models.CharField(max_length=80)),
                ('care_sub_type', models.CharField(max_length=80)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palliative_phase', models.CharField(max_length=80)),
                ('blood_pressure', models.CharField(max_length=80)),
                ('pulse', models.CharField(max_length=80)),
                ('general_random_blood_sugar', models.CharField(max_length=80)),
                ('personal_hygiene', models.CharField(max_length=80)),
                ('mouth_hygiene', models.CharField(max_length=80)),
                ('pubic_hygiene', models.CharField(max_length=80)),
                ('systemic_examination', models.CharField(max_length=80)),
                ('patient_at_peace', models.BooleanField(default=False)),
                ('pain', models.BooleanField(default=False)),
                ('symptoms', models.CharField(max_length=80)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VisitSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('description', models.TextField()),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.treatment')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.visit')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.disease')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='FamilDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('phone', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('email', models.CharField(max_length=80)),
                ('relation', models.CharField(max_length=80)),
                ('address', models.TextField()),
                ('education', models.CharField(max_length=80)),
                ('occupation', models.CharField(max_length=80)),
                ('remarks', models.TextField()),
                ('is_primary', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]

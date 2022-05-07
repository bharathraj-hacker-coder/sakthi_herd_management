# Generated by Django 3.2.4 on 2022-03-28 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alarm_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_no', models.CharField(max_length=200, null=True)),
                ('alarm_date', models.DateField(max_length=200, null=True)),
                ('alarm_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='calving_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_no', models.CharField(max_length=200, null=True)),
                ('date_calving', models.DateField(max_length=200, null=True)),
                ('sex', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cattle_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_no', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('breed', models.CharField(max_length=200, null=True)),
                ('sex', models.CharField(max_length=200, null=True)),
                ('dob', models.CharField(max_length=200, null=True)),
                ('sire_name', models.CharField(max_length=200, null=True)),
                ('dam_name', models.CharField(max_length=200, null=True)),
                ('no_of_location', models.IntegerField(max_length=200, null=True)),
                ('milking_status', models.CharField(max_length=200, null=True)),
                ('breeding_status', models.CharField(max_length=200, null=True)),
                ('last_breeding', models.DateField(max_length=200, null=True)),
                ('last_calving', models.DateField(max_length=200, null=True)),
                ('calf_gender', models.CharField(max_length=200, null=True)),
                ('concentrate', models.CharField(max_length=200, null=True)),
                ('quality', models.FloatField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='deworming_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_no', models.CharField(max_length=200, null=True)),
                ('deworme_name', models.CharField(max_length=200, null=True)),
                ('quantity', models.FloatField(max_length=200, null=True)),
                ('date_deworming', models.DateField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='insemination_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_no', models.CharField(max_length=200, null=True)),
                ('date_heat_sign', models.DateField(max_length=200, null=True)),
                ('action', models.CharField(max_length=200, null=True)),
                ('date_breeding', models.DateField(max_length=200, null=True)),
                ('nature_of_service', models.CharField(max_length=200, null=True)),
                ('site_tag_no', models.CharField(max_length=200, null=True)),
                ('aitech_name', models.CharField(max_length=200, null=True)),
                ('sat_alarm', models.DateField(max_length=200, null=True)),
                ('pregnant_status', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='milk_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_no', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(max_length=200, null=True)),
                ('shift', models.CharField(max_length=200, null=True)),
                ('quantity', models.FloatField(max_length=200, null=True)),
                ('fat', models.FloatField(max_length=200, null=True)),
                ('snf', models.FloatField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='treatment_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_no', models.CharField(max_length=200, null=True)),
                ('medicine_name', models.CharField(max_length=200, null=True)),
                ('diagnosis', models.CharField(max_length=200, null=True)),
                ('date_diagnosis', models.DateField(max_length=200, null=True)),
                ('medicine_advice', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vaccination_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_no', models.CharField(max_length=200, null=True)),
                ('vaccine_name', models.CharField(max_length=200, null=True)),
                ('date_vaccination', models.IntegerField(max_length=200, null=True)),
            ],
        ),
    ]

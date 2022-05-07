from django.db import models


class cattle_records(models.Model):
    tag_no = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    breed = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=200, null=True)
    dob = models.CharField(max_length=200, null=True)
    sire_name = models.CharField(max_length=200, null=True)
    dam_name = models.CharField(max_length=200, null=True)
    no_of_lactation = models.IntegerField(null=True)
    milking_status = models.CharField(max_length=200, null=True)
    breeding_status = models.CharField(max_length=200, null=True)
    last_breeding = models.DateField(max_length=200, null=True)
    last_calving = models.DateField(max_length=200, null=True)
    calf_gender = models.CharField(max_length=200, null=True)
    concentrate1 = models.CharField(max_length=200, null=True)
    quantity1 = models.FloatField(max_length=200, null=True)
    concentrate2 = models.CharField(max_length=200, null=True)
    quantity2 = models.FloatField(max_length=200, null=True)

    def __str__(self):
        return self.tag_no

class vaccination_record(models.Model):
    tag_no= models.CharField(max_length=200, null=True)
    vaccine_name= models.CharField(max_length=200, null=True)
    date_vaccination = models.IntegerField(null=True)

    def __str__(self):
        return self.tag_no

class calving_records(models.Model):
    tag_no = models.CharField(max_length=200, null=True)
    date_calving = models.DateField(max_length=200, null=True)
    sex = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tag_no

class deworming_records(models.Model):
    tag_no = models.CharField(max_length=200, null=True)
    deworme_name = models.CharField(max_length=200, null=True)
    quantity = models.FloatField(max_length=200, null=True)
    date_deworming = models.DateField(max_length=200, null=True)

    def __str__(self):
        return self.tag_no

class alarm_records(models.Model):
    tag_no = models.CharField(max_length=200, null=True)
    alarm_date = models.DateField(max_length=200, null=True)
    alarm_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tag_no

class milk_record(models.Model):
    tag_no = models.CharField(max_length=200, null=True)
    date = models.DateField(max_length=200, null=True)
    shift = models.CharField(max_length=200, null=True)
    quantity = models.FloatField(max_length=200, null=True)
    fat = models.FloatField(max_length=200, null=True)
    snf = models.FloatField(max_length=200, null=True)

    def __str__(self):
        return self.tag_no

class treatment_record(models.Model):
    tag_no = models.CharField(max_length=200, null=True)
    medicine_name = models.CharField(max_length=200, null=True)
    diagnosis = models.CharField(max_length=200, null=True)
    date_diagnosis= models.DateField(max_length=200, null=True)
    medicine_advice = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tag_no

class insemination_records(models.Model):
    tag_no = models.CharField(max_length=200, null=True)
    date_heat_sign = models.DateField(max_length=200, null=True)
    action = models.CharField(max_length=200, null=True)
    date_breeding= models.DateField(max_length=200, null=True)
    nature_of_service = models.CharField(max_length=200, null=True)
    site_tag_no = models.CharField(max_length=200, null=True)
    aitech_name = models.CharField(max_length=200, null=True)
    sat_alarm = models.DateField(max_length=200, null=True)
    pregnant_status = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tag_no

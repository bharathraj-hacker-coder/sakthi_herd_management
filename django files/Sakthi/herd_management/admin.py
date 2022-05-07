from django.contrib import admin
from .models import  cattle_records, vaccination_record, calving_records, deworming_records,\
    alarm_records, milk_record, treatment_record, insemination_records
# Register your models here.


admin.site.register(cattle_records)
admin.site.register(vaccination_record)
admin.site.register(calving_records)
admin.site.register(deworming_records)
admin.site.register(alarm_records)
admin.site.register(milk_record)
admin.site.register(treatment_record)
admin.site.register(insemination_records)
from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin, name='signin'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('error_page', views.error_page, name='error_page'),
    path('logout', views.logout, name='logout'),
    path('bull',views.bull, name='bull'),
    path('buffalo_bull', views.buffalo_bull, name='buffalo_bull'),
    path('cow', views.cow, name='cow'),
    path('buffalo_cow', views.buffalo_cow, name='buffalo_cow'),
    path('cow_calf', views.cow_calf, name='cow_calf'),
    path('buffalo_calf', views.buffalo_calf, name='buffalo_calf'),
    path('bull_or_buffalo_entry', views.bull_or_buffalo_entry, name='bull_or_buffalo_entry'),
    path('cow_or_buffalo_cow_entry', views.cow_or_buffalo_cow_entry, name='cow_or_buffalo_cow_entry'),
    path('cow_calf_or_buffalo_calf_entry', views.cow_calf_or_buffalo_calf_entry, name='cow_calf_or_buffalo_calf_entry'),
    path('add_feed', views.add_feed, name='add_feed'),
    path('milk_data_entry', views.milk_data_entry, name='milk_data_entry'),
    path('milk_data_overall_report', views.milk_data_overall_report, name='milk_data_overall_report'),
    path('insemination_entry', views.insemination_entry, name='insemination_entry'),
    path('calving_entry', views.calving_entry, name='calving_entry'),
    path('deworming_entry', views.deworming_entry, name='deworming_entry'),
    path('breeding_report', views.breeding_report, name='breeding_report'),
    path('treatment_entry', views.treatment_entry, name='treatment_entry'),
    path('vaccination_entry', views.vaccination_entry, name='vaccination_entry'),path('treatementdetails',views.treatementdetails,name='treatementdetails'),
    path('bullandbullbuffaloprofile',views.bullandbullbuffaloprofile,name='bullandbullbuffaloprofile'),
    path('cowandcowbuffaloprofile',views.cowandcowbuffaloprofile,name='cowandcowbuffaloprofile'),
    path('cowcalfandbullcalfprofile',views.cowcalfandbullcalfprofile,name='cowcalfandbullcalfprofile'),
    path('cowandcowbuffaloedit', views.cowandcowbuffaloedit, name='cowandcowbuffaloedit'),
    path('cowcalfandbullcalfedit',views.cowcalfandbullcalfedit,name='cowcalfandbullcalfedit'),
    path('bullandbullbuffaloedit',views.bullandbullbuffaloedit,name='bullandbullbuffaloedit'),
    path('individualmilkreport',views.individualmilkreport,name='individualmilkreport'),
    path('individualmilkreport_pdf', views.individualmilkreport_pdf, name='individualmilkreport_pdf'),
    path('milk_data_overall_report_pdf', views.milk_data_overall_report_pdf, name='milk_data_overall_report_pdf'),
]


from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import  cattle_records, vaccination_record, calving_records, deworming_records,\
    alarm_records, milk_record, treatment_record, insemination_records
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
import datetime

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return redirect("signin")
    else:
        return render(request, "signin.html")

@login_required(login_url="error_page")
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        print('user created')
        return redirect("signin")
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect("signin")

def error_page(request):
    return JsonResponse({'error': 'The resource was not found'}, status=404)

@login_required(login_url="error_page")
def bull(request):
    existing_data = cattle_records.objects.values_list('name','tag_no').filter(breed='Bull')
    exist=[]
    for i in existing_data:
        temp_exist=[]
        temp_exist.append(i[0])
        temp_exist.append(i[1])
        exist.append(temp_exist)
    return render(request,'bull.html',{"exist":exist})

@login_required(login_url="error_page")
def buffalo_bull(request):
    existing_data = cattle_records.objects.values_list('name','tag_no').filter(breed='Buffalo_Bull')
    exist=[]
    for i in existing_data:
        temp_exist=[]
        temp_exist.append(i[0])
        temp_exist.append(i[1])
        exist.append(temp_exist)
    return render(request,'bullbuffalo.html',{"exist":exist})

@login_required(login_url="error_page")
def cow(request):
    existing_data = cattle_records.objects.values_list('name','tag_no').filter(breed='Cow')
    exist=[]
    for i in existing_data:
        temp_exist=[]
        temp_exist.append(i[0])
        temp_exist.append(i[1])
        exist.append(temp_exist)
    return render(request,'cow.html',{"exist":exist})

@login_required(login_url="error_page")
def buffalo_cow(request):
    existing_data = cattle_records.objects.values_list('name','tag_no').filter(breed='Buffalo_Cow')
    exist=[]
    for i in existing_data:
        temp_exist=[]
        temp_exist.append(i[0])
        temp_exist.append(i[1])
        exist.append(temp_exist)
    return render(request,'cowbuffalo.html',{"exist":exist})

@login_required(login_url="error_page")
def cow_calf(request):
    existing_data = cattle_records.objects.values_list('name','tag_no').filter(breed='Cow_Calf')
    exist=[]
    for i in existing_data:
        temp_exist=[]
        temp_exist.append(i[0])
        temp_exist.append(i[1])
        exist.append(temp_exist)
    return render(request,'cowcalf.html',{"exist":exist})

@login_required(login_url="error_page")
def buffalo_calf(request):
    existing_data = cattle_records.objects.values_list('name','tag_no').filter(breed='Buffalo_Calf')
    exist=[]
    for i in existing_data:
        temp_exist=[]
        temp_exist.append(i[0])
        temp_exist.append(i[1])
        exist.append(temp_exist)
    return render(request,'buffalocalf.html',{"exist":exist})

@login_required(login_url="error_page")
def bull_or_buffalo_entry(request):
    if request.is_ajax() and request.method == 'POST':
        bbb_tagnum = request.POST.get('bbb_tagnum')
        if cattle_records.objects.filter(tag_no=bbb_tagnum).exists():
            return JsonResponse({'status': 'Internal Server Error'}, status=500)
        else:
            bbb_name = request.POST.get('bbb_cname')
            bbb_sirename = request.POST.get('bbb_sirename')
            bbb_damname = request.POST.get('bbb_damname')
            bbb_breedname = request.POST.get('bbb_breedname')
            bbb_sex = request.POST.get('bbb_sex')
            bbb_dateofbirth = request.POST.get('bbb_dateofbirth')
            if bbb_tagnum != '' and bbb_name != '' and bbb_sirename != '' and bbb_damname != '' and bbb_breedname != '' and bbb_sex != '' and bbb_dateofbirth != '' :
                cattle_records(tag_no=bbb_tagnum, name=bbb_name,breed=bbb_breedname,sex=bbb_sex,dob=bbb_dateofbirth,sire_name=bbb_sirename,dam_name=bbb_damname).save()
                return JsonResponse({"tag_no": bbb_tagnum}, safe=False, status=200)
            else:
                return JsonResponse({'status': 'ValueError'}, status=400)

    breedname = request.GET.get('breedname')
    sex = request.GET.get('sex')
    return render(request,'bull_or_buffalo_entry.html',{"breedname":breedname,"sex":sex})

@login_required(login_url="error_page")
def cow_or_buffalo_cow_entry(request):
    if request.is_ajax() and request.method == 'POST':
        ccb_tagnum = request.POST.get('ccb_tagnum')
        if cattle_records.objects.filter(tag_no=ccb_tagnum).exists():
            return JsonResponse({'status': 'Internal Server Error'}, status=500)
        else:
            ccb_cname = request.POST.get('ccb_cname')
            ccb_sirename = request.POST.get('ccb_sirename')
            ccb_damname = request.POST.get('ccb_damname')
            ccb_breedname = request.POST.get('ccb_breedname')
            ccb_sex = request.POST.get('ccb_sex')
            ccb_dateofbirth = request.POST.get('ccb_dateofbirth')
            ccb_Bstatus = request.POST.get('ccb_Bstatus')
            ccb_Mstatus = request.POST.get('ccb_Mstatus')
            ccb_lactation = request.POST.get('ccb_lactation')
            ccb_breeddate = request.POST.get('ccb_breeddate')
            ccb_calvdate = request.POST.get('ccb_calvdate')
            ccb_Cgen = request.POST.get('ccb_Cgen')
            if ccb_tagnum != '' and ccb_cname != '' and ccb_sirename != '' and ccb_damname != '' and ccb_breedname != '' and ccb_sex != '' and ccb_dateofbirth != '' and ccb_Bstatus != '' and ccb_Mstatus != '' and ccb_lactation != '' and ccb_breeddate != '' and ccb_calvdate != '' and ccb_Cgen != '':
                cattle_records(tag_no=ccb_tagnum, name=ccb_cname,breed=ccb_breedname,sex=ccb_sex,dob=ccb_dateofbirth,sire_name=ccb_sirename,dam_name=ccb_damname,milking_status=ccb_Mstatus,breeding_status=ccb_Bstatus,no_of_lactation=ccb_lactation,last_breeding=ccb_breeddate,last_calving=ccb_calvdate,calf_gender=ccb_Cgen).save()
                return JsonResponse({"tag_no": ccb_tagnum}, safe=False, status=200)
            else:
                return JsonResponse({'status': 'ValueError'}, status=400)
    breedname = request.GET.get('breedname')
    sex = request.GET.get('sex')
    return render(request,'cow_or_buffalo_cow_entry.html',{"breedname":breedname,"sex":sex})

@login_required(login_url="error_page")
def cow_calf_or_buffalo_calf_entry(request):
    if request.is_ajax() and request.method == 'POST':
        ccbc_tagnum = request.POST.get('ccbc_tagnum')
        if cattle_records.objects.filter(tag_no=ccbc_tagnum).exists():
            return JsonResponse({'status': 'Internal Server Error'}, status=500)
        else:
            ccbc_cname = request.POST.get('ccbc_cname')
            ccbc_sirename = request.POST.get('ccbc_sirename')
            ccbc_damname = request.POST.get('ccbc_damname')
            ccbc_breedname = request.POST.get('ccbc_breedname')
            ccbc_sex = request.POST.get('ccbc_sex')
            ccbc_dateofbirth = request.POST.get('ccbc_dateofbirth')
            if ccbc_tagnum != '' and ccbc_cname != '' and ccbc_sirename != '' and ccbc_damname != '' and ccbc_breedname != '' and ccbc_sex != '' and ccbc_dateofbirth != '' :
                cattle_records(tag_no=ccbc_tagnum, name=ccbc_cname,breed=ccbc_breedname,sex=ccbc_sex,dob=ccbc_dateofbirth,sire_name=ccbc_sirename,dam_name=ccbc_damname).save()
                return JsonResponse({"tag_no": ccbc_tagnum}, safe=False, status=200)
            else:
                return JsonResponse({'status': 'ValueError'}, status=400)
    breedname = request.GET.get('breedname')
    sex = request.GET.get('sex')
    return render(request,'cow_calf_or_buffalo_calf_entry.html',{"breedname":breedname,"sex":sex})

@login_required(login_url="error_page")
def add_feed(request):
    if request.is_ajax() and request.method == 'POST':
        ad_tag_num = request.POST.get('ad_tag_num')
        ad_company1 = request.POST.get('ad_company1')
        ad_quantity1 = request.POST.get('ad_quantity1')
        ad_company2 = request.POST.get('ad_company2')
        ad_quantity2 = request.POST.get('ad_quantity2')
        if ad_tag_num != '' and ad_company1 != '' and ad_quantity1 != '' and ad_company2 != '' and ad_quantity2 != '':
            cattle_records.objects.filter(tag_no=ad_tag_num).update(concentrate1=ad_company1,
                                                                         quantity1=ad_quantity1,
                                                                         concentrate2=ad_company2,
                                                                         quantity2=ad_quantity2)
        else:
            return JsonResponse({'status': 'ValueError'}, status=400)
    tag_num = request.GET.get('tag_no')
    return render(request,'add_feed.html',{"tag_no":tag_num})

@login_required(login_url="error_page")
def milk_data_entry(request):
    if request.is_ajax() and request.method == 'POST':
        mr_tagno = request.POST.get('mr_tagno')
        mr_MilkRegdate = request.POST.get('mr_MilkRegdate')
        mreg_shift = request.POST.get('mreg_shift')
        mreg_MilkRegquantity = request.POST.get('mreg_MilkRegquantity')
        mreg_MilkRegFat = request.POST.get('mreg_MilkRegFat')
        mreg_MilkRegsnf = request.POST.get('mreg_MilkRegsnf')
        if mr_tagno != '' and mr_MilkRegdate != '' and mreg_shift != '' and mreg_MilkRegquantity != '' and mreg_MilkRegFat != '' and mreg_MilkRegsnf != '':
            milk_record(tag_no=mr_tagno, date=mr_MilkRegdate, shift=mreg_shift, quantity=mreg_MilkRegquantity,
                           fat=mreg_MilkRegFat, snf=mreg_MilkRegsnf).save()
            existing_data = milk_record.objects.all().filter(date=mr_MilkRegdate,shift=mreg_shift)
            milk_list=[]
            for rec in existing_data:
                temp_rec=[rec.tag_no,rec.quantity,rec.fat,rec.snf]
                milk_list.append(temp_rec)
            return JsonResponse({"milk_list":milk_list}, safe=False, status=200)
        else:
            return JsonResponse({'status': 'ValueError'}, status=400)
    else:
        existing_data = cattle_records.objects.values_list('tag_no').filter(milking_status='Milking')
        tag_list=[]
        for i in existing_data:
            for j in i:
                tag_list.append(j)
        context={
            "tag_list":tag_list
        }
    return render(request,'milk_reg.html',context)

@login_required(login_url="error_page")
def milk_data_overall_report(request):
    existing_data = cattle_records.objects.values_list('tag_no').filter(milking_status='Milking')
    tag_list = []
    for i in existing_data:
        for j in i:
            tag_list.append(j)
    context = {
        "tag_list": tag_list
    }
    return render(request,'milk_report.html',context)

@login_required(login_url="error_page")
def insemination_entry(request):
    return render(request,'insemination_entry.html')

@login_required(login_url="error_page")
def calving_entry(request):
    return render(request,'calving_entry.html')

@login_required(login_url="error_page")
def deworming_entry(request):
    return render(request,'deworming_entry.html')

@login_required(login_url="error_page")
def breeding_report(request):
    return render(request,'breeding_report.html')

@login_required(login_url="error_page")
def treatment_entry(request):
    return render(request,'treatment_entry.html')

@login_required(login_url="error_page")
def vaccination_entry(request):
    return render(request,'vaccination_entry.html')

@login_required(login_url="error_page")
def treatementdetails(request):
    return render(request,'treatmentdetails.html')

@login_required(login_url='error_page')
def bullandbullbuffaloprofile(request):
    tag_num = request.GET.get('tag_no')
    existing_data = cattle_records.objects.get(tag_no=tag_num)
    exist = {"name":existing_data.name,"tag_no":existing_data.tag_no,"breed":existing_data.breed,"sex":existing_data.sex,"dob":existing_data.dob,"sire_name":existing_data.sire_name,"dam_name":existing_data.dam_name,"concentrate1":existing_data.concentrate1,"quantity1":existing_data.quantity1,"concentrate2":existing_data.concentrate2,"quantity2":existing_data.quantity2}
    return render(request,'bullandbullbuffaloprofile.html', exist)

@login_required(login_url="error_page")
def cowandcowbuffaloprofile(request):
    tag_num = request.GET.get('tag_no')
    existing_data = cattle_records.objects.get(tag_no=tag_num)
    exist = {"name":existing_data.name,"tag_no":existing_data.tag_no,"breed":existing_data.breed,"sex":existing_data.sex,"dob":existing_data.dob,"no_of_lactation":existing_data.no_of_lactation,"breeding_status":existing_data.breeding_status,"milking_status":existing_data.milking_status,"last_breeding":existing_data.last_breeding,"last_calving":existing_data.last_calving,"calf_gender":existing_data.calf_gender,"sire_name":existing_data.sire_name,"dam_name":existing_data.dam_name,"concentrate1":existing_data.concentrate1,"quantity1":existing_data.quantity1,"concentrate2":existing_data.concentrate2,"quantity2":existing_data.quantity2}
    return render(request,'cowandcowbuffaloprofile.html', exist)

@login_required(login_url="error_page")
def cowcalfandbullcalfprofile(request):
    tag_num = request.GET.get('tag_no')
    existing_data = cattle_records.objects.get(tag_no=tag_num)
    exist = {"name":existing_data.name,"tag_no":existing_data.tag_no,"breed":existing_data.breed,"sex":existing_data.sex,"dob":existing_data.dob,"sire_name":existing_data.sire_name,"dam_name":existing_data.dam_name,"concentrate1":existing_data.concentrate1,"quantity1":existing_data.quantity1,"concentrate2":existing_data.concentrate2,"quantity2":existing_data.quantity2}
    return render(request,'cowcalfandbullcalfprofile.html', exist)

@login_required(login_url="error_page")
def cowandcowbuffaloedit(request):
    if request.is_ajax() and request.method == 'POST':
        cedit_data_from = request.POST.get('cedit_data_from')
        if cedit_data_from == 'save':
            ccbe_tagnum = request.POST.get('ccbe_tagnum')
            ccbe_tagnumold = request.POST.get('ccbe_tagnumold')
            if (cattle_records.objects.filter(tag_no=ccbe_tagnum).exists() and ccbe_tagnumold!=ccbe_tagnum):
                return JsonResponse({'status': 'Internal Server Error'}, status=500)
            else:
                ccbe_cname = request.POST.get('ccbe_cname')
                ccbe_sirename = request.POST.get('ccbe_sirename')
                ccbe_damname = request.POST.get('ccbe_damname')
                ccbe_dateofbirth = request.POST.get('ccbe_dateofbirth')
                ccbe_brstatus = request.POST.get('ccbe_brstatus')
                ccbe_mistatus = request.POST.get('ccbe_mistatus')
                ccbe_lactation = request.POST.get('ccbe_lactation')
                ccbe_breeddate = request.POST.get('ccbe_breeddate')
                ccbe_calvdate = request.POST.get('ccbe_calvdate')
                ccbe_Cgen = request.POST.get('ccbe_Cgen')
                ccbe_nameofcomp1 = request.POST.get('ccbe_nameofcomp1')
                ccbe_quantity1 = request.POST.get('ccbe_quantity1')
                ccbe_nameofcomp2 = request.POST.get('ccbe_nameofcomp2')
                ccbe_quantity2 = request.POST.get('ccbe_quantity2')
                if ccbe_tagnum != '' and ccbe_cname != '' and ccbe_sirename != '' and ccbe_damname != '' and ccbe_dateofbirth != '' and ccbe_brstatus != '' and ccbe_mistatus != '' and ccbe_lactation != '' and ccbe_breeddate != '' and ccbe_calvdate != '' and ccbe_Cgen != '' and ccbe_nameofcomp1 != '' and ccbe_quantity1 != '' and ccbe_nameofcomp2 != '' and ccbe_quantity2 != '':
                    cattle_records.objects.filter(tag_no=ccbe_tagnum).update(tag_no=ccbe_tagnum, name=ccbe_cname,dob=ccbe_dateofbirth,sire_name=ccbe_sirename,dam_name=ccbe_damname,milking_status=ccbe_mistatus,breeding_status=ccbe_brstatus,no_of_lactation=ccbe_lactation,last_breeding=ccbe_breeddate,last_calving=ccbe_calvdate,calf_gender=ccbe_Cgen,concentrate1=ccbe_nameofcomp1,quantity1=ccbe_quantity1,concentrate2=ccbe_nameofcomp2,quantity2=ccbe_quantity2)
                    return JsonResponse({"tag_no": ccbe_tagnum}, safe=False, status=200)
                else:
                    return JsonResponse({'status': 'ValueError'}, status=400)
        else:
            del_tag_no = request.POST.get('ccbd_tagnum')
            print(del_tag_no)
            extract_del=cattle_records.objects.get(tag_no=del_tag_no)
            extract_del.delete()
            return JsonResponse(safe=False, status=200)
    else:
        tag_num = request.GET.get('tag_no')
        existing_data = cattle_records.objects.get(tag_no=tag_num)
        context = {'name':existing_data.name,'tag_no':existing_data.tag_no,'breed':existing_data.breed,'sex':existing_data.sex,'dob':existing_data.dob,'nol':existing_data.no_of_lactation,'bstatus':existing_data.breeding_status,'mstatus':existing_data.milking_status,'lastbreed':existing_data.last_breeding,'lastcalv':existing_data.last_calving,'calfgen':existing_data.calf_gender,'sirename':existing_data.sire_name,'damname':existing_data.dam_name,'con1':existing_data.concentrate1,'quan1':int(existing_data.quantity1),'con2':existing_data.concentrate2,'quan2':int(existing_data.quantity2)}
    return render(request,'cowandcowbuffaloedit.html',context)

@login_required(login_url="error_page")
def cowcalfandbullcalfedit(request):
    if request.is_ajax() and request.method == 'POST':
        cedit_data_from = request.POST.get('cedit_data_from')
        if cedit_data_from == 'save':
            ccbe_tagnum = request.POST.get('ccbe_tagnum')
            ccbe_tagnumold = request.POST.get('ccbe_tagnumold')
            if (cattle_records.objects.filter(tag_no=ccbe_tagnum).exists() and ccbe_tagnumold!=ccbe_tagnum):
                return JsonResponse({'status': 'Internal Server Error'}, status=500)
            else:
                ccbe_cname = request.POST.get('ccbe_cname')
                ccbe_sirename = request.POST.get('ccbe_sirename')
                ccbe_damname = request.POST.get('ccbe_damname')
                ccbe_dateofbirth = request.POST.get('ccbe_dateofbirth')
                ccbe_nameofcomp1 = request.POST.get('ccbe_nameofcomp1')
                ccbe_quantity1 = request.POST.get('ccbe_quantity1')
                ccbe_nameofcomp2 = request.POST.get('ccbe_nameofcomp2')
                ccbe_quantity2 = request.POST.get('ccbe_quantity2')
                if ccbe_tagnum != '' and ccbe_cname != '' and ccbe_sirename != '' and ccbe_damname != '' and ccbe_dateofbirth != '' and ccbe_nameofcomp1 != '' and ccbe_quantity1 != '' and ccbe_nameofcomp2 != '' and ccbe_quantity2 != '':
                    cattle_records.objects.filter(tag_no=ccbe_tagnum).update(tag_no=ccbe_tagnum, name=ccbe_cname,dob=ccbe_dateofbirth,sire_name=ccbe_sirename,dam_name=ccbe_damname,concentrate1=ccbe_nameofcomp1,quantity1=ccbe_quantity1,concentrate2=ccbe_nameofcomp2,quantity2=ccbe_quantity2)
                    return JsonResponse({"tag_no": ccbe_tagnum}, safe=False, status=200)
                else:
                    return JsonResponse({'status': 'ValueError'}, status=400)
        else:
            del_tag_no = request.POST.get('ccbd_tagnum')
            print(del_tag_no)
            extract_del=cattle_records.objects.get(tag_no=del_tag_no)
            extract_del.delete()
            return JsonResponse(safe=False, status=200)
    else:
        tag_num = request.GET.get('tag_no')
        existing_data = cattle_records.objects.get(tag_no=tag_num)
        context = {'name':existing_data.name,'tag_no':existing_data.tag_no,'breed':existing_data.breed,'sex':existing_data.sex,'dob':existing_data.dob,'sirename':existing_data.sire_name,'damname':existing_data.dam_name,'con1':existing_data.concentrate1,'quan1':int(existing_data.quantity1),'con2':existing_data.concentrate2,'quan2':int(existing_data.quantity2)}
    return render(request,'cowcalfandbullcalfedit.html',context)

@login_required(login_url="error_page")
def bullandbullbuffaloedit(request):
    if request.is_ajax() and request.method == 'POST':
        cedit_data_from = request.POST.get('cedit_data_from')
        if cedit_data_from == 'save':
            ccbe_tagnum = request.POST.get('ccbe_tagnum')
            ccbe_tagnumold = request.POST.get('ccbe_tagnumold')
            if (cattle_records.objects.filter(tag_no=ccbe_tagnum).exists() and ccbe_tagnumold!=ccbe_tagnum):
                return JsonResponse({'status': 'Internal Server Error'}, status=500)
            else:
                ccbe_cname = request.POST.get('ccbe_cname')
                ccbe_sirename = request.POST.get('ccbe_sirename')
                ccbe_damname = request.POST.get('ccbe_damname')
                ccbe_dateofbirth = request.POST.get('ccbe_dateofbirth')
                ccbe_nameofcomp1 = request.POST.get('ccbe_nameofcomp1')
                ccbe_quantity1 = request.POST.get('ccbe_quantity1')
                ccbe_nameofcomp2 = request.POST.get('ccbe_nameofcomp2')
                ccbe_quantity2 = request.POST.get('ccbe_quantity2')
                if ccbe_tagnum != '' and ccbe_cname != '' and ccbe_sirename != '' and ccbe_damname != '' and ccbe_dateofbirth != '' and ccbe_nameofcomp1 != '' and ccbe_quantity1 != '' and ccbe_nameofcomp2 != '' and ccbe_quantity2 != '':
                    cattle_records.objects.filter(tag_no=ccbe_tagnum).update(tag_no=ccbe_tagnum, name=ccbe_cname,dob=ccbe_dateofbirth,sire_name=ccbe_sirename,dam_name=ccbe_damname,concentrate1=ccbe_nameofcomp1,quantity1=ccbe_quantity1,concentrate2=ccbe_nameofcomp2,quantity2=ccbe_quantity2)
                    return JsonResponse({"tag_no": ccbe_tagnum}, safe=False, status=200)
                else:
                    return JsonResponse({'status': 'ValueError'}, status=400)
        else:
            del_tag_no = request.POST.get('ccbd_tagnum')
            print(del_tag_no)
            extract_del=cattle_records.objects.get(tag_no=del_tag_no)
            extract_del.delete()
            return JsonResponse(safe=False, status=200)
    else:
        tag_num = request.GET.get('tag_no')
        existing_data = cattle_records.objects.get(tag_no=tag_num)
        context = {'name':existing_data.name,'tag_no':existing_data.tag_no,'breed':existing_data.breed,'sex':existing_data.sex,'dob':existing_data.dob,'nol':existing_data.no_of_lactation,'bstatus':existing_data.breeding_status,'mstatus':existing_data.milking_status,'lastbreed':existing_data.last_breeding,'lastcalv':existing_data.last_calving,'calfgen':existing_data.calf_gender,'sirename':existing_data.sire_name,'damname':existing_data.dam_name,'con1':existing_data.concentrate1,'quan1':int(existing_data.quantity1),'con2':existing_data.concentrate2,'quan2':int(existing_data.quantity2)}
    return render(request,'bullandbullbuffaloedit.html',context)

@login_required(login_url="error_page")
def individualmilkreport(request):
    tag_num = request.GET.get('tag_no')
    existing_data = cattle_records.objects.get(tag_no=tag_num)
    context = {'tag_no':existing_data.tag_no,'breed':existing_data.breed,'sex':existing_data.sex}
    return render(request,'individualmilkreport.html',context)

@login_required(login_url="error_page")
def individualmilkreport_pdf(request):
    from_date = request.GET.get('TReportdate')
    to_date = request.GET.get('TReportdate1')
    report_date = datetime.date.today().strftime("%d/%m/%Y")
    template_path = 'milkreport_pdf.html'
    existing_data = milk_record.objects.all().filter(date__range=[from_date,to_date]).order_by('date')
    context = {'existing_data': existing_data, 'report_date': report_date}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="client_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url="error_page")
def milk_data_overall_report_pdf(request):
    cow_tag = request.GET.get('cow_tag')
    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')
    shift = request.GET.get('shift')
    report_date = datetime.date.today().strftime("%d/%m/%Y")
    template_path = 'milkreport_pdf.html'
    existing_data = milk_record.objects.all().filter(tag_no=cow_tag,date__range=[fromdate,todate],shift=shift).order_by('tag_no')
    context = {'existing_data': existing_data, 'report_date': report_date}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="client_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response







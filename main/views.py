from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import lab_data, reports, patient, patient_dat
from datetime import date
from .utils import render_to_pdf
from random import random as rand
from django.contrib.auth.models import auth, User

dat = lab_data()


# Create your views here.


def home(request):
    return render(request, 'powell_home.html')


def check_result(request):
    if request.method == 'POST':
        global dat
        uid = request.POST['uid']
        p = patient.objects.all()
        p = p.filter(uid=uid)
        x = reports.objects.all()
        x = x.filter(uid=uid)
        if not p.exists():
            return render(request, 'check_result.html', context={'flag': True, 'flag_content': 'No Patient with such '
                                                                                               'UID, Try Again!!!'})
        for c in p.values():
            if c['age'] != int(request.POST['age']):
                print(c['age'], request.POST['age'])
                return render(request, 'check_result.html',
                              context={'flag': True, 'flag_content': 'Invalid Credentials'})
            if c['name'].lower() != request.POST['name'].lower():
                print(c['name'])
                return render(request, 'check_result.html', context={'flag': True, 'flag_content': 'Entered Patient '
                                                                                                   'Name is Invalid'})
            dat.name = c['name']
            dat.uid = c['uid']
            dat.age = c['age']
            dat.gender = c['gender']

        if x.exists():
            for r in x.values():
                dat.name = r['name']
                dat.uid = r['uid']
                dat.age = r['age']
                dat.gender = r['gender']
                dat.calcium = r['calcium']
                dat.cholesterol = r['cholesterol']
                dat.co2 = r['co2']
                dat.iron = r['iron']
                dat.glucose = r['glucose']
                dat.potassium = r['potassium']
                dat.phosphate = r['phosphate']
                dat.sodium = r['sodium']
                dat.date = r['date1']
            return render(request, 'progress.html',
                          context={'name': dat.name.upper(), 'uid': dat.uid, 'test_stat': 'Report Ready', 'flag': True})
        else:
            return render(request, 'progress.html',
                          context={'name': dat.name.upper(), 'uid': dat.uid, 'test_stat': 'In Process', 'flag': False})
    else:
        return render(request, 'check_result.html', context={'flag': False})


def view_pdf(request):
    x = add_sym()
    return render(request, 'pdf_design.html', context={'dat': x})


def register(request):
    if request.method == 'POST':
        uid = int(rand() * 100000)
        # print('uid is ', uid)
        p1 = patient(uid=uid, name=request.POST['name'], age=request.POST['age'], gender=request.POST['gender'],
                     phn=request.POST['phone'])
        p1.save()
        v = "Registration successful!!" + " UID: " + str(uid)
        return render(request, 'register.html', context={'flag': True, 'flag_content': v})
    else:
        return render(request, 'register.html', context={'flag': False})


def add_sym():
    global dat
    dat1 = lab_data()
    dat1.uid = dat.uid
    dat1.name = dat.name
    dat1.gender = dat.gender
    dat1.date = dat.date
    if int(dat.iron) > 170:
        dat1.iron = str(dat.iron) + "    H"
    if int(dat.iron) < 50:
        dat1.iron = str(dat.iron) + "    L"
    if int(dat.co2) > 31:
        dat1.co2 = str(dat.co2) + "    H"
    if int(dat.co2) < 21:
        dat1.co2 = str(dat.co2) + "    L"
    if int(dat.sodium) > 144:
        dat1.sodium = str(dat.sodium) + "    H"
    if int(dat.sodium) < 136:
        dat1.sodium = str(dat.sodium) + "    L"
    if int(dat.glucose) > 125:
        dat1.glucose = str(dat.glucose) + "    H"
    if int(dat.glucose) < 65:
        dat1.glucose = str(dat.glucose) + "    L"
    if float(dat.potassium) > 5.1:
        dat1.potassium = str(dat.potassium) + "    H"
    if float(dat.potassium) < 3.6:
        dat1.potassium = str(dat.potassium) + "    L"
    if float(dat.phosphate) > 4.5:
        dat1.phosphate = str(dat.phosphate) + "    H"
    if float(dat.calcium) > 10.3:
        dat1.calcium = str(dat.calcium) + "    H"
    if float(dat.calcium) < 8.8:
        dat1.calcium = str(dat.calcium) + "    L"
    if float(dat.cholesterol) > 199:
        dat1.cholesterol = str(dat.cholesterol) + "    H"
    if float(dat.cholesterol) < 120:
        dat1.cholesterol = str(dat.cholesterol) + "    L"
        return dat1


def gen_pdf(request):
    if request.method == 'POST':
        global dat
        dat.name = request.POST['name']
        dat.uid = request.POST['uid']
        x = patient.objects.filter(uid=dat.uid)
        dat.age = request.POST['age']
        dat.gender = request.POST['gender']
        dat.calcium = request.POST['calcium']
        dat.cholesterol = request.POST['cholesterol']
        dat.co2 = request.POST['co2']
        dat.iron = request.POST['iron']
        dat.glucose = request.POST['glucose']
        dat.potassium = request.POST['potassium']
        dat.phosphate = request.POST['phosphate']
        dat.sodium = request.POST['sodium']
        dat.date = date.today()

        d = reports(uid=dat.uid, name=dat.name, age=dat.age, gender=dat.gender, calcium=dat.calcium,
                    cholesterol=dat.cholesterol,
                    co2=dat.co2, iron=dat.iron, glucose=dat.glucose, potassium=dat.potassium, phosphate=dat.phosphate,
                    sodium=dat.sodium, date1=dat.date)
        if x is not None:
            d.save()
            return render(request, 'progress.html',
                          context={'name': dat.name, 'uid': dat.uid, 'gender': dat.gender, 'flag': True,
                                   'test_stat': 'Report Generated'})
        else:
            return render(request, 'gen_result.html', context={'flag': True, 'flag_content': 'No patient '
                                                                                             'registered with '
                                                                                             'the given UID'})
    else:
        html = render(request, 'gen_result.html', context={'flag': False})
        return HttpResponse(html)


def download(request):
    x = add_sym()
    pdf = render_to_pdf(context_dict={'dat': x})
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "LabResult_%s.pdf" % str(dat.uid)
    content = "inline; filename='%s'" % filename
    download1 = request.GET.get("download")
    if download1:
        content = "attachment; filename='%s'" % filename
    response['Content-Disposition'] = content
    return response


def pending_test(request):
    p1 = patient.objects.all()
    r1 = reports.objects.all()
    list1 = []
    for r in r1.values():
        uid = r['uid']
        p1 = p1.exclude(uid=uid)
    # print(p1.values())
    for p in p1.values():
        d = patient_dat()
        d.name = p['name']
        d.uid = p['uid']
        list1.append(d)
    # print(list1)
    return render(request, 'pending_test.html', context={'patients': list1})


def admin_panel(request):
    return render(request, 'admin.html')


from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from .models import Patients
from datetime import date
# Create your views here.
username = "Userdemo"
def index(request):
    return render(request, "index.html")


def login(request):
    global username
    lst=[]
    object1 = Patients.objects.all()
    for obj in object1:
        lst.append([obj.serial, obj.name, obj.age, obj.sex, obj.height, obj.weight,
                    obj.bgroup, obj.fname, obj.address, obj.city, obj.state, obj.mobile,
                    obj.email, obj.doctor, obj.disease, obj.med, obj.bill, obj.payment,
                    obj.date1, obj.date2])
    arg = {'lst': lst, 'username': username}
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['username'] = username
                return render(request, 'loggedin.html', arg)
        except:
            return render(request, 'loggedin.html', arg)


    return render(request, 'index.html', {"flag": 0})


def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return render(request, 'index.html')

def add(request):
    if request.method == "POST":
        name = request.POST.get('name', 'default')
        serial = request.POST.get('serial', 'default')
        father = request.POST.get('father', 'default')
        age = request.POST.get('age', 'default')
        sex = request.POST.get('sex', 'default')
        height = request.POST.get('height', 'default')
        weight = request.POST.get('weight', 'default')
        blood = request.POST.get('blood', 'default')
        address = request.POST.get('address', 'default')
        city = request.POST.get('city', 'default')
        state = request.POST.get('state', 'default')
        mobile = request.POST.get('mobile', 'default')
        email = request.POST.get('email', 'default')
        doctor = request.POST.get('doctor', 'default')
        disease = request.POST.get('disease', 'default')
        medicine = request.POST.get('medicine', 'default')
        bill = request.POST.get('bill', 'default')
        payment = request.POST.get('payment', 'default')
        date1 = request.POST.get('date1', 'default')
        date2 = request.POST.get('date2')
        obj = Patients(name=name, serial=serial, age=age, sex=sex, height=height, weight=weight, bgroup=blood, fname=father,
                      address=address, city=city, state=state, mobile=mobile, email=email, doctor=doctor, disease=disease, med=medicine,
                       bill=bill, payment=payment, date1=date1, date2=date2)
        obj.save()
        arg = {'header': 'Successfull', 'content': 'Registration has been completed Successfully'}
        return render(request, "success.html", arg)

def update(request):
    if request.method == "POST":
        name = request.POST.get('name')
        serial = request.POST.get('serial')
        object1 = Patients.objects.all()
        flag = 0
        for obj in object1:
            if obj.name == name and obj.serial == serial:
                arg = {'name':obj.name, 'serial':obj.serial, 'age':obj.age, 'sex':obj.sex, 'height':obj.height, 'weight':obj.weight, 'blood':obj.bgroup,
                       'father':obj.fname, 'address':obj.address, 'city':obj.city, 'state':obj.state, 'mobile':obj.mobile, 'email':obj.email, 'doctor':obj.doctor,
                       'disease':obj.disease, 'med':obj.med, 'bill':obj.bill, 'payment':obj.payment, 'date1':obj.date1, 'date2':obj.date2}
                return render(request, 'update.html', arg)
                break
        arg = {'header': 'Failed', 'content': 'Incorrect Details'}
        return render(request, 'success.html', arg)

def delete(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            serial = request.POST.get('serial')
            object1 = Patients.objects.all()
            flag = 0
            for obj in object1:
                if obj.name == name and obj.serial == serial:
                    obj.delete()
                    flag = 1
                    break
            arg = {'header': 'Successfull', 'content': 'Data has been deleted Successfully'}
            return render(request, 'success.html', arg)
        except:
            arg = {'header': 'Failed', 'content': 'Incorrect Details'}
            return render(request, 'success.html', arg)

def modify(request):
    if request.method == "POST":
        name = request.POST.get('name', 'default')
        serial = request.POST.get('serial', 'default')
        father = request.POST.get('father', 'default')
        age = request.POST.get('age', 'default')
        sex = request.POST.get('sex', 'default')
        height = request.POST.get('height', 'default')
        weight = request.POST.get('weight', 'default')
        blood = request.POST.get('blood', 'default')
        address = request.POST.get('address', 'default')
        city = request.POST.get('city', 'default')
        state = request.POST.get('state', 'default')
        mobile = request.POST.get('mobile', 'default')
        email = request.POST.get('email', 'default')
        doctor = request.POST.get('doctor', 'default')
        disease = request.POST.get('disease', 'default')
        medicine = request.POST.get('medicine', 'default')
        bill = request.POST.get('bill', 'default')
        payment = request.POST.get('payment', 'default')
        date1 = request.POST.get('date1', date.today())
        date2 = request.POST.get('date2')

        object1 = Patients.objects.all()
        flag = 0
        for obj in object1:
            if obj.serial == serial:
                obj.delete()
                flag = 1
                break
        new_obj = Patients(name=name, serial=serial, age=age, sex=sex, height=height, weight=weight, bgroup=blood, fname=father,
                       address=address, city=city, state=state, mobile=mobile, email=email, doctor=doctor, disease=disease,
                       med=medicine,
                       bill=bill, payment=payment, date1=date1, date2=date2)
        new_obj.save()

        arg = {'header': 'Successfull', 'content': 'Updation has been completed Successfully'}
        return render(request, "success.html", arg)

def search(request):
    if request.method == "POST":
        sk = request.POST.get('key', 'Not Found')
        lst=[]
        object1 = Patients.objects.all()

        if request.method == "POST":
            for obj in object1:
                if (sk.lower() in obj.name.lower() or sk.lower() in obj.serial or
                        sk.lower() in obj.age.lower() or sk.lower() in obj.sex.lower() or
                         sk.lower() in obj.height.lower() or sk.lower() in obj.weight.lower() or
                         sk.lower() in obj.bgroup.lower() or sk.lower() in obj.fname.lower() or
                         sk.lower() in obj.address.lower() or sk.lower() in obj.city.lower() or
                         sk.lower() in obj.state.lower() or sk.lower() in obj.mobile.lower() or
                         sk.lower() in obj.email.lower() or sk.lower() in obj.doctor.lower() or
                         sk.lower() in obj.disease.lower() or sk.lower() in obj.med.lower() or
                         sk.lower() in obj.bill.lower() or sk.lower() in obj.payment.lower() or
                         sk.lower() in obj.date1.lower() or sk.lower() in obj.date2.lower()):

                    lst.append([obj.serial, obj.name, obj.age, obj.sex, obj.height, obj.weight,
                                obj.bgroup, obj.fname, obj.address, obj.city, obj.state, obj.mobile,
                                obj.email, obj.doctor, obj.disease, obj.med, obj.bill, obj.payment,
                                obj.date1, obj.date2])
            if lst != []:
                arg = {'lst': lst, 'sk': sk}
                return render(request, 'search.html', arg)
            arg={'lst':lst, 'sk':sk +" Not Found"}
            return render(request, 'search.html', arg)
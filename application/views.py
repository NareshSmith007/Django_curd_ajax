from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *

def index(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,'Employee_view/display_employee.html',context)

def add_employee(request):
    return render(request,'Employee_view/add_employee.html')

def insert_employee(request):
        if not request.POST['name']: 
            return JsonResponse({"error": "Name is Required"})
        elif not request.POST['email']:
            return JsonResponse({"error": "Email is Required"})
        elif not request.POST['phone']:
            return JsonResponse({"error": "Phone is Required"})
        elif not request.POST['address']:
            return JsonResponse({"error": "Address is Required"})
        elif not request.POST['city']:
            return JsonResponse({"error": "City is Required"})
        elif not request.POST['zipcode']:
            return JsonResponse({"error": "ZipCode is Required"})
        else:
            if request.method=="POST":
                name=request.POST['name']
                email=request.POST['email']
                phone=request.POST['phone']
                address=request.POST['address']
                city=request.POST['city']
                zipcode=request.POST['zipcode']
                item=Employee(name=name,email=email,phone=phone,address=address,city=city,zipcode=zipcode)
                result=item.save()
                return JsonResponse({"success": "Employee Details insert Successfully"})
            else:
                return JsonResponse({"error":"Error Some where"})
               
def edit_employee(request,myid):
        get_val=Employee.objects.get(id=myid)
        context={
        'employee_detail':get_val,
        } 
        return render(request,'Employee_view/edit_employee.html',context)

def update_employee(request):
    if not request.POST['name']: 
        return JsonResponse({"error": "Name is Required"})
    elif not request.POST['email']:
        return JsonResponse({"error": "Email is Required"})
    elif not request.POST['phone']:
        return JsonResponse({"error": "Phone is Required"})
    elif not request.POST['address']:
        return JsonResponse({"error": "Address is Required"})
    elif not request.POST['city']:
        return JsonResponse({"error": "City is Required"})
    elif not request.POST['zipcode']:
        return JsonResponse({"error": "ZipCode is Required"})
    else:
        #  if request.method=="POST":
            item=Employee.objects.get(id=request.POST['id'])
            item.name=request.POST['name']
            item.email=request.POST['email']
            item.phone=request.POST['phone']
            item.address=request.POST['address']
            item.city=request.POST['city']
            item.zipcode=request.POST['zipcode']
            item.save()
            return JsonResponse({"success": "Employee Details Update Successfully"})
        #  else:
        #       return JsonResponse({"error":"Error Some where"})
        
def delete_employee(request):
    item=Employee.objects.get(id=request.GET['id'])
    item.delete()
    return JsonResponse({"success": "Employee Details Delete Successfully"})

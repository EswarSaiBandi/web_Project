from audioop import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, FileResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import F
from django.contrib import messages
from django.utils import timezone
import io
from hosteldb.settings import LOGIN_URL
from students.forms import addItemsForm,HumaddItemsForm
from institute.models import item,Customer,Humitem


class StudentTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_student or self.request.user.is_customer)

class RoomAllotmentTestMixin(UserPassesTestMixin):
    def test_func(self):
        if (self.request.user.is_student or self.request.user.is_customer) and self.request.user.student.roomdetail and self.request.user.student.roomdetail.room()!='-':
            return True
        return False

def student_check(user):
    return user.is_authenticated and (user.is_student or user.is_customer or user.is_admin)

def customer_check(user):
    return user.is_authenticated  and user.is_customer 
def room_allotment_check(user):
    return user.is_authenticated and user.is_student and user.student.roomdetail and user.student.roomdetail.room()!='-'

# Create your views here.

@user_passes_test(customer_check)
def home(request):
    user = request.user 
    print(user)
    print("hi") 
    return render(request, 'students/home.html' )




@user_passes_test(customer_check)
def business(request):
    user = request.user
     
    return render(request, 'students/Business.html' )



@user_passes_test(customer_check)
def businessBuyer(request):
    user = request.user
     
    return render(request, 'students/BusinessBuyer.html' )



@user_passes_test(customer_check)
def businessSeller(request):
    user = request.user
     
    return render(request, 'students/BusinessSeller.html' )


@user_passes_test(customer_check)
def  humanity(request):
    user = request.user
     
    return render(request, 'students/Humanity.html' )


@user_passes_test(customer_check)
def  humanityBuyer(request):
    user = request.user
     
    return render(request, 'students/HumanityBuyer.html' )


@user_passes_test(customer_check)
def  humanitySeller(request):
    user = request.user
     
    return render(request, 'students/HumanitySeller.html' )




 

from django.contrib.auth.decorators import user_passes_test
from students.forms import *
from django.shortcuts import render
 

@user_passes_test(customer_check)
def addItems(request):
    if request.method == 'POST':
        form = addItemsForm(request.POST)
        if(form.is_valid()):
            item_id = form.cleaned_data['item_id']
            price = form.cleaned_data['price']
            quantity_available = form.cleaned_data['quantity_available']
            # regulation = int(form.cleaned_data['regulation'])
            # if(( (form.cleaned_data['price']>=0) and (form.cleaned_data['quantity_available']>0))):
            r = item(item_id=item_id, quantity_available=quantity_available, price=price)
            r.save()
            msg = 'Item Added Successfully.'
            return render(request, 'students/addItems.html', {'form':form, 'msg':msg})
    else:
        form = addItemsForm()
    return render(request, 'students/addItems.html', {'form':form})

 

 
def itemsView(request):
    user = request.user
    items=item.objects.all()   
    form = itemsViewForm()
    return render(request, 'students/items_list.html', {'form':form,'items': items})


@user_passes_test(customer_check)
def HumaddItems(request):
    if request.method == 'POST':
        form = HumaddItemsForm(request.POST)
        if(form.is_valid()):
            item_id = form.cleaned_data['item_id']
            # price = form.cleaned_data['price']
            quantity_available = form.cleaned_data['quantity_available']
            # regulation = int(form.cleaned_data['regulation'])
            # if(( (form.cleaned_data['price']>=0) and (form.cleaned_data['quantity_available']>0))):
            r = Humitem(item_id=item_id, quantity_available=quantity_available)
            r.save()
            msg = 'Item Added Successfully.'
            return render(request, 'students/addItems.html', {'form':form, 'msg':msg})
    else:
        form = HumaddItemsForm()
    return render(request, 'students/addItems.html', {'form':form})

  


def HumitemsView(request):
    user = request.user
    items=Humitem.objects.all()   
    form = HumitemsViewForm()
    return render(request, 'students/Humitems_list.html', {'form':form,'items': items})

def send_birthday_mail():
    # search the query set for birthday and send him email
    from datetime import datetime
    # query_set=Student.objects.all()
    # bday_fellows=query_set.filter(dob=datetime.today().date())

    from django.core.mail import send_mail
    from django.conf import settings
    # for student in bday_fellows:
    #     from django.core.mail import EmailMultiAlternatives
    #     from django.template.loader import get_template
    #     from django.template import Context

    #     subject, from_email, to = 'Happy Birthday',settings.EMAIL_HOST_USER, student.user.email

    #     variables = {
    #     'student':student
    #     }
    #     html_content = get_template('students/birthyday_mail_template_html.html').render(variables)
    #     text_content = get_template('students/birthyday_mail_template_text.html').render(variables)
    #     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()

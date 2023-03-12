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
from location_field.models.plain import PlainLocationField

from hosteldb.settings import LOGIN_URL
from students.forms import *
from institute.models import *


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
    customer = user.customer 
    r=len(Order.objects.filter(customer_id=customer.id))
    r1=len(HumOrder.objects.filter(customer_id=customer.id))
    r2=len(Order.objects.filter(orderStatus="processing",customer_id=customer.id))
    r3=len(HumOrder.objects.filter(orderStatus="processing",customer_id=customer.id))
    r4=len(Order.objects.filter(orderStatus="prepared",customer_id=customer.id))
    r5=len(HumOrder.objects.filter(orderStatus="prepared",customer_id=customer.id))
    r6=len(Order.objects.filter(orderStatus="delivered",customer_id=customer.id))
    r7=len(HumOrder.objects.filter(orderStatus="delivered",customer_id=customer.id))
    r8=r+r1
    r9=r2+r3
    r10=r4+r5
    r11=r6+r7

 
    return render(request, 'students/home.html',{ 'customer':customer,'Total_Number_Of_Orders':r8,'Total_Number_Of_Orders_Processing':r9,'Total_Number_Of_Orders_Prepared':r10,'Total_Number_Of_Orders_Delivered':r11} )




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
    user = request.user 
    if request.method == 'POST':
        form = addItemsForm(request.POST)
        if(form.is_valid()):
             
            price = form.cleaned_data['price']
            quantity_available = form.cleaned_data['quantity_available']
            photo=form.cleaned_data['photo']
            foodType=form.cleaned_data['foodType']
            seller_id=user.id
            location=form.cleaned_data['location']
            # regulation = int(form.cleaned_data['regulation'])
            # if(( (form.cleaned_data['price']>=0) and (form.cleaned_data['quantity_available']>0))):
            r = item(foodType=foodType, quantity_available=quantity_available, price=price,photo=photo,seller_id=seller_id,location=location)
            r.save()          
            print("hiiii")  
            messages.success(request, 'Item has been Added Successfully.')

            return render(request, 'students/businessSeller.html', {'form':form,'user':user})
    else:
       
        form = addItemsForm()
    return render(request, 'students/addItems.html', {'form':form,'user':user})

 

 
def itemsView(request):
    user = request.user
    items=item.objects.all()   
    form = itemsViewForm()

    return render(request, 'students/items_list.html', {'form':form,'items': items,'user':user})


 
def TrackitemsView(request):
    user = request.user
    items=item.objects.filter(seller_id=user.id)
    print(items)
    form = itemsViewForm()
    return render(request, 'students/Trackitems_list.html', {'form':form,'items': items,'user':user})


@user_passes_test(customer_check)
def HumaddItems(request):
    user = request.user 
    if request.method == 'POST':
        form = HumaddItemsForm(request.POST)
        if(form.is_valid()):
             
            # price = form.cleaned_data['price']
            quantity_available = form.cleaned_data['quantity_available']
            photo=form.cleaned_data['photo']
            foodType=form.cleaned_data['foodType']
            seller_id=user.id
            location=form.cleaned_data['location']
            r = Humitem(foodType=foodType, quantity_available=quantity_available,photo=photo,seller_id=seller_id,location=location)
            r.save() 
            messages.success(request, 'Item has been Added Successfully.')

            
            return render(request, 'students/HumaddItems.html', {'form':form ,'user':user})
    else:
        form = HumaddItemsForm()
    return render(request, 'students/HumaddItems.html', {'form':form,'user':user})

 
  


def HumitemsView(request):
    user = request.user
    items=Humitem.objects.all()   
    form = HumitemsViewForm()
    return render(request, 'students/TrackHumitems_list.html', {'form':form,'items': items,'user':user})

def TrackHumitemsView(request):
    user = request.user
    items=Humitem.objects.filter(seller_id=user.id)
    print(items)
    form = itemsViewForm()
    return render(request, 'students/Trackitems_list.html', {'form':form,'items': items,'user':user})















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


@user_passes_test(customer_check)
def NeedFul(request):
    user = request.user 
    if request.method == 'POST':
        form = NeedFulForm(request.POST)
        if(form.is_valid()):
             
            need = form.cleaned_data['need']
            phone = form.cleaned_data['phone']
            photo=form.cleaned_data['photo']
            foodType=form.cleaned_data['foodType']
            # city=form.cleaned_data['city']
            location=form.cleaned_data['location']
            
            # regulation = int(form.cleaned_data['regulation'])
            # if(( (form.cleaned_data['price']>=0) and (form.cleaned_data['quantity_available']>0))):
            r = needful(need=need,phone=phone,location=location,foodType=foodType,photo=photo )
            r.save() 
            messages.success(request, 'Needful has been Added Successfully.')

            return render(request, 'students/needful.html', {'form':form,'user':user})
    else:
        form = NeedFulForm()
    return render(request, 'students/needful.html', {'form':form,'user':user})


def ServeNeedFul(request):
    user = request.user
    needful1=needful.objects.all()
    form = ServeNeedFulForm()
    return render(request, 'students/ServeNeedFul.html', {'form':form,'needful1': needful1,'user':user})


def OrderView(request,pk):
    user = request.user
    print("helloo",user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if(form.is_valid()):
            print(pk)
            customer_id = user.id
            item1=item.objects.filter(id=pk)
            
            # print(item.all())
            seller_id=item1[0].seller_id
            price=item1[0].price
            foodType=item1[0].foodType
            orderStatus='processing'
            quantity=item1[0].quantity_available
            quantity=quantity-1
            print(customer_id,price,orderStatus,seller_id)
            item.objects.filter(id=pk).update(quantity_available=quantity)

            r = Order(seller_id=seller_id,price=price,orderStatus=orderStatus,customer_id=customer_id,foodType=foodType )
            r.save() 
            messages.success(request, 'Order has been Ordered Successfully.')

            return render(request, 'students/business.html', {'form':form, 'user':user})
    
    form = OrderForm()
    return render(request, 'students/Order.html', {'form':form,'user':user})


 


def SellerOrderView(request):
    user = request.user
    orders=Order.objects.filter(seller_id=user.id)
    form = SellerOrderViewForm()
    return render(request, 'students/SellerOrderView.html', {'form':form,'orders': orders,'user':user})






 

def ChangeOrderStatus(request,pk):
    user = request.user 
    print(pk)
    r=Order.objects.filter(id=pk)
    print(r[0].orderStatus)
    if(r[0].orderStatus=="processing"):
        r=Order.objects.filter(id=pk).update(orderStatus='prepared')
         
    
    messages.success(request, 'Status of the Order has been Successfully changed to Prepared.')

    
    orders=Order.objects.filter(seller_id=user.id)
    return render(request, 'students/SellerOrderView.html', {'user':user,'orders': orders})




def CustomerOrdersView(request):
    user = request.user
    orders=Order.objects.filter(customer_id=user.id) 
    return render(request, 'students/CustomerOrdersView.html', {'orders': orders,'user':user})



def ChangeOrderStatustoDelivered(request,pk):
    user = request.user
    print("helloo",user)
    print(pk)
    r=Order.objects.filter(id=pk)
    print(r[0].orderStatus)
    if(r[0].orderStatus=="prepared"):
        r=Order.objects.filter(id=pk).update(orderStatus='delivered')
         
    messages.success(request, 'Status of the Order has been Successfully changed to delivered.')

    orders=Order.objects.filter(customer_id=user.id)
    return render(request, 'students/CustomerOrdersView.html', {'user':user,'orders': orders})








def HumOrderView(request,pk):
    user = request.user 
    if request.method == 'POST':
        form = HumOrderForm(request.POST)
        if(form.is_valid()):
            print(pk)
            customer_id = user.id
            item1=Humitem.objects.filter(id=pk)
            
            # print(item.all())
            seller_id=item1[0].seller_id
            foodType=item1[0].foodType
            # price=item1[0].price
            orderStatus='processing'
            quantity=item1[0].quantity_available
            quantity=quantity-1
            print(customer_id,orderStatus,seller_id)
            Humitem.objects.filter(id=pk).update(quantity_available=quantity)

            r = HumOrder(seller_id=seller_id,orderStatus=orderStatus,customer_id=customer_id,foodType=foodType )
            r.save()
            
            messages.success(request, 'Order has been Added Successfully.')

            return render(request, 'students/HumOrder.html', {'form':form, 'user':user})
    
    form = OrderForm()
    return render(request, 'students/HumOrder.html', {'form':form,'user':user})


 


def HumSellerOrderView(request):
    user = request.user
    orders=HumOrder.objects.filter(seller_id=user.id)
    form = HumSellerOrderViewForm()
    return render(request, 'students/HumSellerOrderView.html', {'form':form,'orders': orders,'user':user})






 

def HumChangeOrderStatus(request,pk):
    user = request.user
    print("helloo",user)
    print(pk)
    r=HumOrder.objects.filter(id=pk)
    print(r[0].orderStatus)
    if(r[0].orderStatus=="processing"):
        r=HumOrder.objects.filter(id=pk).update(orderStatus='prepared')
         
    
    messages.success(request, 'Status of the Order has been Successfully changed to Prepared.')
    
    orders=HumOrder.objects.filter(seller_id=user.id)
    return render(request, 'students/HumSellerOrderView.html', {'user':user,'orders': orders})




def HumCustomerOrdersView(request):
    user = request.user
    orders=HumOrder.objects.filter(customer_id=user.id) 
    return render(request, 'students/HumCustomerOrdersView.html', {'orders': orders,'user':user})



def HumChangeOrderStatustoDelivered(request,pk):
    user = request.user
    print("helloo",user)
    print(pk)
    r=HumOrder.objects.filter(id=pk)
    print(r[0].orderStatus)
    if(r[0].orderStatus=="prepared"):
        r=HumOrder.objects.filter(id=pk).update(orderStatus='delivered')
         
    messages.success(request, 'Status of the Order has been Successfully changed to delivered.')

    orders=HumOrder.objects.filter(customer_id=user.id)
    return render(request, 'students/HumCustomerOrdersView.html', {'user':user,'orders': orders})




def SearchByCost(request):
    if request.method == 'POST':
        user = request.user
        searchWord = request.POST.get('search','')
        items=item.objects.all()
        items1=[]
        for i in range(len(items)): 
            if(items[i].price<=int(searchWord)):
                    items1.append(items[i])
            
        
        messages.success(request, 'Items have been Successfully Filtered.')
        return render(request, 'students/items_list.html', {'user':user,'items': items1})
    
 


def TotalOrdersView(request):
    user=request.user

    orders=Order.objects.filter(customer_id=user.id)
    Humorders=HumOrder.objects.filter(customer_id=user.id)
    messages.success(request, 'Displaying all the Orders')
    return render(request, 'students/TotalOrdersView.html', {'user':user,'orders': orders,'Humorders':Humorders})




def TotalOrdersViewProcessing(request):
    user=request.user

    orders=Order.objects.filter(customer_id=user.id,orderStatus='processing')
    Humorders=HumOrder.objects.filter(customer_id=user.id,orderStatus='processing')
    messages.success(request, 'Displaying all the Orders that are being Processed')
    return render(request, 'students/TotalOrdersView.html', {'user':user,'orders': orders,'Humorders':Humorders})



def TotalOrdersViewPrepared(request):
    user=request.user

    orders=Order.objects.filter(customer_id=user.id,orderStatus='prepared')
    Humorders=HumOrder.objects.filter(customer_id=user.id,orderStatus='prepared')
    messages.success(request, 'Displaying all the Orders that are prepared')
    return render(request, 'students/TotalOrdersView.html', {'user':user,'orders': orders,'Humorders':Humorders})



def TotalOrdersViewDelivered(request):
    user=request.user

    orders=Order.objects.filter(customer_id=user.id,orderStatus='delivered')
    Humorders=HumOrder.objects.filter(customer_id=user.id,orderStatus='delivered')
    messages.success(request, 'Displaying all the Orders that are delivered')
    return render(request, 'students/TotalOrdersView.html', {'user':user,'orders': orders,'Humorders':Humorders})



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
    # customer = user.student
    print(user)
    print("hi")
    # print(user.__dict__)
    # user=user.customer
    # print(user.customer.gender)
    # present_dates_count = 0
    # absent_dates_count = 0
    # if user.student.roomdetail and user.student.roomdetail.room()=='-':
    #     raise Http404('You are not allocated any room yet')
    # if Attendance.objects.filter(student=student).exists():
    #     present_dates_count = (student.attendance and student.attendance.present_dates and len(student.attendance.present_dates.split(','))) or 0
    #     absent_dates_count = (student.attendance and student.attendance.absent_dates and len(student.attendance.absent_dates.split(','))) or 0
    # outing_count = 0
    # for outing in student.outing_set.all():
    #     if outing.is_upcoming():
    #         outing_count+=1
    # outing_rating = student.outing_rating
    # discipline_rating = student.discipline_rating
    # complaints = Complaint.objects.filter(user = user)
    # announce_obj = student.related_announcements()[:5]
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

class itemsView(StudentTestMixin, ListView):
    model = Customer
    template_name = 'students/items_list.html'
    context_object_name = 'items_list'

    def get_queryset(self):
        items_set = item.objects.filter() #.filter(student=self.request.user.student).annotate(outTime=F('outinginouttimes__outTime'), \
            #inTime=F('outinginouttimes__inTime'))

        print(items_set.all())
        return items_set



class HumaddItems(StudentTestMixin, SuccessMessageMixin, CreateView):
    model = Humitem
    form_class = HumaddItemsForm
    template_name = 'students/HumaddItems.html'
    success_url = reverse_lazy('students:HumaddItems')
    success_message = 'Item successfully Added!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Add Items'
        return context
    def get_form_kwargs(self):
        kwargs = super(HumaddItems, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    def form_valid(self, form):
        # form.instance.student = self.request.user.student
        return super().form_valid(form)



class HumitemsView(StudentTestMixin, ListView):
    model = Customer
    template_name = 'students/Humitems_list.html'
    context_object_name = 'items_list'

    def get_queryset(self):
        items_set = Humitem.objects.filter() #.filter(student=self.request.user.student).annotate(outTime=F('outinginouttimes__outTime'), \
            #inTime=F('outinginouttimes__inTime'))

        print(items_set.all())
        return items_set
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

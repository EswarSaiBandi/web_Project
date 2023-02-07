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



class StudentTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_student

class RoomAllotmentTestMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_student and self.request.user.student.roomdetail and self.request.user.student.roomdetail.room()!='-':
            return True
        return False

def student_check(user):
    return user.is_authenticated and (user.is_student or user.is_customer or user.is_admin)

def room_allotment_check(user):
    return user.is_authenticated and user.is_student and user.student.roomdetail and user.student.roomdetail.room()!='-'

# Create your views here.

@user_passes_test(student_check)
def home(request):
    user = request.user
    # student = user.student
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

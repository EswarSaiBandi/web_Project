from unicodedata import decimal
from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.validators import MinLengthValidator
from institute.validators import numeric_only, date_no_future

from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Admin(models.Model):


    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
    )

     

    def photo_storage_path(instance, filename):
        extension = filename.split('.')[-1]
        return 'Student-Photos/Year-{}/{}.{}'.format(instance.year, instance.regd_no, extension)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    account_email = models.EmailField(unique=True, null=True, blank=True)
    # regd_no = models.CharField(unique=True, null=False, max_length=8, validators=[MinLengthValidator(6)])
    # roll_no = models.CharField(unique=True, null=True, blank=True, max_length=8, validators=[MinLengthValidator(6)])
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=True, blank=True)
    # year = models.IntegerField(null=False, choices=YEAR)
    # branch = models.CharField(max_length=40,null=True, blank=True)
    gender = models.CharField(max_length=7,choices=GENDER,null=False)
    # pwd = models.BooleanField(null=False, default=False, blank=True)
    # community = models.CharField(max_length=25, null=True, blank=True)
    aadhar_number = models.CharField(max_length=12, null=True, blank=True, validators=[MinLengthValidator(4)], default='0000')
    dob = models.DateField(null=True, default="2000-01-01",validators=[date_no_future], blank=True)
    # blood_group = models.CharField(max_length=25, null=True, blank=True)
    # father_name = models.CharField(max_length=100, null=True, blank=True)
    # mother_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(null=False, max_length=10, validators=[numeric_only])
    # parents_phone = models.CharField(null=True, max_length=10, validators=[numeric_only], blank=True)
    # emergency_phone = models.CharField(null=True, blank=True, max_length=10, validators=[numeric_only])
    address = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to=photo_storage_path)
    # is_hosteller = models.BooleanField(null=False, default=True)
    # outing_rating = models.DecimalField(null=False,blank=True, default=5.0, max_digits=3, decimal_places=2)
    # discipline_rating = models.DecimalField(null=False, blank=True, default=5.0, max_digits=3, decimal_places=2)
    # specialization = models.CharField(max_length=15, choices=PROGRAMME_OPTIONS, null=False)

     

   

# Create your models here.
class Customer(models.Model):


    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
    )

     

    def photo_storage_path(instance, filename):
        extension = filename.split('.')[-1]
        return 'Student-Photos/Year-{}/{}.{}'.format(instance.year, instance.regd_no, extension)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    account_email = models.EmailField(unique=True, null=True, blank=True)
    # regd_no = models.CharField(unique=True, null=False, max_length=8, validators=[MinLengthValidator(6)])
    # roll_no = models.CharField(unique=True, null=True, blank=True, max_length=8, validators=[MinLengthValidator(6)])
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=True, blank=True)
    # year = models.IntegerField(null=False, choices=YEAR)
    # branch = models.CharField(max_length=40,null=True, blank=True)
    gender = models.CharField(max_length=7,choices=GENDER,null=False)
    # pwd = models.BooleanField(null=False, default=False, blank=True)
    # community = models.CharField(max_length=25, null=True, blank=True)
    aadhar_number = models.CharField(max_length=12, null=True, blank=True, validators=[MinLengthValidator(4)], default='0000')
    dob = models.DateField(null=True, default="2000-01-01",validators=[date_no_future], blank=True)
    # blood_group = models.CharField(max_length=25, null=True, blank=True)
    # father_name = models.CharField(max_length=100, null=True, blank=True)
    # mother_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(null=False, max_length=10, validators=[numeric_only])
    # parents_phone = models.CharField(null=True, max_length=10, validators=[numeric_only], blank=True)
    # emergency_phone = models.CharField(null=True, blank=True, max_length=10, validators=[numeric_only])
    address = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to=photo_storage_path)
    # is_hosteller = models.BooleanField(null=False, default=True)
    # outing_rating = models.DecimalField(null=False,blank=True, default=5.0, max_digits=3, decimal_places=2)
    # discipline_rating = models.DecimalField(null=False, blank=True, default=5.0, max_digits=3, decimal_places=2)
    # specialization = models.CharField(max_length=15, choices=PROGRAMME_OPTIONS, null=False)

    

      
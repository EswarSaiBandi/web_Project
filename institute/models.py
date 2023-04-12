from django.db import models 
from django.conf import settings
from django.core.validators import MinLengthValidator
from institute.validators import numeric_only, date_no_future 
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
    adm_id = models.CharField(unique=True, null=False, max_length=8, validators=[MinLengthValidator(6)])
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
    cus_id = models.CharField(unique=True, null=False, max_length=8, validators=[MinLengthValidator(6)])
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
    def __str__(self):
        return str(self.cus_id)
    




class item(models.Model):
    foodTypeOptions=(
         ("Veg","Veg"),
         ("Non Veg","Non Veg"),
    )

    location=(
         ("Hyderabad","Hyderabad"),
         ("Bangalore","Bangalore"),
         ("Mumbai","Mumbai"),
         ("Delhi","Delhi"),
         ("Kolkota","Kolkota"),


    )

    
    def photo_storage_path(instance, filename):
            extension = filename.split('.')[-1]
             

            return 'Student-Photos/Year-{}.{}'.format( instance.id, extension)

    name=models.CharField(max_length=255,null=False)
    quantity_available = models.IntegerField(null=False,default=1)
    price=models.DecimalField(null=False,  max_digits=10, decimal_places=2)
    photo = models.FileField(null=True,blank=True)
    foodType=models.CharField(max_length=25,null=False,choices=foodTypeOptions)
    seller_id = models.IntegerField( null=False )
    location=models.CharField(max_length=25,null=False,choices=location)
    

    


class Humitem(models.Model):
    foodTypeOptions=(
         ("Veg","Veg"),
         ("Non Veg","Non Veg"),
    )
    location=(
         ("Hyderabad","Hyderabad"),
         ("Bangalore","Bangalore"),
         ("Mumbai","Mumbai"),
         ("Delhi","Delhi"),
         ("Kolkota","Kolkota"),


    )
    def photo_storage_path(instance, filename):
            extension = filename.split('.')[-1]
            return 'Student-Photos/Year-{}/{}.{}'.format(instance.year, instance.regd_no, extension)

    
    quantity_available = models.IntegerField(null=False,default=1)
    name=models.CharField(max_length=255,null=False)

    # price=models.DecimalField(null=False,  max_digits=10, decimal_places=2)
    photo = models.FileField(null=True,blank=True)

    foodType=models.CharField(max_length=25,null=False,choices=foodTypeOptions,default="Non Veg")
    seller_id = models.IntegerField( null=False )
    location=models.CharField(max_length=25,null=False,choices=location)


    

class needful(models.Model):
    foodTypeOptions=(
         ("Vegetarian","Vegetarian"),
         ("Non Vegetarian","Non Vegetarian"),
    )
    def photo_storage_path(instance, filename):
            extension = filename.split('.')[-1]
            return 'Student-Photos/Year-{}/{}.{}'.format(instance.year, instance.regd_no, extension)

    location = models.CharField(max_length=255)
    # location = PlainLocationField(based_fields=['city'], zoom=7)
    photo = models.FileField(null=True,blank=True)
    name=models.CharField(max_length=255)
    phone = models.CharField(null=False, max_length=10, validators=[numeric_only])
    foodType=models.CharField(max_length=25,null=False,choices=foodTypeOptions)
    need = models.CharField(max_length=255)

    # seller_id = models.IntegerField( null=False )

    



# Create your models here.
class Order(models.Model):
    orderStatusOptions=(
        ('processing','processing'),
        ('prepared','prepared'),
        ('delivered','delivered'),

    )
    location=(
         ("Hyderabad","Hyderabad"),
         ("Bangalore","Bangalore"),
         ("Mumbai","Mumbai"),
         ("Delhi","Delhi"),
         ("Kolkota","Kolkota"),
    )
    foodTypeOptions=(
         ("Veg","Veg"),
         ("Non Veg","Non Veg"),
    )
    
    customer_id=models.IntegerField(max_length=100)
    seller_id=models.IntegerField(max_length=100)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(null=True,blank=True,  max_digits=3, decimal_places=2)
    review= models.CharField(null=True,blank=True,  max_length=255)
    orderStatus=models.CharField(choices=orderStatusOptions,max_length=255)
    foodType=models.CharField(max_length=25,null=False,choices=foodTypeOptions)
    location=models.CharField(max_length=25,null=False,choices=location)
    name=models.CharField(max_length=255,null=False)
    photo = models.FileField(null=True,blank=True)



    


 



# Create your models here.
class HumOrder(models.Model):
    orderStatusOptions=(
        ('processing','processing'),
        ('prepared','prepared'),
        ('delivered','delivered'),

    )
    foodTypeOptions=(
         ("Veg","Veg"),
         ("Non Veg","Non Veg"),
    )
    location=(
         ("Hyderabad","Hyderabad"),
         ("Bangalore","Bangalore"),
         ("Mumbai","Mumbai"),
         ("Delhi","Delhi"),
         ("Kolkota","Kolkota"),
    )

    
    customer_id=models.IntegerField(max_length=100)
    seller_id=models.IntegerField(max_length=100)
    # price=models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(null=True,blank=True,  max_digits=3, decimal_places=2)
    review= models.CharField(null=True,blank=True,  max_length=255)
    orderStatus=models.CharField(choices=orderStatusOptions,max_length=255)
    foodType=models.CharField(max_length=25,null=False,choices=foodTypeOptions)
    location=models.CharField(max_length=25,null=False,choices=location)
    name=models.CharField(max_length=255,null=False)
    photo = models.FileField(null=True,blank=True)


    
from django.db import models  
class Employee(models.Model):  
    firstname= models.CharField(null=True,blank=True,  max_length=50)
    lastname= models.CharField(null=True,blank=True,  max_length=50)
    account_email = models.EmailField(unique=True, null=True, blank=True)
    seller_id=models.IntegerField(max_length=100)

    file      = models.FileField()
from django import forms
from django.utils import timezone
from institute.models import item,Humitem,Customer
from django_auth.models import User
from django.db.models import Q
from location_field.models.plain import PlainLocationField

from institute.validators import numeric_only


 

class addItemsForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(addItemsForm, self).__init__(*args, **kwargs)
        foodTypeOptions=(
        ( None, 'Select'),
         ("Veg","Veg"),
         ("Non Veg","Non Veg"),
        )
        foodType = forms.CharField(max_length=25,  widget=forms.Select(choices=foodTypeOptions))

        # foodType=forms.Select(choices=foodTypeOptions)
        photo=forms.ImageField(required=False,label='Upload Photo')

        price=forms.DecimalField(label='Enter Price')
         
        quantity_available=forms.IntegerField(label='Enter Quantity')
 
        self.fields['foodType'] = foodType
        self.fields['quantity_available'] = quantity_available 
        self.fields['price'] = price 
        self.fields['photo'] = photo
        
        

class HumaddItemsForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(HumaddItemsForm, self).__init__(*args, **kwargs)
        foodTypeOptions=(
        ( None, 'Select'),
         ("Veg","Veg"),
         ("Non Veg","Non Veg"),
        )
        foodType = forms.CharField(max_length=25,  widget=forms.Select(choices=foodTypeOptions))

        # foodType=forms.Select(choices=foodTypeOptions)
        photo=forms.ImageField(required=False,label='Upload Photo')

        # price=forms.DecimalField(label='Enter Price')
         
        quantity_available=forms.IntegerField(label='Enter Quantity')
 
        self.fields['foodType'] = foodType
        self.fields['quantity_available'] = quantity_available 
        # self.fields['price'] = price 
        self.fields['photo'] = photo
         
 
class itemsViewForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(itemsViewForm,self).__init__(*args, **kwargs)
        
         


class HumitemsViewForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(HumitemsViewForm,self).__init__(*args, **kwargs)
         
 


class NeedFulForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(NeedFulForm, self).__init__(*args, **kwargs)
        foodTypeOptions=(
        ( None, 'Select'),
         ("Vegetarian","Vegetarian"),
         ("Non Vegetarian","Non Vegetarian"),
        )
        foodType = forms.CharField(max_length=25,  widget=forms.Select(choices=foodTypeOptions))

        # foodType=forms.Select(choices=foodTypeOptions)
        photo=forms.ImageField(required=False,label='Upload Photo')
        phone=forms.CharField(max_length=10)
        need=forms.CharField(max_length=255)
        location = forms.CharField(max_length=255)
        # location = PlainLocationField(based_fields=['city'], zoom=7)
        # price=forms.DecimalField(label='Enter Price')
          
 
        self.fields['foodType'] = foodType
        self.fields['need'] = need
        # self.fields['price'] = price 
        self.fields['photo'] = photo
        self.fields['phone'] = phone
        # self.fields['city'] = city
        self.fields['location'] = location
        


class ServeNeedFulForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(ServeNeedFulForm,self).__init__(*args, **kwargs)
         
 



         

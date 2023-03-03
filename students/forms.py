from django import forms
from django.utils import timezone
from institute.models import item,Humitem,Customer
from django_auth.models import User
from django.db.models import Q
from institute.validators import numeric_only


 

class addItemsForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(addItemsForm, self).__init__(*args, **kwargs)
        item_id=forms.IntegerField(label='Enter Id')

        price=forms.DecimalField(label='Enter Price')
        # photo=forms.
        quantity_available=forms.IntegerField(label='Enter Quantity')
 
        self.fields['item_id'] = item_id
        self.fields['price'] = price 
        self.fields['quantity_available'] = quantity_available 
        # self.fields['regulation'] = forms.CharField(label='Regulation Code',min_length=1)
        # if  price  and (0 >= price):
        #     raise forms.ValidationError("Price should be greater than 0")
        # if  quantity_available  and (0 > quantity_available):
        #     raise forms.ValidationError("Invalid Quantity,Quantity should be greater than 0")
        

class HumaddItemsForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(HumaddItemsForm, self).__init__(*args, **kwargs)
        item_id=forms.IntegerField(label='Enter Id')

        # price=forms.DecimalField(label='Enter Price')
        # photo=forms.
        quantity_available=forms.IntegerField(label='Enter Quantity')
 
        self.fields['item_id'] = item_id
        # self.fields['price'] = price 
        self.fields['quantity_available'] = quantity_available 
        # self.fields['regulation'] = forms.CharField(label='Regulation Code',min_length=1)
        # if  price  and (0 >= price):
        #     raise forms.ValidationError("Price should be greater than 0")
        # if  quantity_available  and (0 > quantity_available):
        #     raise forms.ValidationError("Invalid Quantity,Quantity should be greater than 0")
        
 
class itemsViewForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(itemsViewForm,self).__init__(*args, **kwargs)
         


class HumitemsViewForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(HumitemsViewForm,self).__init__(*args, **kwargs)
         
 
    
from django import forms
from django.utils import timezone
from institute.models import item,Humitem,Customer
from django_auth.models import User
from django.db.models import Q
from institute.validators import numeric_only


# class addItemsForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         if 'request' in kwargs.keys():
#             self.request = kwargs.pop('request')
#         super(addItemsForm, self).__init__(*args, **kwargs)
        
#     class Meta:
#         model = item
#         fields = ['item_id', 'quantity_available', 'price', 'photo']

#         labels = {
#             'item_id': 'item Id',
#             'quantity_available': 'Quantity',
#             'price': 'price',
#             'photo': 'photo',
             
#         }
#     def clean(self):
#         cleaned_data = super().clean()
#         item_id = cleaned_data.get('item_id')
#         quantity_available= cleaned_data.get('quantity_available')
#         price = cleaned_data.get('price')
#         photo = cleaned_data.get('photo')
#         # user = User.objects.get(email=self.request.user)
#         # student = Customer.objects.get(user_id=user.id)
#         # outings = Outing.objects.filter(~Q(permission__in=['Revoked', 'Rejected']),student_id=student.id).exclude(status='Closed')
#         if  price  and (0 >= price):
#             raise forms.ValidationError("Price should be greater than 0")
#         if  quantity_available  and (0 > quantity_available):
#             raise forms.ValidationError("Invalid Quantity,Quantity should be greater than 0")
        
        
#         return cleaned_data



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
        


class HumaddItemsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'request' in kwargs.keys():
            self.request = kwargs.pop('request')
        super(HumaddItemsForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Humitem
        fields = ['item_id', 'quantity_available', 'photo']

        labels = {
            'item_id': 'item Id',
            'quantity_available': 'Quantity',
            'photo': 'photo',
             
        }
    def clean(self):
        cleaned_data = super().clean()
        item_id = cleaned_data.get('item_id')
        quantity_available= cleaned_data.get('quantity_available')
        photo = cleaned_data.get('photo')
        # user = User.objects.get(email=self.request.user)
        # student = Customer.objects.get(user_id=user.id)
        # outings = Outing.objects.filter(~Q(permission__in=['Revoked', 'Rejected']),student_id=student.id).exclude(status='Closed')
        if  quantity_available  and (0 > quantity_available):
            raise forms.ValidationError("Invalid Quantity,Quantity should be greater than 0")
        
        
        return cleaned_data

    
    
   
    
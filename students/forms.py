from django import forms 


 

class addItemsForm(forms.Form):
     
        foodTypeOptions=(
        ( None, 'Select'),
         ("Veg","Veg"),
         ("Non Veg","Non Veg"),
        )
        location=(
         ( None, 'Select'),
         ("Hyderabad","Hyderabad"),
         ("Bangalore","Bangalore"),
         ("Mumbai","Mumbai"),
         ("Delhi","Delhi"),
         ("Kolkota","Kolkota"),
        )

        foodType = forms.CharField(max_length=25,  widget=forms.Select(choices=foodTypeOptions))
        location = forms.CharField(max_length=25,  widget=forms.Select(choices=location))
        name = forms.CharField(max_length=255)
 
        price=forms.DecimalField(label='Enter Price')
         
        quantity_available=forms.IntegerField(label='Enter Quantity')
        file      = forms.FileField() # for creating file input  
 
      


        
        

class HumaddItemsForm(forms.Form):
        foodTypeOptions=(
        ( None, 'Select'),
         ("Veg","Veg"),
         ("Non Veg","Non Veg"),
        )
        location=(
         ( None, 'Select'),
         ("Hyderabad","Hyderabad"),
         ("Bangalore","Bangalore"),
         ("Mumbai","Mumbai"),
         ("Delhi","Delhi"),
         ("Kolkota","Kolkota"),
        )

        foodType = forms.CharField(max_length=25,  widget=forms.Select(choices=foodTypeOptions))
        location = forms.CharField(max_length=25,  widget=forms.Select(choices=location))
        name = forms.CharField(max_length=255)
 
        # price=forms.DecimalField(label='Enter Price')
         
        quantity_available=forms.IntegerField(label='Enter Quantity')
        file      = forms.FileField() # for creating file input  
 
      
     

         
 
class itemsViewForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(itemsViewForm,self).__init__(*args, **kwargs)
        
         


class HumitemsViewForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(HumitemsViewForm,self).__init__(*args, **kwargs)
         
 


class NeedFulForm(forms.Form):
     
        foodTypeOptions=(
        ( None, 'Select'),
         ("Vegetarian","Vegetarian"),
         ("Non Vegetarian","Non Vegetarian"),
        )
        foodType = forms.CharField(max_length=25,  widget=forms.Select(choices=foodTypeOptions))

         
        file      = forms.FileField() # for creating file input  

        phone=forms.CharField(max_length=10)
        need=forms.CharField(max_length=255)
        location = forms.CharField(max_length=255)
       



  
         
        


class ServeNeedFulForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(ServeNeedFulForm,self).__init__(*args, **kwargs)
         
class OrderForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)
        foodTypeOptions=(
        ( None, 'Select'),
         ("select me","Select me"),
         
        )        
        need = forms.CharField(max_length=25,  widget=forms.Select(choices=foodTypeOptions))
 
        self.fields['need'] = need

       
class SellerOrderViewForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(SellerOrderViewForm,self).__init__(*args, **kwargs)
        
      
class HumOrderForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(HumOrderForm,self).__init__(*args, **kwargs)
        foodTypeOptions=(
        ( None, 'Select'),
         ("select me","Select me"),
         
        )        
        need = forms.CharField(max_length=25,  widget=forms.Select(choices=foodTypeOptions))
 
        self.fields['need'] = need

       
class HumSellerOrderViewForm(forms.Form):
    def __init__(self, *args,**kwargs):
        super(HumSellerOrderViewForm,self).__init__(*args, **kwargs)
        
from django import forms  
class trialForm(forms.Form):  
    
    
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input  
 
        

 



         

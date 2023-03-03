from django.urls import path
from students.views import addItems
from . import views

app_name= 'students'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('business/', views.business, name='business'),
    path('businessBuyer/', views.businessBuyer, name='businessBuyer'),
    path('businessSeller/', views.businessSeller, name='businessSeller'),
    path('humanity/', views.humanity, name='humanity'),
    path('humanityBuyer/', views.humanityBuyer, name='humanityBuyer'),
    path('humanitySeller/', views.humanitySeller, name='humanitySeller'),
    path('addItems/',  views.addItems, name='addItems'),
    path('itemsView/', views.itemsView, name='itemsView'),
    path('HumaddItems/', views.HumaddItems, name='HumaddItems'),
    path('HumitemsView/', views.HumitemsView, name='HumitemsView'),
    



    
    
]
from django.urls import path
from students.views import *
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
    path('TrackitemsView/', views.TrackitemsView, name='TrackitemsView'),

    path('HumaddItems/', views.HumaddItems, name='HumaddItems'),
    path('HumitemsView/', views.HumitemsView, name='HumitemsView'),
    path('TrackHumitemsView/', views.TrackHumitemsView, name='TrackHumitemsView'),
    path('NeedFul/', views.NeedFul, name='NeedFul'),
    path('ServeNeedFul/', views.ServeNeedFul, name='ServeNeedFul'),
    # path('Order/', views.Order, name='Order'),
    path('OrderView/<int:pk>', views.OrderView, name='OrderView'),
    path('SellerOrderView/', views.SellerOrderView, name='SellerOrderView'),
    path('ChangeOrderStatus/<int:pk>', views.ChangeOrderStatus, name='ChangeOrderStatus'),
    
    path('CustomerOrdersView/', views.CustomerOrdersView, name='CustomerOrdersView'),
    path('ChangeOrderStatustoDelivered/<int:pk>', views.ChangeOrderStatustoDelivered, name='ChangeOrderStatustoDelivered'),







    



    
    
]
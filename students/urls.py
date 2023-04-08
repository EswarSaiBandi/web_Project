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
   

    path('HumOrderView/<int:pk>', views.HumOrderView, name='HumOrderView'),
    path('HumSellerOrderView/', views.HumSellerOrderView, name='HumSellerOrderView'),
    path('HumChangeOrderStatus/<int:pk>', views.HumChangeOrderStatus, name='HumChangeOrderStatus'),
    
    path('HumCustomerOrdersView/', views.HumCustomerOrdersView, name='HumCustomerOrdersView'),
    path('HumChangeOrderStatustoDelivered/<int:pk>', views.HumChangeOrderStatustoDelivered, name='HumChangeOrderStatustoDelivered'),
    path('TotalOrdersView/', views.TotalOrdersView, name='TotalOrdersView'),
    path('TotalOrdersViewProcessing/', views.TotalOrdersViewProcessing, name='TotalOrdersViewProcessing'),
    path('TotalOrdersViewPrepared/', views.TotalOrdersViewPrepared, name='TotalOrdersViewPrepared'),
    path('TotalOrdersViewDelivered/', views.TotalOrdersViewDelivered, name='TotalOrdersViewDelivered'),
    path('TotalOrdersViewCancelled/', views.TotalOrdersViewCancelled, name='TotalOrdersViewCancelled'),
    path('TotalOrdersViewToBeDelivered/', views.TotalOrdersViewToBeDelivered, name='TotalOrdersViewToBeDelivered'),


    path('Filtering/', views.Filtering, name='Filtering'),
    
    path('HumCancelOrder/<int:pk>', views.HumCancelOrder, name='HumCancelOrder'),
    path('CancelOrder/<int:pk>', views.CancelOrder, name='CancelOrder'),
    path('Review/<int:pk>', views.Review, name='Review'),
    path('HumReview/<int:pk>', views.HumReview, name='HumReview'),
    path('Rating/<int:pk>', views.Rating, name='Rating'),
    path('HumRating/<int:pk>', views.HumRating, name='HumRating'),
    path('trial/', views.trial, name='trial'),    
]



from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
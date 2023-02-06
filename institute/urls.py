from django.urls import path

from . import views

app_name= 'institute'

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery',views.gallery, name='gallery'),
    path('block-gallery/',views.hostels,name='hostels'),
    path('contact/',views.contact,name='contact'),
    path('developer-team/',views.developers, name='developers'),
    path('Home',views.Home,name='Home'),
    path('Profile',views.Profile,name='Profile'),
    path('KnowledgeCentre',views.KnowledgeCentre,name='KnowledgeCentre'),
    path('Sbilifeinfo',views.Sbilifeinfo,name='Sbilifeinfo'),
    path('ResourceCentre',views.ResourceCentre,name='ResourceCentre'),
    path('NRIinfo',views.NRIinfo,name='NRIinfo'),
    path('Lifeinsurance',views.Lifeinsurance,name='Lifeinsurance'),
    path('Healthinsurance',views.Healthinsurance,name='Healthinsurance'),
    path('Generalinsurance',views.Generalinsurance,name='Generalinsurance'),
    path('Nri',views.Nri,name='Nri'),
    path('Corporateplanning',views.Corporateplanning,name='Corporateplanning'),
    path('Homeloans',views.Homeloans,name='Homeloans'),
    path('Mutualfund',views.Mutualfund,name='Mutualfund'),
    path('Medclaim',views.Medclaim,name='Medclaim'),
    path('Fixeddeposit',views.Fixeddeposit,name='Fixeddeposit'),


    

    

]
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from . import views

app_name= 'officials'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
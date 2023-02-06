from django.shortcuts import render
from institute.models import Block

# Create your views here.
def index(request):
    return render(request, 'institute/index.html')

def gallery(request):
    return render(request, 'institute/grid-gallery.html')


def hostels(request):
    blocks = Block.objects.all()
    return render (request,'institute/hostels.html',{'blocks': blocks})

def contact(request):
    boys_blocks = Block.objects.filter(gender='Male')
    girls_blocks = Block.objects.filter(gender='Female') 
    return render (request,'institute/contact.html', {'boys_blocks':boys_blocks, 'girls_blocks':girls_blocks})

def developers(request):
    return render(request,'institute/developers.html')

def Home(request):
    return render(request,'institute/Home.html')
def Profile(request):
    return render(request,'institute/Profile.html')
def KnowledgeCentre(request):
    return render(request,'institute/KnowledgeCentre.html')
def Sbilifeinfo(request):
    return render(request,'institute/Sbilifeinfo.html')
def ResourceCentre(request):
    return render(request,'institute/ResourceCentre.html')
def NRIinfo(request):
    return render(request,'institute/NRIinfo.html')
def Lifeinsurance(request):
    return render(request,'institute/Lifeinsurance.html')
def Healthinsurance(request):
    return render(request,'institute/Healthinsurance.html')
def Generalinsurance(request):
    return render(request,'institute/Generalinsurance.html')
def Nri(request):
    return render(request,'institute/Nri.html')
def Corporateplanning(request):
    return render(request,'institute/Corporateplanning.html')
def Homeloans(request):
    return render(request,'institute/Homeloans.html')
def Mutualfund(request):
    return render(request,'institute/Mutualfund.html')
def Medclaim(request):
    return render(request,'institute/Medclaim.html')
def Fixeddeposit(request):
    return render(request,'institute/Fixeddeposit.html')
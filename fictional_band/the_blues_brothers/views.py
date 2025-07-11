from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm


# Create your views here.
def home(request):
    #template = loader.get_template('home.html')
    return render(request, 'home.html')


def members(request):
    #template = loader.get_template('members.html')
    return render(request, 'members.html')


'''def contact(request):
    #template = loader.get_template('contact.html')
    return render(request, 'contact.html')'''


def login(request):
    #template = loader.get_template('login.html')
    return render(request, 'login.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
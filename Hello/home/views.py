from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("this is a home page")
    context = {
        'variable': 'this is vavariable'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    
def services(request):
    return render(request, 'services.html')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        date = datetime.today()

        contact = Contact(
            name = name,
            email = email,
            desc = desc,
            date = date
        )
        contact.save()

        messages.success(request, "Saved Successfully")
    return render(request, 'contact.html')
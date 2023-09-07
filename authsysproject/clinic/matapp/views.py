from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_subject = request.POST['message_subject']
        umessage = request.POST['umessage']

        send_mail(
            #message_name, #user name
            message_subject, #message subject
            umessage, #messages
            message_email, #from email
            ['diananyawira.dn15@gmail.com'], #to email
        )

        return render(request, 'contact.html', {'message_name':message_name})
    
    else: 
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog_single(request):
    return render(request, 'blog_single.html', {})

def antenatal(request):
    return render(request, 'antenatal.html', {})


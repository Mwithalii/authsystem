from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import UserInfo
from .forms import UserInfoForm
import africastalking
from .chatgpt import chat_with_gpt

africastalking.initialize(
    username='Mwithalii_1',
    api_key = "1126f44923e4533cf9f17feadff831b3f3f5cbb769407f8d3dfd980267260cee"
)

sms = africastalking.SMS


def home(request):
    return render(request, 'users/home.html')

def homepage(request):
    return render(request, 'users/homepage.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            phone_number = "+254742086215"
            message = "You have Successfully Singed Up to MaternaCare. Welcome!"
            response = sms.send(message, [phone_number])
            print(response)
            return redirect('home')
            
    else:
        form = UserRegisterForm()
    

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    if request.method == 'POST':
        institution = request.POST.get('institution')
        mfl = request.POST.get('mfl')
        anc = request.POST.get('anc')
        pnc = request.POST.get('pnc')
        client = request.POST.get('client')
        age = request.POST.get('age')
        gravida = request.POST.get('gravida')
        parity = request.POST.get('parity')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        lmp = request.POST.get('lmp')
        edd = request.POST.get('edd')
        marital = request.POST.get('marital')
        occupation = request.POST.get('occupation')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        education = request.POST.get('education')
        kin = request.POST.get('kin')
        relationship = request.POST.get('relationship')
        kin_phone = request.POST.get('kin_phone')


        context = {
            'institution': institution,
            'mfl': mfl,
            'anc': anc,
            'pnc': pnc,
            'client': client,
            'age': age,
            'gravida': gravida,
            'parity': parity,
            'height': height,
            'weight': weight,
            'lmp': lmp,
            'edd': edd,
            'marital': marital,
            'occupation': occupation,
            'address': address,
            'phone': phone,
            'education': education,
            'weight': weight,
            'kin': kin,
            'relationship': relationship,
            'kin_phone': kin_phone,

        }

        return render(request, 'users/profile.html', context)

    return render(request, 'users/profile.html')



def about(request):
    return render(request, 'users/about.html')

def antenatal(request):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        diabetes = request.POST.get('diabetes')
        hypertension = request.POST.get('hypertension')
        transfusion = request.POST.get('delivery_mode')
        tb = request.POST.get('tb')
        add_notes = request.POST.get('add_notes')
        nvisit = request.POST.get('nvisit')
        tt1day = request.POST.get('tt1day')
        tt1next = request.POST.get('tt1next')
        tt2day = request.POST.get('tt2day')
        tt2next = request.POST.get('tt2next')
        malday = request.POST.get('malday')
        malnext = request.POST.get('malnext')

        context = {
            'operation': operation,
            'diabetes': diabetes,
            'hypertension': hypertension,
            'transfusion': transfusion,
            'malnext': malnext,
            'malday': malday,
            'tt2next': tt2next,
            'tt2day': tt2day,
            'tt1next': tt1next,
            'tt1day': tt1day,
            'nvisit': nvisit,
            'add_notes': add_notes,
            'tb': tb,
        }

        return render(request, 'users/antenatal.html', context)

    return render(request, 'users/antenatal.html')

def blog_single(request):
    return render(request, 'users/blog_single.html')

def blog(request):
    return render(request, 'users/blog.html')

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


        return render(request, 'users/contact.html', {'message_name':message_name})
    
    else: 
        return render(request, 'users/contact.html', {})
    
    

def delivery(request):
    if request.method == 'POST':
        duration = request.POST.get('duration')
        hiv = request.POST.get('hiv')
        hiv_type = request.POST.get('hiv_type')
        delivery_mode = request.POST.get('delivery_mode')
        date = request.POST.get('date')
        blood = request.POST.get('blood')
        pre_eclampsia = request.POST.get('pre_eclampsia')
        eclampsia = request.POST.get('eclampsia')
        obstructed_labour = request.POST.get('obstructed_labour')
        condition = request.POST.get('condition')
        rescuscitation = request.POST.get('rescuscitation')
        min_1 = request.POST.get('min_1')
        min_5 = request.POST.get('min_5')
        min_10 = request.POST.get('min_10')
        oxy = request.POST.get('oxy')
        vit = request.POST.get('vit')
        teo = request.POST.get('teo')
        weight = request.POST.get('weight')
        length = request.POST.get('length')
        head = request.POST.get('head')
        place = request.POST.get('place')
        other = request.POST.get('other')
        conducted_by = request.POST.get('conducted_by')
        other2 = request.POST.get('other2')

        context = {
            'duration': duration,
            'hiv': hiv,
            'hiv_type': hiv_type,
            'delivery_mode': delivery_mode,
            'date': date,
            'blood': blood,
            'pre_eclampsia': pre_eclampsia,
            'eclampsia': eclampsia,
            'obstructed_labour': obstructed_labour,
            'condition': condition,
            'rescuscitation': rescuscitation,
            'min_1': min_1,
            'min_5': min_5,
            'min_10': min_10,
            'oxy': oxy,
            'vit': vit,
            'teo': teo,
            'weight': weight,
            'length': length,
            'head': head,
            'place': place,
            'other': other,
            'conducted_by': conducted_by,
            'other2': other2,
        }

        return render(request, 'users/delivery.html', context)

    return render(request, 'users/delivery.html')

def doctors(request):
    return render(request, 'users/doctors.html')

def postnatal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        phone = request.POST.get('phone')
        bcg_birth = request.POST.get('bcg_birth')
        bcg_next = request.POST.get('bcg_next')
        polio_birth = request.POST.get('polio_birth')
        ipv6 = request.POST.get('ipv6')
        dept6 = request.POST.get('dept6')
        dept_next = request.POST.get('dept_next')
        pne6 = request.POST.get('pne6')
        pne6_next = request.POST.get('pne6_next')

        context = {
            'name': name,
            'date': date,
            'father': father,
            'mother': mother,
            'phone': phone,
            'bcg_birth': bcg_birth,
            'bcg_next': bcg_next,
            'polio_birth': polio_birth,
            'ipv6': ipv6,
            'dept6': dept6,
            'dept_next': dept_next,
            'pne6': pne6,
            'pne6_next': pne6_next,
        }

        return render(request, 'users/postnatal.html', context)

    return render(request, 'users/postnatal.html')

def services(request):
    return render(request, 'users/services.html')

def chat_view(request):
       if request.method == 'POST':
           user_input = request.POST.get('user_input')
           response = chat_with_gpt(user_input)
           # Process the response as needed
           return render(request, 'users/chat_view.html', {'response': response})
       else:
           return render(request, 'users/chat_view.html')

def form(request):
    if request.method == 'POST':
        phone_number = "+254794824427"
        message = "Your appointment has been booked successfully. We look forward to seeing you!"
        response = sms.send(message, [phone_number])
        print(response)
        return redirect('homepage')

    return render(request, 'users/homepage.html')




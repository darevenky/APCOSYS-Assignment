from django.shortcuts import render
from app.models import *
from app.forms import *
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def home(request):
    if request.session.get('username'):
        username=request.session.get('username')

        d={'username':username}
        return render(request,'app/home.html',d)
    return render(request, 'app/home.html')


def Registration(request):
    user = UserForm()
    details = DetailsForm()

    d = {'uo': user, 'do': details}

    if request.method == 'POST':
        USF = UserForm(request.POST)
        DFO = DetailsForm(request.POST)

        if USF.is_valid() and DFO.is_valid():
            USUO = USF.save(commit=False)
            password = USF.cleaned_data['password']
            USUO.set_password(password)
            USUO.save()

            USDO = DFO.save(commit=False)
            USDO.username = USUO
            USDO.save()

            return HttpResponseRedirect(reverse('user_login'))
        else:
            return HttpResponse('something went wrong!')

    return render(request, 'app/Registration.html', d)

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        name = User.objects.filter(username=username)
        if name :
            for i in name:
                check = Details.objects.filter(username=i.id)
                print(check)
                for i in check:
                    if i.is_access == 'no':
                        return HttpResponse('access denied,contact admin')
                    else:
                        pass
        

        AUO=authenticate(username=username, password=password)

        if AUO:
            login(request,AUO)
            request.session['username'] = username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('data not found')
        
    return render(request, 'app/user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))





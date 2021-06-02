from users.models import Account
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from users.forms import AccountUpdateForm, RegistrationForm, AccountAuthenticationForm



def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("Ya iniciaste sesión como " + str(user.email))
    
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            dni = form.cleaned_data.get('dni')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password= raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination: #if destination != None
                return redirect(destination)
            return redirect("Home")
        else:
            context['registration_form'] = form
        
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)

def profile_view(request):
    return render(request, "users/profile.html")

def editprofile_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("Login")
    try:
        account = Account.objects.get(pk=request.user.id)
    except Account.DoesNotExist:
        return HttpResponse("Hubo un error")
    if account.pk != request.user.pk:
        return HttpResponse("No podes editar el perfil de otro")


    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        # print(form.errors)
        if form.is_valid():   
            form.save()
            return redirect("Profile")
        else:
            form = AccountUpdateForm(request.POST, instance=request.user,
                initial={
                    
                    "email": account.email,
                    "first_name": account.first_name,
                    "last_name": account.last_name,
                    "dni": account.dni,
                    "date_of_birth": account.date_of_birth
                }
            )
            context['form'] = form
    else:
        
        form = AccountUpdateForm(
                initial={
                    
                    "email": account.email,
                    "first_name": account.first_name,
                    "last_name": account.last_name,
                    "dni": account.dni,
                    "date_of_birth": account.date_of_birth
                }
            )
        context['form'] = form
    
    return render(request, "users/edit_profile.html", context)

def misviajes_view(request):
    return render(request, "users/misviajes.html")

def logout_view(request):
    logout(request)
    return redirect("Home")

def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated: 
        return redirect("Home")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            # remember_me = request.POST['remember_me']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                # if not remember_me:
                #     request.session.set_expiry(0)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("Home")
        else:
            context['login_form'] = form
    return render(request, "users/login.html", context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect

from users.models import Account, Tarjeta
from Combi19App.models import Pasaje, Viaje
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from datetime import datetime
import pytz
from django.db.models import F
from django.utils import timezone
from users.forms import AccountUpdateForm, AddCardForm, RegistrationForm, AccountAuthenticationForm, EditCardForm



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
    viajes_pendientes = Viaje.objects.filter(pasajeros=request.user).filter(estado=False)
    viajes_finalizados = Viaje.objects.filter(pasajeros=request.user).filter(estado=True)
    context = {"finalizados": viajes_finalizados, "pendientes":viajes_pendientes}
    return render(request, "users/misviajes.html", context)

def mistarjetas_view(request):
    tarjetas = Tarjeta.objects.filter(usuario_id=request.user.id)
    return render(request, "users/mistarjetas.html", {"tarjetas": tarjetas})
    
def tarjeta_view(request, *args, **kwargs):
    # try:
    #     account = Account.objects.get(pk=request.user.id)
    # except Account.DoesNotExist:
    #     return HttpResponse("Hubo un error")
    context = {}
    
    if request.POST:
        form = AddCardForm(request.POST, instance=request.user)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("Tarjetas")
        else:
            context['form'] = form
        
    else:
        form = AddCardForm()
        context['form'] = form
    return render(request, "users/nueva_tarjeta.html", context)

def edit_tarjeta_view(request, *args, **kwargs):
    tarjeta_id = kwargs.get("tarjeta_id")
    try:
        tarjeta = Tarjeta.objects.get(pk=tarjeta_id)
    except Tarjeta.DoesNotExist:
        return HttpResponse("Hubo un error")

    context = {}
    if request.POST:
        form = EditCardForm(request.POST, usuario=request.user, instance=tarjeta, )
        print(form)
        if form.is_valid():   
            form.save(user=request.user)
            return redirect("Tarjetas")
        else:
            form = EditCardForm(request.POST, usuario=request.user,  instance=tarjeta,
                initial={
                    "nro": tarjeta.nro,
                    "nombre_titular": tarjeta.nombre_titular,
                    "cvv": tarjeta.cvv,
                    "fecha_vencimiento": tarjeta.fecha_vencimiento,
                    "usuario" : tarjeta.usuario
                }
            )
            context['form'] = form
    else:
        form = EditCardForm( usuario=request.user,
                initial={
                    "nro": tarjeta.nro,
                    "nombre_titular": tarjeta.nombre_titular,
                    "cvv": tarjeta.cvv,
                    "fecha_vencimiento": tarjeta.fecha_vencimiento,
                    "usuario" : tarjeta.usuario
                }
            )
        context['form'] = form
    
    return render(request, "users/nueva_tarjeta.html", context)

def delete_tarjeta_view(request, *args, **kwargs):
    tarjeta_id = kwargs.get("tarjeta_id")

    try:
        tarjeta = Tarjeta.objects.get(pk=tarjeta_id)
    except Tarjeta.DoesNotExist:
        return HttpResponse("Hubo un error")
    context = {"tarjeta":tarjeta}


    if request.POST:
        tarjeta.delete()
        return redirect("Tarjetas")

    return render(request, "users/eliminar_tarjeta.html", context)

def delete_viaje(request, *args, **kwargs):
    viaje_id = kwargs.get("v_id")
    try:
        viaje = Viaje.objects.get(pk=viaje_id)
    except Viaje.DoesNotExist:
        return HttpResponse("Hubo un error")

    if (((viaje.fecha)-timezone.now()).days > 2):
        context = {"mensaje": "Se te reembolsará el 100% del valor del pasaje"}
    else:
        context = {"mensaje": "Estas cancelando dentro de las 48hs previas al viaje, se te reembolsará solo el 50% de tu pago."}
    
    if request.POST:
        pasaje = Pasaje.objects.filter(viaje=viaje_id).filter(usuario=request.user)
        pasaje.delete()
        viaje.asientos_ocupados= F('asientos_ocupados') - 1
        viaje.pasajeros.remove(request.user)
        viaje.save()
        viaje.refresh_from_db()
        return redirect("Viajes")

    return render(request, "users/eliminar_viaje.html", context)

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

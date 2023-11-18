from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as login2
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from Cuentas.forms import FormuCreacion, EdicionPerfil
from Cuentas.models import DatosExtra
# Create your views here.
def login(request):
    if request.method == 'POST':
        formulario= AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            login2(request, user)
            
            datos_extra= DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('inicio')
        else:
            return render(request, 'Cuentas/login.html', {'formulario': formulario})                
    formulario= AuthenticationForm()
    return render(request, 'Cuentas/login.html', {'formulario': formulario})

def registro(request):
    
    
    formulario= FormuCreacion()
    
    if request.method == 'POST':
        formulario= FormuCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
    
    return render(request, 'Cuentas/registro.html', {'formulario_registro': formulario})

def editar_perfil(request):
  
    datos_extra = request.user.datosextra
    
    formulario = EdicionPerfil(instance=request.user, initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar})
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nueva_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nueva_avatar:
                datos_extra.avatar = nueva_avatar
            
            datos_extra.save()
            formulario.save()
            
            return redirect('editar_perfil')
    
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('logout')
    
def ver_perfil(request):
    
    datos_extra = request.user.datosextra
    biografia = datos_extra.biografia
    avatar = datos_extra.avatar
    return render(request, 'cuentas/verperfil.html', {'biografia': biografia, 'avatar': avatar})



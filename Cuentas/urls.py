from django.urls import path
from Cuentas.views import login, registro, editar_perfil, CambiarPassword, ver_perfil
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', login, name = 'login'),
    path('registro/', registro, name = 'Registrarse'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('perfil/editar/', editar_perfil, name= 'editar_perfil'),
    path('perfil/ver/', ver_perfil, name= 'ver_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='cambiar_password')
    ]

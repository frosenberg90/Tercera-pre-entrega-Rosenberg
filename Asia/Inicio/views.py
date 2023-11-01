from django.shortcuts import render, redirect
""" from django.http import HttpResponse
from django.template import loader """
from Inicio.models import Productos, Ventas, Clientes
from Inicio.forms import HacerPedidoFormulario
# Create your views here.
def inicio (request):
    """     template = loader.get_template('inicio.html')
    template_renderizado = template.render({})
    
    return HttpResponse(template_renderizado) """
    return render(request,'Inicio/inicio.html',{})

def produ(request):
    tipo_a_buscar= request.GET.get('tipo')
    
    if tipo_a_buscar:
        
        Listado_pedidos = Productos.objects.filter(tipo=tipo_a_buscar)
    else:
        Listado_pedidos = Productos.objects.all()
    
    return render(request,'Inicio/Productos.html',{'Listado_pedidos': Listado_pedidos})

""" def hacer_pedido(request):
    
    print(request.GET)
    print('===========')
    print(request.POST)
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        descrip = request.POST.get('Descripcion')
        cantidad = request.POST.get('Cantidad')
        cost = request.POST.get('costo')
    
    
        producto = Productos(tipo=tipo, descripcion=descrip, cantidad=cantidad, costo=cost)
        producto.save()
    
    
    return render (request, 'inicio/pedidos.html', {})
 """
def hacer_pedido(request):
    
    
    if request.method == 'POST':
        formulario = HacerPedidoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia= formulario.cleaned_data
            tipo = info_limpia.get('tipo')
            descrip = info_limpia.get('descripcion')
            cantidad = info_limpia.get('cantidad')
            cost = info_limpia.get('costo')
            
            producto = Productos(tipo=tipo, descripcion=descrip, cantidad=cantidad, costo=cost)
            producto.save()
            
            return redirect('productos')
            
    formulario = HacerPedidoFormulario()
    return render (request, 'inicio/pedidos.html', {'formulario':formulario})


def Ingresar (request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        genero = request.POST.get('genero')
    
    
        usuario = Clientes(Nombre=nombre, Apellido=apellido, Edad=edad, genero=genero)
        usuario.save()
    
    
    return render (request, 'inicio/clientes.html', {})
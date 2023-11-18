from django.shortcuts import render, redirect
""" from django.http import HttpResponse
from django.template import loader """
from Inicio.models import Productos, Promos, Clientes
from Inicio.forms import HacerPedidoFormulario, ActualizarFormulario
from django.contrib.auth.decorators import login_required
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
    
    return render(request,'inicio/Productos.html',{'Listado_pedidos': Listado_pedidos})


@login_required
def hacer_pedido(request):
    
    #vamos a hacer el CRUD (CREATE, READ, UPDATE AND DELETE)
    #En la clase del 30/10 vamos a ver estos temas arrancando por el DELETE
    if request.method == 'POST':
        formulario = HacerPedidoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia= formulario.cleaned_data
            tipo = info_limpia.get('tipo')
            descrip = info_limpia.get('descripcion')
            cantidad = info_limpia.get('cantidad')
            cost = info_limpia.get('costo')
            fecha = info_limpia.get('fecha')
            producto = Productos(tipo=tipo, descripcion=descrip, cantidad=cantidad, costo=cost, fecha=fecha)
            producto.save()
            
            return redirect('productos')
            
    formulario = HacerPedidoFormulario()
    return render (request, 'inicio/pedidos.html', {'formulario':formulario})

@login_required
def eliminar(request, Productos_id): #si quiero modificar un nombre, apreo F2 y me modifica en todo el proyecto lo que esta relacionado a este nombre#
    Producto_a_eliminar=Productos.objects.get(id=Productos_id)
    Producto_a_eliminar.delete()
    
    return redirect("productos")

@login_required    
def actualizar(request, Productos_id):
    
    pedido_a_modificar=Productos.objects.get(id=Productos_id)
    
    if request.method == 'POST':
        formulario = ActualizarFormulario(request.POST)
        if formulario.is_valid():
            info_nueva= formulario.cleaned_data
            pedido_a_modificar.tipo = info_nueva.get('tipo')
            pedido_a_modificar.descripcion = info_nueva.get('descripcion')
            pedido_a_modificar.cantidad = info_nueva.get('cantidad')
            pedido_a_modificar.costo = info_nueva.get('costo')
            pedido_a_modificar.save()
            return redirect('productos')
    formulario = ActualizarFormulario(initial={'tipo': pedido_a_modificar.tipo,'descripcion': pedido_a_modificar.descripcion,'cantidad': pedido_a_modificar.cantidad,'costo': pedido_a_modificar.costo}) 
    return render (request, 'inicio/actualizar.html', {'formulario':formulario})    

def detalle(request, Productos_id):
    Producto_a_mostrar=Productos.objects.get(id=Productos_id)
    
    return render (request, 'inicio/detalle.html', {'Productos':Producto_a_mostrar})    

    
def ingreso(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        genero = request.POST.get('genero')
    
    
        usuario = Clientes(Nombre=nombre, Apellido=apellido, Edad=edad, genero=genero)
        usuario.save()
        return redirect('pedidos')
    
    return render (request, 'inicio/clientes.html', {})
def promo(request):
    
    if request.method == 'POST':
        promo = request.POST.get('promo')
        cantidad = request.POST.get('cantidad')
            
    
        Desc = Promos(Promo=promo,Cantidad=cantidad)
        Desc.save()
        return redirect('productos')
    
    return render (request, 'inicio/promo.html', {})

def acerca (request):
    """     template = loader.get_template('inicio.html')
    template_renderizado = template.render({})
    
    return HttpResponse(template_renderizado) """
    return render(request,'inicio/acerca.html',{})
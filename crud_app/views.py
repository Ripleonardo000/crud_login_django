from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




@login_required(login_url='/login/')
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista.html', {'productos': productos})


@login_required(login_url='/login/')
def crear_producto(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        return redirect('lista_productos')
    return render(request, 'crear.html')

@login_required(login_url='/login/')
def editar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.save()
        return redirect('lista_productos')
    return render(request, 'editar.html', {'producto': producto})
@login_required(login_url='/login/')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')


#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_productos')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

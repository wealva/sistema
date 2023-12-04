from django.shortcuts import render
from django.http import HttpResponse
from . forms import ProductoForm

def inicial(request):
    return HttpResponse("¡Hola, esta es la vista inicial!")



# def inicial(request):
#     # Your view logic here
#     return render(request, 'inicial.html')
#     # return render(request, 'inicial_template.html')

def crear_producto(request):
    if request.method == "POST":
        producto_form = ProductoForm(request.POST or None)
        if producto_form.is_valid():
            producto_form.save()
        else:
           return(request, 'Formulario invalido. Por favor, corrige los errores.')
    else:
        producto_form = ProductoForm()

    return render(request, "crear_pro.html", {"form": producto_form})

def modificar_producto(request):
    if request.method == "POST":
        producto_form = ProductoForm(request.POST or None)
        if producto_form.is_valid():
            producto_form.save()
        else:
           return(request, 'Formulario invalido. Por favor, corrige los errores.')
        
    else:
        producto_form = ProductoForm()

    return render(request, "crear_pro.html", {"form": producto_form})

def eliminar_producto(request):
    if request.method == "POST":
        producto_form = ProductoForm(request.POST or None)
        if producto_form.is_valid():
            producto_form.save()
        else:
           return(request, 'Formulario invalido. Por favor, corrige los errores.')
        
    else:
        producto_form = ProductoForm()

    return render(request, "crear_pro.html", {"form": producto_form})

def consultar_producto(request):
    if request.method == "POST":
        producto_form = ProductoForm(request.POST or None)
        if producto_form.is_valid():
            producto_form.save()
        else:
           return(request, 'Formulario invalido. Por favor, corrige los errores.')
        
    else:
        producto_form = ProductoForm()

    return render(request, "crear_pro.html", {"form": producto_form})
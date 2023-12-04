from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)



class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Inventario(models.Model):
    producto = models. ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Venta(models.Model):
    producto = models. ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models. ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_venta = models.DateField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    empleado = models. ForeignKey(Empleado, on_delete=models.CASCADE)
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_compra = models.DateField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Factura(models.Model):
    venta = models. ForeignKey(Venta, on_delete=models.CASCADE, null=True)
    compra = models. ForeignKey(Compra, on_delete=models.CASCADE, null=True)
    fecha_emision = models.DateField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Pago(models.Model):
    factura = models. ForeignKey(Factura, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Devolucion(models.Model):
    venta = models. ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_devolucion = models.DateField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Promocion(models.Model):
    nombre = models.CharField(max_length=255)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class Notificacion(models.Model):
    mensaje = models.TextField()
    usuario = models. ForeignKey(Usuario, on_delete=models.CASCADE)
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class HistorialVentas(models.Model):
    venta = models. ForeignKey(Venta, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255)
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

class ComentarioProducto(models.Model):
    producto = models. ForeignKey(Producto, on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    usuario_creacion= models.CharField(max_length=20)
    usuario_modificacion= models.CharField(max_length=20)
    fecha_creacion=models.DateTimeField (auto_now_add= True)
    fecha_modificacion=models.DateTimeField (auto_now= True)
    estado = models.IntegerField(default=1)

#Dar permisos varios: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#Activar el entorno virtual: Ir a la carpeta SCRIPT y ejecutar el file .\activate
#python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate 
# django-admin startproject sisferre .
# django-admin startapp inventario1
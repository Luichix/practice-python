from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    email= models.EmailField()
    telefono= models.CharField(max_length=7)

class Articulos(models.Model):
    nombre= models.CharField(max_length=30)
    seccion= models.CharField(max_length=20)
    precio= models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero= models.IntegerField()
    fecha= models.DateField()
    entregado= models.BooleanField()


# CRUD: Create, Read, Update, Delete

# ~  python manage.py shell
# >>> from gestionPedidos.models import Articulos

# Create
# >>> art=Articulos(nombre='mesa', seccion='decoracion', precio=90)
# >>> art.save()
# >>> art2=Articulos(nombre='camisa', seccion='confeccion', precio=75)
# >>> art2.save()
# >>> art3=Articulos.objects.create(nombre='taladro', seccion='ferreteria', precio=65)

# Read
# >>> Lista=Articulos.objects.all()
# >>> Lista
# <QuerySet [<Articulos: Articulos object (1)>, <Articulos: Articulos object (3)>]>
# >>> Lista.query.__str__()
# 'SELECT "gestionPedidos_articulos"."id", "gestionPedidos_articulos"."nombre", "gestionPedidos_articulos"."seccion", "gestionPedidos_articulos"."precio" FROM "gestionPedidos_articulos"

# Update
# >>> art.precio=95
# >>> art.save()

# Delete
# >>> art4=Articulos.objects.get(id=2) 
# >>> art4.delete()  
# (1, {'gestionPedidos.Articulos': 1})

# >>> Articulos.objects.filter(seccion='decoracion')
# <QuerySet [<Articulos: Articulos object (1)>]>

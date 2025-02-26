from random import choices
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

'''Modelos de las tablas de la app'''
class Book(models.Model): # Modelo de la tabla Book
    id_book = models.AutoField(primary_key=True) # PK de la tabla Book
    title = models.CharField(max_length=100) # Atributo title de la tabla Book
    author = models.CharField(max_length=100) # Atributo author de la tabla Book
    description = models.TextField() # Atributo description de la tabla Book

    def __str__(self): # Método que retorna el título del libro
        return self.title # Retorna el título del libro

class Editorials(models.Model): # Modelo de la tabla Editorials
    id_editorial = models.AutoField(primary_key=True) # PK de la tabla Editorials
    editorial_name = models.CharField(max_length=100) # Atributo name de la tabla Editorials
    email = models.EmailField() # Atributo email de la tabla Editorials
    phone = models.CharField(max_length=100) # Atributo phone de la tabla Editorials

    def __str__(self): # Método que retorna el nombre de la editorial
        return self.editorial_name # Retorna el nombre de la editorial

class Copies(models.Model): # Modelo de la tabla Copies
    id_copy = models.AutoField(primary_key=True) # PK de la tabla Copies
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE) # FK de la tabla Book
    id_editorial = models.ForeignKey(Editorials, on_delete=models.CASCADE) # FK de la tabla Editorial
    # Permite que ingreses la fecha manualmente
    published_date = models.DateTimeField()
    # Permite seleccionar el estado de la copia
    state = models.CharField(
        max_length=50,
        choices=[('Disponible', 'Disponible'), ('Prestado', 'Prestado')])
    def __str__(self): # Método que retorna el título del libro 
        return self.id_book.title # Retorna el título del libro de la tabla Copies
    

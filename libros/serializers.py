from rest_framework import serializers
from .models import Book, Copies, Editorials
from django.contrib.auth import get_user_model, authenticate # Importa el modelo usuario y la funcion de autenticacion

    
'''Serializador para la gestion de la biblioteca'''
class BookSerializer(serializers.ModelSerializer): # Clase BookSerializer que hereda de ModelSerializer
    
    class Meta: # Clase Meta que contiene los campos de la tabla Book
        model = Book # Modelo Book 
        fields = '__all__' # Campos de la tabla Book
        read_only_fields = ['id_book'] # Campos de solo lectura de la tabla Book

class EditorialsSerializer(serializers.ModelSerializer): # Clase BookSerializer que hereda de ModelSerializer
    
    class Meta: # Clase Meta que contiene los campos de la tabla Editorials
        model = Editorials # Modelo Editorials
        fields = '__all__' # Campos de la tabla Editorials
        read_only_fields = ['id_editorial'] # Campos de solo lectura de la tabla Editorials
# Compare this snippet from libros/serializers.py:  

class CopiesSerializer(serializers.ModelSerializer): # Clase CopiesSerializer que hereda de ModelSerializer
    
    book = BookSerializer(read_only=True) # Atributo book de la tabla Copies
    editorial = EditorialsSerializer(read_only=True) # Atributo editorial de la tabla Copies
    
    class Meta: # Clase Meta que contiene los campos de la tabla Copies
        model = Copies # Modelo Copies
        fields = '__all__' # Campos de la tabla Copies
        read_only_fields = ['id_copy']# Campos de solo lectura de la tabla Copies
        

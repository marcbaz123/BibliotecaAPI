from pyexpat.errors import messages
from rest_framework import viewsets, permissions
from .models import Book, Copies, Editorials
from .serializers import BookSerializer, CopiesSerializer, EditorialsSerializer
from rest_framework.response import Response
from rest_framework import status

class BookViewSet(viewsets.ModelViewSet): # Clase BookViewSet que hereda de ModelViewSet
    queryset = Book.objects.all() # Consulta que retorna todos los libros
    permission_classes = [permissions.AllowAny] # Clase de permisos
    serializer_class = BookSerializer # Clase serializadora de Book
    

# Clase EditorialsViewSet que hereda de ModelViewSet
class EditorialsViewSet(viewsets.ModelViewSet):
    queryset = Editorials.objects.all() # Consulta que retorna todas las editoriales
    permission_classes = [permissions.AllowAny] # Clase de permisos
    serializer_class = EditorialsSerializer # Serializador de Editorial
       
class CopiesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]  # Permisos
    serializer_class = CopiesSerializer  # Usamos el serializador de Copies

    #Metodo para listar las copias segun el libro
    def get_queryset(self):
        
        book_id = self.kwargs['book_pk']
            # Filtra las copias por 'id_book' (libro)
        if not book_id:
            return Response({"Detail": "Bad request: el parametro 'book_id' es necesario"}, status=status.HTTP_400_BAD_REQUEST)        
        return Copies.objects.filter(id_book=book_id) 
            
    #Funcion del metodo crear para Copias
    def create(self, request, *args, **kwargs):
        try: 
            serializer = self.get_serializer(data=request.data) # serializa los datos recibidos
            if serializer.is_valid(): #Verifica si los datos son validos
                serializer.save() # Guarda en la base de datos
                return Response(serializer.data, status=status.HTTP_201_CREATED) # Devuelve la respuesta con 201 (Creado)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Si hay errores, devuelve 400
    
    #Funcion del metodo actualizar Copias
    def update(self, request, *args, **kwargs):
        try:
            
            instance = self.get_object() # Obtiene el objeto 'copy' correspondiente con el ID que se pasa en los parametros

            # Pasa los datos de la solicitud para ser validados y serializados
            serializer = self.get_serializer(instance, data=request.data, partial=False) # partial=True si solo se actualizan algunos campos

            if serializer.is_valid(): # Verifica la validez de los datos
                serializer.save() # Guarda los cambios en la BD
                return Response(serializer.data, status=status.HTTP_200_OK) # Devuelve la respuesta con 200 OK
            else:
                # Si hay errores, devuelve 400
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Devuelve error 400
            
        except Copies.DoesNotExist: # Excepcion de si no se encuentra la copia en la base de datos
            return Response({"detail":"No se ha encontrado la copia."}, status=status.HTTP_404_NOT_FOUND) # Si no encuentra el objeto
        
        except Exception as e: # Excepcion de cualquier otro error
            return Response({"detail":"str(e)"},status=status.HTTP_500_INTERNAL_SERVER_ERROR) # Devuelve error 500
    
    #Funcion que contiene el metodo eliminar
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object() # Obtiene el objeto a eliminar
            instance.delete() # Elimina el objeto de la base de datos
            return Response({"detail":"Eliminado Correctamente"},status=status.HTTP_204_NO_CONTENT) #Devuelve 204(Sin contenido)
        
        except Copies.DoesNotExist: # En caso de que el objeto a eliminar no exista
            return Response({"detail":"No se encontro la copia"}, status=status.HTTP_404_NOT_FOUND) #No se encontro la copia

        except Exception as e:
            # Devuelve error 500
            return Response({"detail": "str(e)"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

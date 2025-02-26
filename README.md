# BIBLIOTECA DjangoRest API

Esta API está diseñada para gestionar una biblioteca, permitiendo el control de los libros, sus copias y las editoriales responsables de su publicación.

## Descripción del Sistema

1. **Gestión de Libros**  
   El sistema permite almacenar y gestionar la información básica de los libros, como su título, autor y descripción. Los libros son la base para la gestión de las copias disponibles en la biblioteca.

2. **Gestión de Copias**  
   Cada libro puede tener múltiples copias, y el sistema controla el estado de cada una de estas copias. Las copias pueden estar en estado "Disponible" o "Prestado", lo que permite llevar un registro preciso de qué libros están disponibles para ser prestados y cuáles no.

3. **Gestión de Editoriales**  
   El sistema también maneja la información de las editoriales responsables de la publicación de los libros. Esto permite conocer qué editorial ha publicado cada libro y asociarlo con las copias disponibles en la biblioteca.

---

Este sistema tiene como objetivo facilitar la gestión de una biblioteca mediante un registro ordenado de los libros, sus copias y las editoriales, asegurando que tanto los usuarios como los administradores puedan llevar un control eficiente y detallado de todos los elementos.

Este proyecto utiliza Django y Django REST Framework para construir una API.  

## Instalación ##

Sigue estos pasos para configurar el entorno y ejecutar el proyecto.  

1. Instalar Virtualenv (si no lo tienes): `pip install virtualenv`  
2. Crear un entorno virtual en una carpeta llamada `venv`: `python -m venv venv`  
3. Activar el entorno virtual:  
   - **Windows**: `venv\Scripts\activate`  
   - **Mac/Linux**: `source venv/bin/activate`  
4. Instalar dependencias: `pip install django djangorestframework drf-nested-routers`  
5. Ejecutar la API: `python manage.py runserver`  

## Notas  
- Asegúrate de tener **Python 3.x** instalado.  
- Recuerda activar el entorno virtual antes de ejecutar comandos de Django.  

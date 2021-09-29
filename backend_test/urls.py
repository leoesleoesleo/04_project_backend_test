"""backend_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestorComidas.views import ingreso,crearPreferencia,crearRecor,UsuarioList,MenuCreate,MenuUpdate,MenuDelete,PreferUpdate,PreferDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',UsuarioList.as_view(),name='index'),
    path('ingresar/<int:idUsuario>/',ingreso,name='ingresar'),
    path('crear_menu/',MenuCreate.as_view(),name='crear_menu'),
    path('editar_menu/<int:pk>/',MenuUpdate.as_view(),name='editar_menu'),
    path('eliminar_menu/<int:pk>/',MenuDelete.as_view(),name='eliminar_menu'),
    path('crear_prefer/',crearPreferencia,name='crear_prefer'),
    path('editar_prefer/<int:pk>/',PreferUpdate.as_view(),name='editar_prefer'),
    path('eliminar_prefer/<int:pk>/',PreferDelete.as_view(),name='eliminar_prefer'),
    path('crear_record/',crearRecor,name='crear_record')
]

"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from dictec import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home',),
       path('signup/', views.signup, name='signup',),
       path('logout/', views.signout, name='logout',),
       path('signin/', views.signin, name='signin',),
       path('dashboard/', views.dashboard, name='dashboard',),
       path('cursos/', views.cursos, name='cursos',),
       path('facturas/', views.facturas, name='facturas',),
       path('lista_cobros_por_alumno/', views.lista_cobros_por_alumno, name='lista_cobros_por_alumno',),
       path('lista_cobros_por_alumno/<int:cobro_id>', views.modificar_cobro, name='modificar_cobro',),
       path('facturas/ingresar_cobro/', views.ingresar_cobro, name='ingresar_cobro',),
       path('facturas/<int:cobro_id>', views.cobros_alumno, name='cobros_alumno',),
    #    path('cursosadmin/', views.cursosadmin, name='cursosadmin',),
       path('dashboard_administracion/crear_nota/', views.crear_nota, name='crear_nota',),
       path('cursos/crear_notad/', views.crear_notad, name='crear_notad',),
       path('dashboard_administracion/<int:n_id>/', views.editar_nota, name='editar_nota',),
       path('imprimir/', views.imprimir, name='imprimir',),
       path('cursos/<int:c_id>', views.notas, name='notas',),
       path('curso/<int:curso_id>', views.curso, name='curso',),
       path('dashboard_administracion/', views.dashboard_administracion, name='dashboard_administracion',),
       path('dashboard_estudiante/', views.dashboard_estudiante, name='dashboard_estudiante',),
       path('dashboard_estudiante/estado_decuenta/', views.estado_decuenta, name='estado_decuenta',),
       path('cursos/<int:nd_id>/', views.edit_notad, name='edit_notad',),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
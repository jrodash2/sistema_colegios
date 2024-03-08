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
       path('cursos/crear_nota/', views.crear_nota, name='crear_nota',),
       path('cursos/<int:n_id>/', views.editar_nota, name='editar_nota',),
       path('imprimir/', views.imprimir, name='imprimir',),
       path('cursos/<int:c_id>', views.notas, name='notas',),
       path('curso/<int:curso_id>', views.curso, name='curso',),
       path('dashboard_administracion/', views.dashboard_administracion, name='dashboard_administracion',),
       path('dashboard_estudiante/', views.dashboard_estudiante, name='dashboard_estudiante',),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
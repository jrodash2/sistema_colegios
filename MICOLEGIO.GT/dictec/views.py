from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django. contrib import messages
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter



from dictec.models import Curso
from dictec.models import Calificacion
from dictec.models import Docente

from .forms import CalificacionForm

# Create your views here.



def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password no coninciden'
        })

def home(request):
    return render(request,'home.html')
   
def dashboard(request):
    return render(request,'dashboard.html')


# def listar_cliente(request):
#     busqueda = request.POST.get("buscar")
#     calificaciones = Calificacion.objects.all()

#     if busqueda:
#         clientes = Calificacion.objects.filter(
#             Q(estudiante__icontains = busqueda) | 
#             Q(grado__icontains = busqueda) |
#             Q(docente__icontains = busqueda) |
#             Q(curso__icontains = busqueda)
#         ).distinct()
         

#     return render(request, 'clientes.html', {'clientes':clientes})


def dashboard_administracion(request):
    busqueda = request.GET.get("buscar")
    calificaciones = Calificacion.objects.all()

    if busqueda:
        calificaciones = Calificacion.objects.filter(
            Q(usuario__username__icontains = busqueda) | 
            Q(grado__nombre__icontains = busqueda) |
            Q(docente__nombre__icontains = busqueda) |
            Q(mark_4__icontains = busqueda)
        ).distinct()
        
        
    return render(request,'dashboard_administracion.html', {'calificaciones': calificaciones})


    
def curso(request, curso_id):
    try:
        cursos = get_object_or_404(Curso, id=curso_id)
        calificaciones = Calificacion.objects.filter(curso=curso_id).exclude(activo=False).order_by("grado")
        return render(request, 'curso.html', {'cursos': cursos, 'calificaciones':calificaciones})
    except:
        return render(request, 'dashboard.html')
    
def imprimir(request):
   calificaciones = Calificacion.objects.filter(usuario=request.user)
   return render(request, 'imprimir.html', {'calificaciones': calificaciones})  
    
def cursos(request):
    calificaciones = Calificacion.objects.filter(docente__nombre='Juan Alfredo Marroquin Alvarez').exclude(activo=False).order_by("grado")

    return render(request, 'cursos.html', {'calificaciones': calificaciones})  
    
def notas(request, c_id):
    calificacion = Calificacion.objects.get(pk=c_id)
    return render(request, 'tarjeta.html', {'calificacion': calificacion})

        
def dashboard_estudiante(request):
    calificaciones = Calificacion.objects.filter(usuario=request.user).exclude(activo=False)
    return render(request,'dashboard_estudiante.html', {'calificaciones': calificaciones})
       
       
def crear_nota(request):
    if request.method == 'GET':
        return render(request, 'crear_nota.html', {
            'form': CalificacionForm
        })
    else:
        form = CalificacionForm(request.POST)
        new_dic = form.save(commit=False)
        new_dic.user = request.user
        new_dic.save()
        return redirect('cursos')
 
def editar_nota(request, n_id):
    if request.method == 'GET':
        calificacion = get_object_or_404(Calificacion, pk=n_id)
        form = CalificacionForm(instance=calificacion)
        return render(request, 'editar_nota.html', {'calificacion': calificacion, 'form': form})  
    else:
        calificacion = get_object_or_404(Calificacion, pk=n_id)
        form = CalificacionForm(request.POST, request.FILES, instance=calificacion)
        form.save()
        return redirect('cursos')
      

def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o Password es Incorecto'
        })

        else:
            login(request, user)
            data = user.groups.all()
            for g in data:
                print(g.name)
                if g.name=='Administrativo':
                   return redirect('cursos')
               
                elif g.name=='Docentes':
                       return redirect('cursos')
                elif g.name=='Estudiantes':
                   return redirect('dashboard_estudiante')
                else:
                    return redirect('home')
        
       
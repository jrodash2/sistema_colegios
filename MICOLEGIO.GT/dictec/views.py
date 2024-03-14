from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django. contrib import messages
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import CobroMensual
from datetime import date

from dictec.models import Curso
from dictec.models import Calificacion
from dictec.models import Estudiante
from dictec.models import Docente
from .forms import CalificacionForm
from .forms import CobroMensualForm
from .forms import ModificarCobroMensualForm
from django.contrib.auth.decorators import user_passes_test

def in_grupo_especifico(user):
    return user.groups.filter(name='Administrativo').exists()

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

@login_required
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

@login_required 
@user_passes_test(in_grupo_especifico)
def dashboard_administracion(request):
    busqueda = request.GET.get("buscar")
    calificaciones = Calificacion.objects.all().exclude(activo=False).order_by("grado")

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
 # Obtener la instancia de Docente asociada al usuario actualmente logeado
    usuario_actual = request.user
    docente = Docente.objects.get(usuario=usuario_actual)
    # Obtener todas las calificaciones del docente actualmente logeado
    calificaciones = Calificacion.objects.filter(docente=docente)
    return render(request, 'cursos.html', {'calificaciones': calificaciones})


# def cursosadmin(request):
#     calificaciones = Calificacion.objects.filter().exclude(activo=False).order_by("grado")

#     return render(request, 'cursosadmin.html', {'calificaciones': calificaciones})  





def facturas(request):
    busqueda = request.GET.get("buscar")
    estudiantes = Estudiante.objects.all().exclude(activo=False).order_by("grado")

    if busqueda:
        estudiantes = Estudiante.objects.filter(
            Q(usuario__username__icontains = busqueda) | 
            Q(grado__nombre__icontains = busqueda) 
        ).distinct()
    return render(request, 'contabilidad.html', {'estudiantes': estudiantes})  
    
    
def notas(request, c_id):
    calificacion = Calificacion.objects.get(pk=c_id)
    return render(request, 'tarjeta.html', {'calificacion': calificacion})


def estado_decuenta(request):
    cobros = CobroMensual.objects.filter(usuario=request.user).order_by("fecha_limite")
    hoy = date.today()
    for cobro in cobros:
        if not cobro.pagado and cobro.fecha_limite < hoy:
            cobro.mora = True
        else:
            cobro.mora = False
    return render(request, 'estado_decuenta.html', { 'cobros': cobros})
       
        
 
def edit_notad(request, nd_id):
    if request.method == 'GET':
        calificacion = get_object_or_404(Calificacion, pk=nd_id)
        form = CalificacionForm(instance=calificacion)
        return render(request, 'edit_notad.html', {'calificacion': calificacion, 'form': form})  
    else:
        calificacion = get_object_or_404(Calificacion, pk=nd_id)
        form = CalificacionForm(request.POST, request.FILES, instance=calificacion)
        form.save()
        return redirect('cursos')
      
    
       
       
       
        
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
    
          
def crear_notad(request):
    if request.method == 'GET':
        return render(request, 'crear_notad.html', {
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
                   return redirect('dashboard_administracion')
               
                elif g.name=='Docentes':
                       return redirect('cursos')
                elif g.name=='Estudiantes':
                   return redirect('dashboard_estudiante')
                else:
                    return redirect('home')
        
       
def cobros_alumno(request, cobro_id):
    alumno = Estudiante.objects.get(pk=cobro_id)
    cobros = CobroMensual.objects.filter(alumno=alumno).order_by("fecha_limite")
    hoy = date.today()
    for cobro in cobros:
        if not cobro.pagado and cobro.fecha_limite < hoy:
            cobro.mora = True
        else:
            cobro.mora = False
    return render(request, 'resumencuenta.html', {'alumno': alumno, 'cobros': cobros})
       



def ingresar_cobro(request):
    if request.method == 'POST':
        form = CobroMensualForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturas')  # Redirigir a la lista de cobros después de guardar el nuevo cobro
    else:
        form = CobroMensualForm()
    return render(request, 'ingresar_cobro.html', {'form': form})



def lista_cobros_por_alumno(request):
    
    alumnos = Estudiante.objects.all()
    cobros_por_alumno = {}
    for alumno in alumnos:
        cobros_por_alumno[alumno] = CobroMensual.objects.filter(alumno=alumno).order_by("fecha_limite")

    return render(request, 'lista_cobros.html', {'cobros_por_alumno': cobros_por_alumno})




def modificar_cobro(request, cobro_id):
    cobro = get_object_or_404(CobroMensual, pk=cobro_id)
    if request.method == 'POST':
        form = ModificarCobroMensualForm(request.POST, instance=cobro)
        if form.is_valid():
            form.save()
            return redirect('lista_cobros_por_alumno')  # Redirigir a la lista de cobros después de guardar los cambios
    else:
        form = ModificarCobroMensualForm(instance=cobro)
    return render(request, 'modificar_cobro.html', {'form': form})


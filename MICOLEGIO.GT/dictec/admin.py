
from django.contrib import admin

from .models import  Ciclo, Carrera, Grado, Curso, Calificacion, Docente, Estudiante

# modelos

class CicloAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')
    list_filter = ('nombre',)
admin.site.register(Ciclo, CicloAdmin)

class CarreraAdmin(admin.ModelAdmin):
    readonly_fields = ('activo',)
    list_display = ('nombre', 'ciclo', 'activo')
    list_filter = ('ciclo',)
admin.site.register(Carrera, CarreraAdmin)

class GradoAdmin(admin.ModelAdmin):
    readonly_fields = ('activo',)
    list_display = ('nombre', 'carrera', 'activo')
    list_filter = ('carrera',)
admin.site.register(Grado, GradoAdmin)

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')
admin.site.register(Curso, CursoAdmin)

class CalificacionAdmin(admin.ModelAdmin):
  
    list_display = ('estudiante', 'grado', 'curso', 'activo')

admin.site.register(Calificacion, CalificacionAdmin)

class DocenteAdmin(admin.ModelAdmin):
    readonly_fields = ('activo',)
    list_display = ( 'nombre', 'activo',)
admin.site.register(Docente, DocenteAdmin)

class EstudianteAdmin(admin.ModelAdmin):
    readonly_fields = ('activo',)
    list_display = ( 'nombre', 'activo',)
admin.site.register(Estudiante, EstudianteAdmin)
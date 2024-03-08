from django.db import models
from django.contrib.auth.models import User

# Create your models here.

         
# etiqueta / ciclo


class Ciclo (models.Model):
      nombre = models.CharField(max_length=200, verbose_name='Nombre')
      creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
      actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Modificación' )
      activo = models.BooleanField(default=True, verbose_name='Activo')
      
      class Meta:
            verbose_name = 'Ciclo'
            verbose_name_plural = 'Ciclos'
            ordering = ['nombre']
            
      def __str__(self):
          return self.nombre
            
# carreras

class Carrera (models.Model):
      nombre = models.CharField(max_length=200, verbose_name='Nombre')
      ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, verbose_name='Ciclo')
      creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
      actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Modificación')
      activo = models.BooleanField(default=True, verbose_name='Activo')
      
      class Meta:
            verbose_name = 'Carrera'
            verbose_name_plural = 'Carreras'
            ordering = ['nombre']
            
      def __str__(self):
            return self.nombre 
    
    


# grados

class Grado (models.Model):
      nombre = models.CharField(max_length=200, verbose_name='Nombre')
      carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name='Carrera')
      creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
      actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Modificación' )
      activo = models.BooleanField(default=True, verbose_name='Activo')
      
      class Meta:
            verbose_name = 'Grado'
            verbose_name_plural = 'Grados'
            ordering = ['nombre']
            
      def __str__(self):
          return self.nombre



# perfil docente

class Docente(models.Model):
      nombre = models.CharField(max_length=200, verbose_name='Nombre')
      telefono = models.CharField(max_length=8, verbose_name='Telefono')
      direccion = models.CharField(max_length=200, verbose_name='Direccion')
      cargo = models.CharField(max_length=200, verbose_name='Cargo')
      activo = models.BooleanField(default=True, verbose_name='Activo')
      creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
      actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Modificación' )
            
      class Meta:
            verbose_name = 'Docente'
            verbose_name_plural = 'Docentes'
            ordering = ['-creacion']
            
      def __str__(self):
          return str(self.nombre)
    
   
    
#  categoria / cursos

class Curso (models.Model):
      nombre = models.CharField(max_length=200, verbose_name='Nombre')
      grado = models.ForeignKey(Grado, on_delete=models.CASCADE, verbose_name='Grado')
      creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
      actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Modificación' )
      activo = models.BooleanField(default=True, verbose_name='Activo')
      docente = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name='Docente')

      
      class Meta:
            verbose_name = 'Curso'
            verbose_name_plural = 'Cursos'
            ordering = ['nombre']
            
      def __str__(self):
          return self.nombre
        
 
# # autor / estudiante = usuario registrados en la aplicacion = importando las tabla de usuarios

 
    # perfil estudiante

class Estudiante(models.Model):
      nombre = models.CharField(max_length=200, verbose_name='Nombre')
      usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
      telefono = models.CharField(max_length=8, verbose_name='Telefono')
      direccion = models.CharField(max_length=200, verbose_name='Direccion')
      carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name='Carrera')
      grado = models.ForeignKey(Grado, on_delete=models.CASCADE, verbose_name='Grado')
      activo = models.BooleanField(default=True, verbose_name='Activo')
      creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
      actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Modificación' )
            
      class Meta:
            verbose_name = 'Estudiante'
            verbose_name_plural = 'Estudiantes'
            ordering = ['-creacion']
            
      def __str__(self):
          return str(self.nombre)

# post / calificacion por curso

class Calificacion(models.Model):
      publicado =models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
      # campos relacionados
      carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name='Carrera')
      grado = models.ForeignKey(Grado, on_delete=models.CASCADE, verbose_name='Grado')
      curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
      docente = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name='Docente')
      estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')
      usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
      activo = models.BooleanField(default=True, verbose_name='Activo')
        
      creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
      actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Modificación' )
      
      mark_1 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 1')
      mark_2 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 2')
      mark_3 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 3')
      mark_4 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 4')
      average = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name='Promedio')

 
      #  Calcular el promedio (llamo a una función)
      def calculate_average(self):
        marks = [self.mark_1, self.mark_2, self.mark_3, self.mark_4]
        valid_marks = [mark for mark in marks if mark is not None]
        if valid_marks:
            return sum(valid_marks) / len(valid_marks)
        return None

      def save(self, *args, **kwargs):
        # Verifico si alguna nota cambio
        if self.mark_1 or self.mark_2 or self.mark_3 or self.mark_4:
            self.average = self.calculate_average()     # Calcular el promedio (llamo a una función)
        super().save(*args, **kwargs)

      class Meta:
            verbose_name = 'Calificacion'
            verbose_name_plural = 'Calificaciones'
            ordering = ['-creacion']
            
                
      def __str__(self):
            return str(self.curso)

            








  
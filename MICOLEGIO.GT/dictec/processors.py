from .models import Curso

def ctx_dic_curso(request):
    ctx_curso = {}
    
    ctx_curso['curso'] = Curso.objects.filter(activo=True)
    
    return ctx_curso
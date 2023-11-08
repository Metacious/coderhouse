from django.shortcuts import render

from familia.models import Familiar

# Create your views here.
def listar_familiares(request):
    contexto = {
        'familiares': Familiar.objects.all()
    }
    http_response = render(
        request=request,
        template_name='familia/familiares.html',
        context=contexto,
    )
    return http_response

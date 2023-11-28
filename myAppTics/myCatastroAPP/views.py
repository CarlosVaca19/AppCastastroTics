import json, urllib.request

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import FichaMantenimiento
from .models import ficha_mantenimiento, funcionarios_gadma


# from django.utils import simplejson

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('panel:panel')
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})


def index_view(request):
    # inst = ConfiguracionIndex.objects.get(pk=1)
    # noti = noticias_index.objects.all()
    # orga = organizaciones.objects.all()
    # productos = presentacion.objects.all()[:5]
    return render(request, 'paneladministracion/index.html',
                  {})


def index_funcionarios(request):
    # consultar servicio
    data = {}
    data['usuarips'] = []

    try:
        url = 'http://localhost:8080/sw/webresources/swRecursoAme/servcios_empleados/'  # url del servicio web
        response = urllib.request.urlopen(url)
        data = json.load(response)
    finally:
        tam = len(data)

    return render(request, 'funcionarios/index.html',
                  {'titulo': 'Funcionarios del Gadma', 'json': data, 'tamano': tam})


def index_asignaciones(request, id_funcionario):
    # http://localhost:8080/sw/webresources/swRecursoAme/equiposasignadosfuncionarios/?cedu=1311326605
    # consultar servicio
    data = {}
    data['usuarios'] = []

    try:
        url = 'http://localhost:8080/sw/webresources/swRecursoAme/equiposasignadosfuncionarios/?cedu=' + id_funcionario  # url del servicio web
        response = urllib.request.urlopen(url)
        data = json.load(response)
    finally:
        tam = len(data)

    return render(request, 'funcionarios/asignaciones_funcionarios.html',
                  {'titulo': 'Asignaciones al Funcionario', 'json': data, 'tamano': tam})


def actualizar_funcionarios_sw(request):
    funcionarios = funcionarios_gadma.objects.all()
    return render(request, 'funcionarios/index.html',
                  {'titulo': 'FUNCIONARIOS', 'json': funcionarios, 'tamano': len(funcionarios)})


def generar_ficha(request, id_equipomantenimiento):
    # http://localhost:8080/sw/webresources/swRecursoAme/identificadorporequipo/?id=1858
    # consultar servicio
    data = {}
    data['equipo'] = []

    try:
        url = 'http://localhost:8080/sw/webresources/swRecursoAme/identificadorporequipo/?id=' + id_equipomantenimiento  # url del servicio web
        response = urllib.request.urlopen(url)
        data = json.load(response)
    finally:
        tam = len(data)
    mensaje = 'ingresar'
    if request.method == 'POST':
        ficha = ficha_mantenimiento(
            det_asig_numero=request.POST.get("det_asig_numero"),
            act_fi_identificador=request.POST.get("act_fi_identificador"),
            det_asig_observacion=request.POST.get("det_asig_observacion"),
            act_fi_codigo=request.POST.get("act_fi_codigo"),
            act_fi_nombre=request.POST.get("act_fi_nombre"),
            act_fi_tipo=request.POST.get("act_fi_tipo"),
            act_fi_nivel=request.POST.get("act_fi_nivel"),
            act_fi_marca=request.POST.get("act_fi_marca"),
            act_fi_modelo=request.POST.get("act_fi_modelo"),
            act_fi_serie=request.POST.get("act_fi_serie"),
            act_fi_color=request.POST.get("act_fi_color"),
            act_fi_accesorios=request.POST.get("act_fi_accesorios"),
            act_fi_valor_compra=request.POST.get("act_fi_valor_compra"),
            act_fi_fecha_compra=request.POST.get("act_fi_fecha_compra"),
            act_fi_vida_util=request.POST.get("act_fi_vida_util"),
            act_fi_estado=request.POST.get("act_fi_estado"),
            act_fi_condicion=request.POST.get("act_fi_condicion"),
            act_fi_asignado=request.POST.get("act_fi_asignado"),
            act_fi_factura=request.POST.get("act_fi_factura")
        )
        ficha.save()
        return render(request, 'equipoinformatico/fichagenerada.html',
                      {'titulo': 'Ficha Equipo', 'json': data, 'tamano': tam, 'sms': mensaje})
    else:
        form = FichaMantenimiento()
        return render(request, 'equipoinformatico/fichamantenimiento.html',
                      {'titulo': 'Ficha Equipo', 'json': data, 'tamano': tam, 'form': form})

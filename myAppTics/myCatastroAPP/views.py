import json, urllib.request

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import ficha_mantenimiento, funcionarios_gadma




#from django.utils import simplejson

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
    #inst = ConfiguracionIndex.objects.get(pk=1)
    #noti = noticias_index.objects.all()
    #orga = organizaciones.objects.all()
    #productos = presentacion.objects.all()[:5]
    return render(request, 'paneladministracion/index.html',
                  {})


def index_funcionarios(request):

    #consultar servicio
    data ={}
    data['usuarips']=[]

    try:
        url = 'http://localhost:8080/sw/webresources/swRecursoAme/servcios_empleados/'  # url del servicio web
        response = urllib.request.urlopen(url)
        data = json.load(response)
    finally:
        tam = len(data)

    return render(request, 'funcionarios/index.html',
                  {'titulo':'Funcionarios del Gadma', 'json':data, 'tamano':tam})



def index_asignaciones(request, id_funcionario):
    #http://localhost:8080/sw/webresources/swRecursoAme/equiposasignadosfuncionarios/?cedu=1311326605
    #consultar servicio
    data ={}
    data['usuarios']=[]

    try:
        url = 'http://localhost:8080/sw/webresources/swRecursoAme/equiposasignadosfuncionarios/?cedu='+id_funcionario  # url del servicio web
        response = urllib.request.urlopen(url)
        data = json.load(response)
    finally:
        tam = len(data)

    return render(request, 'funcionarios/asignaciones_funcionarios.html',
                  {'titulo':'Asignaciones al Funcionario', 'json':data, 'tamano':tam})


def actualizar_funcionarios_sw(request):
    funcionarios = funcionarios_gadma.objects.all()
    return render(request, 'funcionarios/index.html',
                  {'titulo':'FUNCIONARIOS', 'json':funcionarios, 'tamano':len(funcionarios)})


def generar_ficha(request, id_equipomantenimiento):
    #http://localhost:8080/sw/webresources/swRecursoAme/identificadorporequipo/?id=1858
    #consultar servicio
    data ={}
    data['equipo']=[]

    try:
        url = 'http://localhost:8080/sw/webresources/swRecursoAme/identificadorporequipo/?id='+id_equipomantenimiento  # url del servicio web
        response = urllib.request.urlopen(url)
        data = json.load(response)
    finally:
        tam = len(data)
    if request.method == 'POST':
        for equipo in  data['equipo']:
            ficha = ficha_mantenimiento(
                det_asig_numero= equipo[0],
                act_fi_identificador =equipo[1],
                asig_identificador = equipo[2],
                det_asig_observacion = equipo[3],
                act_fi_codigo = equipo[4],
                act_fi_nombre =  equipo.act_fi_nombre,
                act_fi_tipo = equipo.act_fi_tipo,
                act_fi_nivel = equipo.act_fi_nivel,
                act_fi_marca = equipo.act_fi_marca,
                act_fi_modelo = equipo.act_fi_modelo,
                act_fi_serie = equipo.act_fi_serie,
                act_fi_color = equipo.act_fi_color,
                act_fi_accesorios = equipo.act_fi_accesorios,
                act_fi_valor_compra = equipo.act_fi_valor_compra,
                act_fi_fecha_compra = equipo.act_fi_fecha_compra,
                act_fi_vida_util =equipo.act_fi_vida_util,
                act_fi_dep_acum = equipo.act_fi_dep_acum,
                act_fi_estado = equipo.act_fi_estado,
                act_fi_dep_periodo = equipo.act_fi_dep_periodo,
                act_fi_cuad_contab = equipo.act_fi_cuad_contab,
                act_fi_cantidad = equipo.act_fi_cantidad,
                act_fi_condicion = equipo.act_fi_condicion,
                act_fi_estCompra = equipo.act_fi_estCompra,
                act_fi_valor_reval = equipo.act_fi_valor_reval,
                act_fi_asignado = equipo.act_fi_asignado,
                act_fi_factura = equipo.act_fi_factura,
                act_fi_capitaliza = equipo.act_fi_capitaliza,
                act_fi_fecha_ingreso = equipo.act_fi_fecha_ingreso,
                act_fi_codigo_mef = equipo.act_fi_codigo_mef,
                asig_fecha = equipo.asig_fecha,
                ent_traspaso = equipo.ent_traspaso,
                det_asig_asignado = equipo.det_asig_asignado,
                det_asig_estado = equipo.det_asig_estado,
                det_asig_valor =equipo.det_asig_valor,)
            ficha.save()
        return render(request, 'equipoinformatico/fichagenerada.html',
           {'titulo': 'Ficha Equipo', 'json': data, 'tamano': tam})

    return render(request, 'equipoinformatico/fichamantenimiento.html',
                  {'titulo':'Ficha Equipo', 'json':data, 'tamano':tam})

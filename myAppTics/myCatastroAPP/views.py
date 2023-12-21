import datetime
import json, urllib.request
import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.staticfiles import finders
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from .forms import FichaMantenimiento
from .models import ficha_mantenimiento, funcionarios_gadma, historial_mantenimiento
from django.conf import settings


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
    numero_mantenimiento = historial_mantenimiento.objects.all()
    numero_equipos = ficha_mantenimiento.objects.all()
    return render(request, 'paneladministracion/index.html',
                  {'ne': len(numero_equipos) , 'nm': len(numero_mantenimiento), 'json':numero_mantenimiento})


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
    bandera = "NO"
    id_ficha = 0
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
        fmant = ficha_mantenimiento.objects.all().filter(act_fi_identificador=id_equipomantenimiento)
        if len(fmant) > 0:
            for ficha_nueva in fmant:
                id_ficha = ficha_nueva.id
        return redirect('panel:historial_mantenimiento', id_ficha)

    else:
        form = FichaMantenimiento()
        #fmant = ficha_mantenimiento.objects.get(act_fi_identificador=id_equipomantenimiento)
        fmant = ficha_mantenimiento.objects.all().filter(act_fi_identificador=id_equipomantenimiento)
        if len(fmant) > 0:
            bandera = "SI"
            for ficha_nueva in fmant:
                id_ficha = ficha_nueva.id
                nombre_ficha = ficha_nueva.act_fi_nombre
        #return redirect('panel:historial_mantenimiento', id_ficha)
        return render(request, 'equipoinformatico/fichamantenimiento.html',
                      {'titulo': 'Ficha Equipo', 'json': data, 'tamano': tam, 'form': form, 'bandera':bandera,
                       'id_ficha':id_ficha})


def index_historial_mantenimiento(request, id_ficha_mantenimiento):
    historial_mantenimiento1 = historial_mantenimiento.objects.all().filter(id_ficha_mantenimiento=id_ficha_mantenimiento)
    inst_mantenimiento = ficha_mantenimiento.objects.get(pk=id_ficha_mantenimiento)
    return render(request, 'equipoinformatico/fichagenerada.html',
                  {'titulo': 'Hisorial de Mantenimiento', 'json': historial_mantenimiento1, 'ficha':inst_mantenimiento})


def generarmantenimiento(request, id_ficha_mantenimiento):
    inst_mantenimiento = ficha_mantenimiento.objects.get(pk=id_ficha_mantenimiento)

    if request.method == 'POST':
        form = historial_mantenimiento(request.POST)

        ficha = historial_mantenimiento(
            id_ficha_mantenimiento = inst_mantenimiento,
            tipo_mantenimiento= request.POST.get("tipo_mantenimiento"),
            observaciones=request.POST.get("observaciones"),
            fecha_mantenimiento = request.POST.get("fecha_mantenimiento"),
            funcionario_encargado = request.POST.get("funcionario_encargado")
        )
        ficha.save()
        return redirect('panel:historial_mantenimiento', id_ficha_mantenimiento)
    else:
        form = historial_mantenimiento()
        contexto = {'message': 'Guardado con Exito',
                'form': form,
                'ficha': inst_mantenimiento,
                'titulo': "Nuevo Mantenimiento"
                }
    return render(request, 'equipoinformatico/nuevomantenimiento.html', contexto)


class mantenimientoPDF_view(View):
    def link_callback(self, uri, rel):
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL  # Typically /static/
            sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL  # Typically /media/
            mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri
        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        historial_mantenimiento1 = historial_mantenimiento.objects.all()
        #admision = admisione.objects.get(pk=self.kwargs['pk']) #obtener la admission.
        #estudios = estudios_realizado.objects.all().filter(ci=admision.ci.ci)
        #user = User.objects.get(
        #    username=self.request.user)  # envia el usuario que esta en la logueado en la aplicacion.
        reporte_name = "reporte"
        template_path = 'reportes/reporte1.html'
        fecha = datetime.date.today()
        context = {'tittle': 'MANTENIMIENTO DE EQUIPOS INFORMATICOS ', 'FICHA': '01',
                   'items': historial_mantenimiento1,
                   'codigo': 100,
                   'icon': '{}{}'.format(settings.MEDIA_URL, 'el-coca.jpg'),
                   'estudios': 100,
                   'date': fecha
                   #'usuario': user
                   }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + reporte_name + ".pdf"
        template = get_template(template_path)
        html = template.render(context)
        if request.POST.get('show_html', ''):
            response['Content-Type'] = 'application/text'
            response['Content-Disposition'] = 'attachment; filename="ABC.txt"'
            response.write(html)
        else:
            pisaStatus = pisa.CreatePDF(
                html.encode("UTF-8"), dest=response, link_callback=self.link_callback)
            if pisaStatus.err:
                return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err, html))
        return response
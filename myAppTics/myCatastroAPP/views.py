import datetime
import json, urllib.request
import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from .forms import FichaMantenimiento, historial_mantenimientoFORM
from .models import ficha_mantenimiento, funcionarios_gadma, historial_mantenimiento
from django.conf import settings


# from django.utils import simplejson

# Definir la función de vista para el inicio de sesión
def login_view(request):
    # Verificar si el formulario se envió mediante POST
    if request.method == 'POST':
        # Crear una instancia de AuthenticationForm con los datos POST
        form = AuthenticationForm(request.POST)
        # Obtener el nombre de usuario y la contraseña de los datos POST
        username = request.POST['username']
        password = request.POST['password']
        # Autenticar al usuario utilizando las credenciales proporcionadas
        user = authenticate(username=username, password=password)
        # Verificar si el usuario está autenticado y activo
        if user is not None:
            if user.is_active:
                # Iniciar sesión del usuario y redirigir a la página del panel
                login(request, user)
                return redirect('panel:panel')
    else:
        # Si el formulario no se envió mediante POST, crear un AuthenticationForm vacío
        form = AuthenticationForm()
    # Renderizar la página de inicio de sesión con el formulario
    return render(request, 'login/index.html', {'form': form})

# Definir la función de vista para la página de inicio del panel de administración
def index_view(request):
    # Obtener todos los registros de historial_mantenimiento y ficha_mantenimiento
    numero_mantenimiento = historial_mantenimiento.objects.all()
    numero_equipos = ficha_mantenimiento.objects.all()
    # Renderizar la página de inicio con la cantidad de mantenimientos y equipos
    return render(request, 'paneladministracion/index.html',
                  {'ne': len(numero_equipos) , 'nm': len(numero_mantenimiento), 'json':numero_mantenimiento})

# Definir la función de vista para la página de funcionarios
def index_funcionarios(request):
    # Inicializar un diccionario para almacenar datos
    data = {}
    data['usuarips'] = []

    try:
        # Definir la URL del servicio web
        url = 'http://localhost:8080/sw/webresources/swRecursoAme/servcios_empleados/'
        # Realizar una solicitud al servicio web y cargar los datos en formato JSON
        response = urllib.request.urlopen(url)
        data = json.load(response)
    finally:
        # Obtener el tamaño de los datos obtenidos
        tam = len(data)
    # Renderizar la página de funcionarios con el título, datos y tamaño
    return render(request, 'funcionarios/index.html',
                  {'titulo': 'Funcionarios del Gadma', 'json': data, 'tamano': tam})

# Definir la función de vista para la página de asignaciones de un funcionario
def index_asignaciones(request, id_funcionario):
    # Inicializar un diccionario para almacenar datos
    data = {}
    data['usuarios'] = []

    try:
        # Construir la URL del servicio web con el ID del funcionario
        url = 'http://localhost:8080/sw/webresources/swRecursoAme/equiposasignadosfuncionarios/?cedu=' + id_funcionario

        # Realizar una solicitud al servicio web y cargar los datos en formato JSON
        response = urllib.request.urlopen(url)
        data = json.load(response)
    finally:
        # Obtener el tamaño de los datos obtenidos
        tam = len(data)
    # Renderizar la página de asignaciones de funcionarios con el título, datos y tamaño como contexto
    return render(request, 'funcionarios/asignaciones_funcionarios.html',
                  {'titulo': 'Asignaciones al Funcionario', 'json': data, 'tamano': tam})

# Definir la función de vista para actualizar funcionarios desde el software (sw) externo
def actualizar_funcionarios_sw(request):
    # Obtener todos los funcionarios desde la base de datos local
    funcionarios = funcionarios_gadma.objects.all()

    # Renderizar la página de funcionarios con el título, datos y tamaño como contexto
    return render(request, 'funcionarios/index.html',
                  {'titulo': 'FUNCIONARIOS', 'json': funcionarios, 'tamano': len(funcionarios)})

# Definir la función de vista para generar una ficha de mantenimiento
def generar_ficha(request, id_equipomantenimiento):
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
        # Procesar el formulario cuando se envía por POST
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
        # Obtener la nueva ficha después de guardarla
        fmant = ficha_mantenimiento.objects.all().filter(act_fi_identificador=id_equipomantenimiento)
        if len(fmant) > 0:
            for ficha_nueva in fmant:
                id_ficha = ficha_nueva.id
        return redirect('panel:historial_mantenimiento', id_ficha)

    else:
        # Renderizar el formulario cuando se accede a la página
        form = FichaMantenimiento()
        # Verificar si ya existe una ficha para este equipo
        fmant = ficha_mantenimiento.objects.all().filter(act_fi_identificador=id_equipomantenimiento)
        if len(fmant) > 0:
            bandera = "SI"
            for ficha_nueva in fmant:
                id_ficha = ficha_nueva.id
                nombre_ficha = ficha_nueva.act_fi_nombre

        # Renderizar la página de equipo informatico con el título, datos y tamaño como contexto
        return render(request, 'equipoinformatico/fichamantenimiento.html',
                      {'titulo': 'Ficha Equipo', 'json': data, 'tamano': tam, 'form': form, 'bandera':bandera,
                       'id_ficha':id_ficha})

# Definir la función de vista para mostrar el historial de mantenimiento de una ficha específica
def index_historial_mantenimiento(request, id_ficha_mantenimiento):
    # Obtener el historial de mantenimiento asociado a la ficha específica
    historial_mantenimiento1 = historial_mantenimiento.objects.all().filter(id_ficha_mantenimiento=id_ficha_mantenimiento)

    # Obtener la ficha de mantenimiento correspondiente
    inst_mantenimiento = ficha_mantenimiento.objects.get(pk=id_ficha_mantenimiento)
    # Renderizar la página con la información del historial y la ficha de mantenimiento
    return render(request, 'equipoinformatico/fichagenerada.html',
                  {'titulo': 'Hisorial de Mantenimiento', 'json': historial_mantenimiento1, 'ficha':inst_mantenimiento})

# Definir la función de vista para generar un nuevo registro de mantenimiento
def generarmantenimiento(request, id_ficha_mantenimiento):
    # Obtener la ficha de mantenimiento correspondiente al ID proporcionado
    inst_mantenimiento = ficha_mantenimiento.objects.get(pk=id_ficha_mantenimiento)

    if request.method == 'POST':
        # Procesar el formulario enviado por el método POST
        form = historial_mantenimiento(request.POST)

        # Crear un nuevo registro de mantenimiento con los datos del formulario
        ficha = historial_mantenimiento(
            id_ficha_mantenimiento = inst_mantenimiento,
            tipo_mantenimiento= request.POST.get("tipo_mantenimiento"),
            observaciones=request.POST.get("observaciones"),
            fecha_mantenimiento = request.POST.get("fecha_mantenimiento"),
            funcionario_encargado = request.POST.get("funcionario_encargado"),
            piezas_reemplazadas = request.POST.get("piezas_reemplazadas"),
            horas_trabajo = request.POST.get("horas_trabajo"),
            recomendaciones = request.POST.get("recomendaciones")
        )
        # Guardar el nuevo registro en la base de datos
        ficha.save()
        # Redirigir a la página de historial de mantenimiento de la ficha específica
        return redirect('panel:historial_mantenimiento', id_ficha_mantenimiento)
    else:
        # Si la solicitud no es POST, renderizar el formulario vacío
        form = historial_mantenimientoFORM()
        user = User.objects.get(username=request.user)
        contexto = {'message': 'Guardado con Exito',
                'form': form,
                'ficha': inst_mantenimiento,
                'titulo': "Nuevo Mantenimiento",
                'usuario': user
                }
    # Renderizar la página con el formulario y la información de la ficha
    return render(request, 'equipoinformatico/nuevomantenimiento.html', contexto)

# Definir la clase de la vista para generar un PDF de mantenimiento
class mantenimientoPDF_view(View):
    # Función de devolución de llamada para manejar los enlaces en el PDF
    def link_callback(self, uri, rel):
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL
            sRoot = settings.STATIC_ROOT
            mUrl = settings.MEDIA_URL
            mRoot = settings.MEDIA_ROOT

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri
        # Asegurarse de que el archivo exista
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    # Método GET para generar el PDF
    def get(self, request, *args, **kwargs):
        # Obtener todos los registros de historial de mantenimiento
        historial_mantenimiento1 = historial_mantenimiento.objects.all()

        # Configurar los parámetros para el PDF
        reporte_name = "reporte"
        template_path = 'reportes/reporte1.html'
        fecha = datetime.date.today()
        context = {'tittle': 'MANTENIMIENTO DE EQUIPOS INFORMATICOS ', 'FICHA': '01',
                   'items': historial_mantenimiento1,
                   'codigo': 100,
                   'icon': '{}{}'.format(settings.MEDIA_URL, 'logoarchidona.png'),
                   'estudios': 100,
                   'date': fecha
                   #'usuario': user
                   }
        # Configurar la respuesta HTTP para el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + reporte_name + ".pdf"
        # Obtener la plantilla HTML y renderizarla con los datos
        template = get_template(template_path)
        html = template.render(context)

        # Verificar si se debe mostrar el HTML en lugar de generar el PDF
        if request.POST.get('show_html', ''):
            response['Content-Type'] = 'application/text'
            response['Content-Disposition'] = 'attachment; filename="ABC.txt"'
            response.write(html)
        else:
            # Generar el PDF a partir del HTML y agregarlo a la respuesta
            pisaStatus = pisa.CreatePDF(
                html.encode("UTF-8"), dest=response, link_callback=self.link_callback)
            if pisaStatus.err:
                return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err, html))
        return response

# Definir la clase de la vista para generar un PDF de mantenimiento individual
class mantenimientoPDFINDIVIDUAL_view(View):
    # Función de devolución de llamada para manejar los enlaces en el PDF
    def link_callback(self, uri, rel):
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL
            sRoot = settings.STATIC_ROOT
            mUrl = settings.MEDIA_URL
            mRoot = settings.MEDIA_ROOT

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri
        # Asegurarse de que el archivo exista
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    # Método GET para generar el PDF
    def get(self, request, *args, **kwargs):
        # Obtener el registro de historial de mantenimiento individual
        historial_mantenimiento1 = historial_mantenimiento.objects.get(pk=self.kwargs['pk']) #obtener la admission.

        # Configurar los parámetros para el PDF
        reporte_name = "reporte"
        template_path = 'reportes/mantenimiento_ficha.html'
        fecha = datetime.date.today()
        context = {'tittle': 'MANTENIMIENTO DE EQUIPOS INFORMATICOS ', 'FICHA': '01',
                   'items': historial_mantenimiento1,
                   'codigo': 100,
                   'icon': '{}{}'.format(settings.MEDIA_URL, 'logoarchidona.png'),
                   'estudios': 100,
                   'date': fecha
                   #'usuario': user
                   }
        # Configurar la respuesta HTTP para el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + reporte_name + ".pdf"

        # Obtener la plantilla HTML y renderizarla con los datos
        template = get_template(template_path)
        html = template.render(context)

        # Verificar si se debe mostrar el HTML en lugar de generar el PDF
        if request.POST.get('show_html', ''):
            response['Content-Type'] = 'application/text'
            response['Content-Disposition'] = 'attachment; filename="ABC.txt"'
            response.write(html)
        else:
            # Generar el PDF a partir del HTML y agregarlo a la respuesta
            pisaStatus = pisa.CreatePDF(
                html.encode("UTF-8"), dest=response, link_callback=self.link_callback)
            if pisaStatus.err:
                return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err, html))
        return response
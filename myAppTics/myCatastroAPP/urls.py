from django.urls import path

from .views import login_view, index_view, index_funcionarios, index_asignaciones, generar_ficha, \
    index_historial_mantenimiento, generarmantenimiento, mantenimientoPDF_view, mantenimientoPDFINDIVIDUAL_view

# Definir los patrones de URL para las vistas
urlpatterns = [
    # Página de inicio de sesión
    path('', login_view, name='login'),

    # Panel principal después del inicio de sesión
    path('panel', index_view,name='panel'),

    # Vista para mostrar la lista de funcionarios
    path('funcionarios', index_funcionarios,name='index_funcionarios'),

    # Vista para mostrar asignaciones de equipos a un funcionario específico
    path('funcionarios/(?P<id_funcionario>\d+)/$', index_asignaciones, name='funcionarios_asignaciones'),

    # Vista para generar la ficha de mantenimiento de un equipo específico
    path('equipo/ficha/(?P<id_equipomantenimiento>\d+)/$', generar_ficha, name='equipo_ficha'),

    # Vista para mostrar el historial de mantenimiento de un equipo
    path('equipo/historial/(?P<id_ficha_mantenimiento>\d+)/$', index_historial_mantenimiento, name='historial_mantenimiento'),

    # Vista para generar un nuevo mantenimiento para un equipo
    path('equipo/historia/nuevo/(?P<id_ficha_mantenimiento>\d+)/$', generarmantenimiento, name='nuevo_mantenimiento'),

    # Vista para generar el informe PDF del historial de mantenimiento
    path('mantenimiento/pdf/<int:pk>/', mantenimientoPDF_view.as_view(), name='ReporteMantenimiento'),

    # Vista para generar el informe PDF individual de un mantenimiento
    path('mantenimientoidv/pdf/<int:pk>/', mantenimientoPDFINDIVIDUAL_view.as_view(), name='ReporteMantenimientoidv'),

]
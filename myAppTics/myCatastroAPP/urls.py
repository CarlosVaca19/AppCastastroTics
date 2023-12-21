from django.urls import path

from .views import login_view, index_view, index_funcionarios, index_asignaciones, generar_ficha, \
    index_historial_mantenimiento, generarmantenimiento, mantenimientoPDF_view

urlpatterns = [
    #path('', index_principal.as_view(), name='index1'),
   # path('/', index_principalF, name='index'),
    path('', login_view, name='login'),
    path('panel', index_view,name='panel'),
    path('funcionarios', index_funcionarios,name='index_funcionarios'),
    path('funcionarios/(?P<id_funcionario>\d+)/$', index_asignaciones, name='funcionarios_asignaciones'),
    path('equipo/ficha/(?P<id_equipomantenimiento>\d+)/$', generar_ficha, name='equipo_ficha'),
    path('equipo/historial/(?P<id_ficha_mantenimiento>\d+)/$', index_historial_mantenimiento, name='historial_mantenimiento'),
    path('equipo/historia/nuevo/(?P<id_ficha_mantenimiento>\d+)/$', generarmantenimiento, name='nuevo_mantenimiento'),


    path('mantenimiento/pdf/<int:pk>/', mantenimientoPDF_view.as_view(), name='ReporteMantenimiento'),

]
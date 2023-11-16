from django.urls import path

from .views import login_view, index_view, index_funcionarios, index_asignaciones

urlpatterns = [
    #path('', index_principal.as_view(), name='index1'),
   # path('/', index_principalF, name='index'),
    path('', login_view, name='login'),
    path('panel', index_view,name='panel'),
    path('funcionarios', index_funcionarios,name='index_funcionarios'),
    path('funcionarios/(?P<id_funcionario>\d+)/$', index_asignaciones, name='funcionarios_asignaciones'),
    #path('acerca', acerca_de, name='acerca_de'),
    #path('organizaciones', organizaciones_view, name='organizaciones_view'),
   # path('productos', procudtos_view, name='procudtos_view'),
    #path('ayuda', ayuda, name='ayuda_view'),

]

from django import forms

from .models import ficha_mantenimiento, historial_mantenimiento

# Definir el formulario para la ficha de mantenimiento
class FichaMantenimiento(forms.ModelForm):
    class Meta:
        # Especificar el modelo asociado al formulario
        model = ficha_mantenimiento
        # Especificar los campos que se mostrarán en el formulario
        fields = [
            'det_asig_numero',
            'act_fi_identificador',
            'det_asig_observacion',
            'act_fi_codigo',
            'act_fi_nombre',
            'act_fi_tipo',
            'act_fi_nivel',
            'act_fi_marca',
            'act_fi_modelo',
            'act_fi_serie',
            'act_fi_color',
            'act_fi_accesorios',
            'act_fi_valor_compra',
            'act_fi_fecha_compra' ,
            'act_fi_vida_util',
            'act_fi_estado',
            'act_fi_condicion',
            'act_fi_asignado',
            'act_fi_factura',
        ]

        # Etiquetas personalizadas para los campos
        labels = {
            'det_asig_numero':'det_asig_numero',
            'act_fi_identificador':'act_fi_identificador',
            'det_asig_observacion':'det_asig_observacion',
            'act_fi_codigo':'act_fi_codigo',
            'act_fi_nombre':'act_fi_nombre',
            'act_fi_tipo':'act_fi_tipo',
            'act_fi_nivel':'act_fi_nivel',
            'act_fi_marca':'act_fi_marca',
            'act_fi_modelo':'act_fi_modelo',
            'act_fi_serie':'act_fi_serie',
            'act_fi_color':'act_fi_color',
            'act_fi_accesorios':'act_fi_accesorios',
            'act_fi_valor_compra':'act_fi_valor_compra',
            'act_fi_fecha_compra':'act_fi_fecha_compra',
            'act_fi_vida_util':'act_fi_vida_util',
            'act_fi_condicion':'act_fi_condicion',
            'act_fi_asignado':'act_fi_asignado',
            'act_fi_factura':'act_fi_factura',
        }

        # Configuración de widgets para la presentación del formulario
        widgets = {
            'det_asig_numero': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_identificador': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'det_asig_observacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_codigo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_nombre': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_tipo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_nivel': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_marca': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_modelo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_serie': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_color': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_accesorios': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_valor_compra': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_fecha_compra': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_vida_util': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_estado': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_condicion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_asignado': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'act_fi_factura': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

# Definir el formulario para el historial de mantenimiento
class historial_mantenimientoFORM(forms.ModelForm):

    class Meta:
        # Especificar el modelo asociado al formulario
        model = historial_mantenimiento
        # Especificar los campos que se mostrarán en el formulario
        fields = [
            'id_ficha_mantenimiento',
            'tipo_mantenimiento',
            'observaciones',
            'fecha_mantenimiento',
            'funcionario_encargado',
            'piezas_reemplazadas',
            'horas_trabajo',
            'recomendaciones',
        ]

        # Etiquetas personalizadas para los campos
        labels = {
            'id_ficha_mantenimiento':'id_ficha_mantenimiento',
            'tipo_mantenimiento':'tipo_mantenimiento',
            'observaciones':'observaciones',
            'fecha_mantenimiento':'fecha_mantenimiento',
            'funcionario_encargado':'funcionario_encargado',
            'piezas_reemplazadas':'piezas_reemplazadas',
            'horas_trabajo':'horas_trabajo',
            'recomendaciones':'recomendaciones',
        }

        # Configuración de widgets para la presentación del formulario
        widgets = {
            'id_ficha_mantenimiento': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tipo_mantenimiento': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_mantenimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'funcionario_encargado': forms.TextInput(attrs={'class': 'form-control'}),
            'piezas_reemplazadas': forms.TextInput(attrs={'class': 'form-control'}),
            'horas_trabajo': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'recomendaciones': forms.TextInput(attrs={'class': 'form-control'}),


        }
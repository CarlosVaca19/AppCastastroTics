from django.db import models

# Create your models here.
class funcionarios_gadma(models.Model):
    iden= models.CharField(verbose_name="Cedula", null=True, max_length=100) # ¿A que iglesia Pertenece?
    ent_nombre = models.CharField(verbose_name="Nombres", null=True, max_length=100) # Denominacion
    ent_apellido= models.CharField(verbose_name="Apellidos", null=True, max_length=200) # Direccion Iglesia, en el formulario considerar Calle, Canton, Provincia
    ent_ingreso = models.CharField(verbose_name="Fecha Ingreso") # ¿Eres mienbro?
    ent_salida = models.CharField(verbose_name="Fecha Salida",null=True)
    ent_cargo = models.CharField(verbose_name="Cargos ",null=True, max_length=200)
    ent_sexo = models.CharField(verbose_name="Sexo", null=True, max_length=2)
    dep_nombre = models.CharField(verbose_name="Departamento", null=True, max_length=70)


class ficha_mantenimiento(models.Model):
    det_asig_numero= models.CharField(verbose_name="det_asig_numero", null=True, max_length=100) # ¿A que iglesia Pertenece?
    act_fi_identificador = models.CharField(verbose_name="act_fi_identificador", null=True, max_length=100) # Denominacion
    det_asig_observacion = models.CharField(verbose_name="det_asig_observacion") # ¿Eres mienbro?
    act_fi_codigo = models.CharField(verbose_name="act_fi_codigo ",null=True, max_length=50)
    act_fi_nombre = models.CharField(verbose_name="act_fi_nombre", null=True, max_length=100)
    act_fi_tipo = models.CharField(verbose_name="act_fi_tipo", null=True, max_length=5)
    act_fi_nivel = models.CharField(verbose_name="act_fi_nivel", null=True, max_length=100)
    act_fi_marca = models.CharField(verbose_name="act_fi_marca", null=True, max_length=100)
    act_fi_modelo = models.CharField(verbose_name="act_fi_modelo", null=True, max_length=70)
    act_fi_serie = models.CharField(verbose_name="act_fi_serie", null=True, max_length=70)
    act_fi_color = models.CharField(verbose_name="act_fi_color", null=True, max_length=70)
    act_fi_accesorios = models.CharField(verbose_name="act_fi_accesorios", null=True, max_length=70)
    act_fi_valor_compra = models.CharField(verbose_name="act_fi_valor_compra", null=True, max_length=70)
    act_fi_fecha_compra = models.CharField(verbose_name="act_fi_fecha_compra", null=True, max_length=70)
    act_fi_vida_util = models.CharField(verbose_name="act_fi_vida_util", null=True, max_length=70)
    act_fi_estado = models.CharField(verbose_name="act_fi_estado", null=True, max_length=70)
    act_fi_condicion = models.CharField(verbose_name="act_fi_condicion", null=True, max_length=70)
    act_fi_asignado = models.CharField(verbose_name="act_fi_asignado", null=True, max_length=70)
    act_fi_factura = models.CharField(verbose_name="act_fi_factura", null=True, max_length=70)

class historial_mantenimiento(models.Model):
    opciones = (
        ('Preventivo', 'Preventivo'),
        ('Correctivo', 'Correctivo'),
        ('Dardebaja', 'Dardebaja'),
    )

    opciones2 = (
        ('0 a 30 min', '0 a 30 min'),
        ('31 a 60 min', '31 a 60 min'),
        ('mas de 1 hora', 'mas de 1 hora'),
    )

    id_ficha_mantenimiento = models.ForeignKey('ficha_mantenimiento', on_delete=models.CASCADE, verbose_name="ficha_mantenimiento")
    tipo_mantenimiento = models.CharField(verbose_name="Tipo Mantenimiento", choices=opciones,max_length=20,null=True)
    observaciones = models.CharField(verbose_name="observaciones", null=True, max_length=300)
    fecha_mantenimiento = models.CharField(verbose_name="Fecha Solicitud",null=True)
    funcionario_encargado = models.CharField(verbose_name="Funcionario", null=True, max_length=70)
    piezas_reemplazadas = models.TextField(verbose_name="piezas_reemplazadas", null=True, max_length=300)
    horas_trabajo = models.CharField(verbose_name="Horas de Trabajo", choices=opciones2, max_length=40, null=True)
    recomendaciones = models.TextField(verbose_name="Recomendaciones", null=True, max_length=300)

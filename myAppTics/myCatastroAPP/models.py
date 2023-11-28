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
    asig_identificador= models.CharField(verbose_name="asig_identificador", null=True, max_length=200) # Direccion Iglesia, en el formulario considerar Calle, Canton, Provincia
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
    act_fi_dep_acum = models.CharField(verbose_name="act_fi_dep_acum", null=True, max_length=70)
    act_fi_estado = models.CharField(verbose_name="act_fi_estado", null=True, max_length=70)
    act_fi_dep_periodo = models.CharField(verbose_name="act_fi_dep_periodo", null=True, max_length=70)
    act_fi_cuad_contab = models.CharField(verbose_name="act_fi_cuad_contab", null=True, max_length=70)
    act_fi_cantidad = models.CharField(verbose_name="act_fi_cantidad", null=True, max_length=70)
    act_fi_condicion = models.CharField(verbose_name="act_fi_condicion", null=True, max_length=70)
    act_fi_estCompra = models.CharField(verbose_name="act_fi_estCompra", null=True, max_length=70)
    act_fi_valor_reval = models.CharField(verbose_name="act_fi_valor_reval", null=True, max_length=70)
    act_fi_asignado = models.CharField(verbose_name="act_fi_asignado", null=True, max_length=70)
    act_fi_factura = models.CharField(verbose_name="act_fi_factura", null=True, max_length=70)
    act_fi_capitaliza = models.CharField(verbose_name="act_fi_capitaliza", null=True, max_length=70)
    act_fi_fecha_ingreso = models.CharField(verbose_name="act_fi_fecha_ingreso", null=True, max_length=70)
    act_fi_codigo_mef = models.CharField(verbose_name="act_fi_codigo_mef", null=True, max_length=70)
    asig_fecha = models.CharField(verbose_name="asig_fecha", null=True, max_length=70)
    ent_traspaso = models.CharField(verbose_name="ent_traspaso", null=True, max_length=70)
    det_asig_asignado = models.CharField(verbose_name="det_asig_asignado", null=True, max_length=70)
    det_asig_estado = models.CharField(verbose_name="det_asig_estado", null=True, max_length=70)
    det_asig_observacion = models.CharField(verbose_name="det_asig_observacion", null=True, max_length=70)
    det_asig_valor = models.CharField(verbose_name="det_asig_valor", null=True, max_length=70)


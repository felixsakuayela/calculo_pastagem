from django.db import models

class CalculoPastagem(models.Model):
    peso_amostra_area_tratada = models.FloatField(verbose_name='Peso da Amostra m² em (Kg)', null=True)
    peso_amostra_testemunha = models.FloatField(verbose_name='Peso da Amostra Testemunha (Kg)', null=True)
    perdas_area_tratada = models.FloatField(verbose_name='Perdas 50%', null=True)
    perdas_testemunha = models.FloatField(verbose_name='Perdas Testemunha 50%', null=True)
    eficiencia_pastejo_area_tratada = models.FloatField(verbose_name='Eficiência de Pastejo 50%', null=True)
    eficiencia_pastejo_testemunha = models.FloatField(verbose_name='Eficiência de Pastejo Testemunha 50%', null=True)
    materia_seca_area_tratada = models.FloatField(verbose_name='Matéria Seca 25%', null=True)
    materia_seca_testemunha = models.FloatField(verbose_name='Matéria Seca Testemunha 25%', null=True)
    periodo_ocupacao = models.IntegerField(verbose_name='Período de Ocupação (dias)', null=True)
    numero_piquetes = models.IntegerField(verbose_name='Número de Piquetes', null=True)
    peso_vivo = models.FloatField(verbose_name='Peso Vivo (Kg)', null=True)
    consumo_animal = models.FloatField(verbose_name='Consumo Animal 2,0% PV', null=True)
    ha_area_tratada = models.FloatField(verbose_name='Área Tratada (ha)', null=True)
    ha_testemunha = models.FloatField(verbose_name='Área Testemunha (ha)', null=True)
    gmd_area_tratada = models.FloatField(verbose_name='Área Tratada (GMD)', null=True)
    gmd_testemunha = models.FloatField(verbose_name='Área Testemunha (GMD)', null=True)
    ha_periodo_aguas_area_tratada = models.FloatField(verbose_name='@ ha /período das Águas (Área Tratada)', null=True)
    ha_periodo_aguas_testemunha = models.FloatField(verbose_name='@ ha /período das Águas (Testemunha)', null=True)
    custo = models.FloatField(verbose_name='Custo (R$)', null=True)
    periodo_aguas = models.IntegerField(verbose_name='Período das Águas (Dias)', null=True)

    def __str__(self):
        return f'Cálculo de Pastagem - ID: {self.pk}'
    
class ResultadoCalculo(models.Model):
    cap_sup_area_tratada_1 = models.IntegerField(verbose_name='Cap. Sup. Área Tratada', null=True)
    cap_sup_area_tratada_2 = models.IntegerField(verbose_name='Cap. Sup. Área Tratada', null=True)
    cap_sup_testemunha_1 = models.IntegerField(verbose_name='Cap. Sup. Testemunha', null=True)
    cap_sup_testemunha_2 = models.IntegerField(verbose_name='Cap. Sup. Testemunha', null=True)
    cab_ha_area_tratada = models.FloatField(verbose_name='Capacidade de Suporte (Cab./ha) - Área Tratada', null=True)
    cab_ha_testemunha = models.FloatField(verbose_name='Capacidade de Suporte (Cab./ha) - Testemunha', null=True)
    cab_ha_porcentagem = models.FloatField(verbose_name='Capacidade de Suporte (Cab./ha) - Testemunha', null=True)
    
    ganho_180_dias_area_tratada_valor = models.FloatField(verbose_name='Ganho 180 dias - Área Tratada (R$)', null=True)
    ganho_180_dias_testemunha_valor = models.FloatField(verbose_name='Ganho 180 dias - Testemunha (R$)', null=True)
    ganho_por_ha_porcentagem = models.FloatField(verbose_name='Ganho 180 dias - Testemunha (R$)', null=True)
    diferenca_ganho = models.FloatField(verbose_name='Diferença de Ganho (R$)', null=True)

    def __str__(self):
        return 'Resultado do Cálculo de Pastagem'
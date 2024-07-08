# Generated by Django 4.2.7 on 2024-05-16 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastagem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculopastagem',
            name='consumo_animal',
            field=models.FloatField(null=True, verbose_name='Consumo Animal 2,0% PV'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='eficiencia_pastejo_area_tratada',
            field=models.FloatField(null=True, verbose_name='Eficiência de Pastejo 50%'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='eficiencia_pastejo_testemunha',
            field=models.FloatField(null=True, verbose_name='Eficiência de Pastejo Testemunha 50%'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='gmd_area_tratada',
            field=models.FloatField(null=True, verbose_name='Área Tratada (GMD)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='gmd_testemunha',
            field=models.FloatField(null=True, verbose_name='Área Testemunha (GMD)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='ha_area_tratada',
            field=models.FloatField(null=True, verbose_name='Área Tratada (ha)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='ha_periodo_aguas_area_tratada',
            field=models.FloatField(null=True, verbose_name='@ ha /período das Águas (Área Tratada)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='ha_periodo_aguas_testemunha',
            field=models.FloatField(null=True, verbose_name='@ ha /período das Águas (Testemunha)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='ha_testemunha',
            field=models.FloatField(null=True, verbose_name='Área Testemunha (ha)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='materia_seca_area_tratada',
            field=models.FloatField(null=True, verbose_name='Matéria Seca 25%'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='materia_seca_testemunha',
            field=models.FloatField(null=True, verbose_name='Matéria Seca Testemunha 25%'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='perdas_area_tratada',
            field=models.FloatField(null=True, verbose_name='Perdas 50%'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='perdas_testemunha',
            field=models.FloatField(null=True, verbose_name='Perdas Testemunha 50%'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='periodo_aguas',
            field=models.IntegerField(null=True, verbose_name='Período das Águas (Dias)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='periodo_ocupacao',
            field=models.IntegerField(null=True, verbose_name='Período de Ocupação (dias)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='peso_amostra_area_tratada',
            field=models.FloatField(null=True, verbose_name='Peso da Amostra m² em (Kg)'),
        ),
        migrations.AlterField(
            model_name='calculopastagem',
            name='peso_amostra_testemunha',
            field=models.FloatField(null=True, verbose_name='Peso da Amostra Testemunha (Kg)'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='cab_ha_area_tratada',
            field=models.FloatField(null=True, verbose_name='Capacidade de Suporte (Cab./ha) - Área Tratada'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='cab_ha_porcentagem',
            field=models.FloatField(null=True, verbose_name='Capacidade de Suporte (Cab./ha) - Testemunha'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='cab_ha_testemunha',
            field=models.FloatField(null=True, verbose_name='Capacidade de Suporte (Cab./ha) - Testemunha'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='cap_sup_area_tratada_1',
            field=models.IntegerField(null=True, verbose_name='Cap. Sup. Área Tratada'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='cap_sup_area_tratada_2',
            field=models.IntegerField(null=True, verbose_name='Cap. Sup. Área Tratada'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='cap_sup_testemunha_1',
            field=models.IntegerField(null=True, verbose_name='Cap. Sup. Testemunha'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='cap_sup_testemunha_2',
            field=models.IntegerField(null=True, verbose_name='Cap. Sup. Testemunha'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='diferenca_ganho',
            field=models.FloatField(null=True, verbose_name='Diferença de Ganho (R$)'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='ganho_180_dias_area_tratada_valor',
            field=models.FloatField(null=True, verbose_name='Ganho 180 dias - Área Tratada (R$)'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='ganho_180_dias_testemunha_valor',
            field=models.FloatField(null=True, verbose_name='Ganho 180 dias - Testemunha (R$)'),
        ),
        migrations.AlterField(
            model_name='resultadocalculo',
            name='ganho_por_ha_porcentagem',
            field=models.FloatField(null=True, verbose_name='Ganho 180 dias - Testemunha (R$)'),
        ),
    ]

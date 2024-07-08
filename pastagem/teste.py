from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def calculo(request):

    if request.method == 'POST':

        peso_amostra_area_tratada = float(request.POST['peso_amostra_area_tratada'])
        peso_amostra_testemunha = float(request.POST['peso_amostra_testemunha'])
        perdas_area_tratada = float(request.POST['perdas_area_tratada'])
        perdas_testemunha = float(request.POST['perdas_testemunha'])
        eficiencia_pastejo_area_tratada = float(request.POST['eficiencia_pastejo_area_tratada'])
        eficiencia_pastejo_testemunha = float(request.POST['eficiencia_pastejo_testemunha'])
        materia_seca_area_tratada = float(request.POST['materia_seca_area_tratada'])
        materia_seca_testemunha = float(request.POST['materia_seca_testemunha'])
        periodo_ocupacao = int(request.POST['periodo_ocupacao'])
        numero_piquetes = int(request.POST['numero_piquetes'])
        peso_vivo = float(request.POST['peso_vivo'])
        consumo_animal = float(request.POST['consumo_animal'])
        ha_area_tratada = float(request.POST['ha_area_tratada'])
        ha_testemunha = float(request.POST['ha_testemunha'])
        gmd_area_tratada = float(request.POST['gmd_area_tratada'])
        gmd_testemunha = float(request.POST['gmd_testemunha'])
        ha_periodo_aguas_area_tratada = float(request.POST['ha_periodo_aguas_area_tratada'])
        ha_periodo_aguas_testemunha = float(request.POST['ha_periodo_aguas_testemunha'])
        custo = float(request.POST['custo'])
        periodo_aguas = int(request.POST['periodo_aguas'])

        # Realizar cálculos com os dados recebidos
        cap_sup_area_tratada_1 = (peso_amostra_area_tratada *
                                    perdas_area_tratada *
                                    eficiencia_pastejo_area_tratada *
                                    materia_seca_area_tratada *
                                    ha_area_tratada)

        cap_sup_area_tratada_2 = (periodo_ocupacao *
                                    (peso_vivo * consumo_animal))

        cap_sup_testemunha_1 = (peso_amostra_testemunha *
                                    perdas_testemunha *
                                    eficiencia_pastejo_testemunha *
                                    materia_seca_testemunha *
                                    ha_testemunha)

        cap_sup_testemunha_2 = (periodo_ocupacao *
                                    (peso_vivo * consumo_animal))

        cab_ha_area_tratada = ((cap_sup_area_tratada_1 / cap_sup_area_tratada_2) /
                                numero_piquetes)

        cab_ha_testemunha = ((cap_sup_testemunha_1 / cap_sup_testemunha_2) /
                                numero_piquetes)

        cab_ha_porcentagem = 1 - (cab_ha_testemunha / cab_ha_area_tratada)

        ganho_180_dias_area_tratada_valor = (ha_periodo_aguas_area_tratada *
                                                custo)

        ganho_180_dias_testemunha_valor = (ha_periodo_aguas_testemunha *
                                            custo)

        ganho_por_ha_porcentagem = ganho_180_dias_area_tratada_valor - ganho_180_dias_testemunha_valor

        diferenca_ganho = ganho_180_dias_testemunha_valor - ganho_180_dias_area_tratada_valor

        # Passando os resultados calculados para o template
        context = {
            'cap_sup_area_tratada_1': cap_sup_area_tratada_1,
            'cap_sup_area_tratada_2': cap_sup_area_tratada_2,
            'cap_sup_testemunha_1': cap_sup_testemunha_1,
            'cap_sup_testemunha_2': cap_sup_testemunha_2,
            'cab_ha_area_tratada': cab_ha_area_tratada,
            'cab_ha_testemunha': cab_ha_testemunha,
            'cab_ha_porcentagem': cab_ha_porcentagem,
            'ganho_180_dias_area_tratada_valor': ganho_180_dias_area_tratada_valor,
            'ganho_180_dias_testemunha_valor': ganho_180_dias_testemunha_valor,
            'ganho_por_ha_porcentagem': ganho_por_ha_porcentagem,
            'diferenca_ganho': diferenca_ganho
        }

        return render(request, 'resultado.html', context)
    
    return render(request, 'calculo.html')
from django.shortcuts import render, redirect
from .models import CalculoPastagem, ResultadoCalculo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def calculo(request):
    if request.method == 'POST':
        peso_amostra_area_tratada = float(request.POST['peso_amostra_area_tratada'])
        peso_amostra_testemunha = float(request.POST['peso_amostra_testemunha'])
        result = (peso_amostra_area_tratada + peso_amostra_testemunha) / 2

        return render(request, 'resultado.html', {'peso_amostra_area_tratada': peso_amostra_area_tratada, 'peso_amostra_testemunha': peso_amostra_testemunha, 'ha_testemunha': result})
        
    """pastagemcalculo = CalculoPastagem.objects.create(peso_amostra_area_tratada=peso_amostra_area_tratada, peso_amostra_testemunha=peso_amostra_testemunha, ha_testemunha=result)
        return redirect('pastagens_calculadas', pk=pastagemcalculo.pk)
    else:"""
    return render(request, 'calculo.html')

def pastagens_calculadas(request, pk):
    pastagemcalculo = CalculoPastagem.objects.get(pk=pk)
    return render(request, 'resultado.html', {'pastagemcalculo': pastagemcalculo})

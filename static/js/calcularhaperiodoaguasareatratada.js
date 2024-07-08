// Função para calcular o valor de ha_periodo_aguas_area_tratada
function calcularHaPeriodoAguasAreaTratada() {
    // Obter os valores dos campos do formulário
    const gmdAreaTratada = parseFloat(document.querySelector('select[name="gmd_area_tratada"]').value);
    const periodoAguas = parseFloat(document.querySelector('input[name="periodo_aguas"]').value);
    const pesoAmostraAreaTratada = parseFloat(document.querySelector('input[name="peso_amostra_area_tratada"]').value);
    const perdasAreaTratada = parseFloat(document.querySelector('input[name="perdas_area_tratada"]').value);
    const eficienciaPastejoAreaTratada = parseFloat(document.querySelector('input[name="eficiencia_pastejo_area_tratada"]').value);
    const materiaSecaAreaTratada = parseFloat(document.querySelector('input[name="materia_seca_area_tratada"]').value);
    const haAreaTratada = parseFloat(document.querySelector('input[name="ha_area_tratada"]').value);
    const periodoOcupacao = parseFloat(document.querySelector('input[name="periodo_ocupacao"]').value);
    const pesoVivo = parseFloat(document.querySelector('input[name="peso_vivo"]').value);
    const consumoAnimal = parseFloat(document.querySelector('input[name="consumo_animal"]').value);
    const numeroPiquetes = parseFloat(document.querySelector('input[name="numero_piquetes"]').value);

    // Calcular ha_periodo_aguas_area_tratada de acordo com a fórmula corrigida
    const haPeriodoAguasAreaTratada = ((gmdAreaTratada * periodoAguas) / 30) * (
        (pesoAmostraAreaTratada * perdasAreaTratada * eficienciaPastejoAreaTratada * materiaSecaAreaTratada * haAreaTratada) /
        (periodoOcupacao * (pesoVivo * consumoAnimal) / 100 * numeroPiquetes)
    );

    // Dividir o resultado por 100 para obter o formato "28,0"
    const haPeriodoAguasAreaTratadaFormatado = (haPeriodoAguasAreaTratada / 100).toFixed(1); // Arredondar para 1 casa decimal

    // Definir o valor calculado no campo ha_periodo_aguas_area_tratada
    document.querySelector('input[name="ha_periodo_aguas_area_tratada"]').value = haPeriodoAguasAreaTratadaFormatado;
}

// Chamar a função de cálculo sempre que um dos campos relevantes mudar
document.querySelector('select[name="gmd_area_tratada"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="periodo_aguas"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="peso_amostra_area_tratada"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="perdas_area_tratada"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="eficiencia_pastejo_area_tratada"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="materia_seca_area_tratada"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="ha_area_tratada"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="periodo_ocupacao"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="peso_vivo"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="consumo_animal"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
document.querySelector('input[name="numero_piquetes"]').addEventListener('change', calcularHaPeriodoAguasAreaTratada);
// Função para calcular o valor de ha_periodo_aguas_testemunha
function calcularHaPeriodoAguasTestemunha() {
    // Obter os valores dos campos do formulário
    const gmdTestemunha = parseFloat(document.querySelector('select[name="gmd_testemunha"]').value);
    const periodoAguas = parseFloat(document.querySelector('input[name="periodo_aguas"]').value);
    const pesoAmostraTestemunha = parseFloat(document.querySelector('input[name="peso_amostra_testemunha"]').value);
    const perdasTestemunha = parseFloat(document.querySelector('input[name="perdas_testemunha"]').value);
    const eficienciaPastejoTestemunha = parseFloat(document.querySelector('input[name="eficiencia_pastejo_testemunha"]').value);
    const materiaSecaTestemunha = parseFloat(document.querySelector('input[name="materia_seca_testemunha"]').value);
    const haTestemunha = parseFloat(document.querySelector('input[name="ha_testemunha"]').value);
    const periodoOcupacao = parseFloat(document.querySelector('input[name="periodo_ocupacao"]').value);
    const pesoVivo = parseFloat(document.querySelector('input[name="peso_vivo"]').value);
    const consumoAnimal = parseFloat(document.querySelector('input[name="consumo_animal"]').value);
    const numeroPiquetes = parseFloat(document.querySelector('input[name="numero_piquetes"]').value);

    // Calcular ha_periodo_aguas_testemunha de acordo com a fórmula fornecida
    const haPeriodoAguasTestemunha = ((gmdTestemunha * periodoAguas) / 30) * (
        (pesoAmostraTestemunha * perdasTestemunha * eficienciaPastejoTestemunha * materiaSecaTestemunha * haTestemunha) /
        (periodoOcupacao * (pesoVivo * consumoAnimal / 100) * numeroPiquetes)
    );

    // Dividir o resultado por 100 para obter o formato "17,1"
    const haPeriodoAguasTestemunhaFormatado = (haPeriodoAguasTestemunha / 100).toFixed(1); // Arredondar para 1 casa decimal

    // Definir o valor calculado no campo ha_periodo_aguas_testemunha
    document.querySelector('input[name="ha_periodo_aguas_testemunha"]').value = haPeriodoAguasTestemunhaFormatado;
}

// Chamar a função de cálculo sempre que um dos campos relevantes mudar
document.querySelector('select[name="gmd_testemunha"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="periodo_aguas"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="peso_amostra_testemunha"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="perdas_testemunha"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="eficiencia_pastejo_testemunha"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="materia_seca_testemunha"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="ha_testemunha"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="periodo_ocupacao"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="peso_vivo"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="consumo_animal"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);
document.querySelector('input[name="numero_piquetes"]').addEventListener('change', calcularHaPeriodoAguasTestemunha);

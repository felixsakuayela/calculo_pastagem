function updatePeriodo() {
    const periodoInput = document.getElementById('periodo_ocupacao');
    const piquetesInput = document.getElementById('numero_piquetes');
    
    const periodoValue = parseInt(periodoInput.value);
    const piquetesValue = parseInt(piquetesInput.value);
    
    if (piquetesValue === 1) {
        periodoInput.value = 45;
    } else if (piquetesValue === 2) {
        periodoInput.value = 30;
    } else if (piquetesValue === 3) {
        periodoInput.value = 15;
    } else if (piquetesValue === 4) {
        periodoInput.value = 10;
    } else if (piquetesValue === 5) {
        periodoInput.value = 8;
    } else if (piquetesValue === 6) {
        periodoInput.value = 6;
    } else {
        // Inserir um comportamento padrão se o valor de piquetes for diferente dos casos acima
        // Por exemplo, poderia mostrar uma mensagem de erro ou comportamento alternativo.
        console.log('Número de piquetes não reconhecido.');
    }
}
// Seleciona o elemento de input pelo ID
const numeroPiquetesInput = document.getElementById('numero_piquetes');

// Adiciona um ouvinte de evento de input para monitorar alterações no valor do input
numeroPiquetesInput.addEventListener('input', function() {
  let numeroPiquetes = parseInt(numeroPiquetesInput.value);

  // Verifica se o valor está fora do intervalo permitido (1 a 6)
  if (numeroPiquetes < 1 || isNaN(numeroPiquetes)) {
    numeroPiquetes = 1;  // Se for menor que 1 ou NaN, ajusta para 1
  } else if (numeroPiquetes > 6) {
    numeroPiquetes = 6;  // Se for maior que 6, ajusta para 6
  }

  // Atualiza o valor no campo de entrada
  numeroPiquetesInput.value = numeroPiquetes;
});
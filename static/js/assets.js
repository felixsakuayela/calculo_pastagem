// Obtém uma referência para o botão de calcular
const calcularBtn = document.getElementById("calcular-btn");

// Adiciona um ouvinte de evento de clique ao botão
calcularBtn.addEventListener("click", function() {
  // Redireciona para a página de resultado
  window.location.href = "resultado.html";
});

document.getElementById('calcularBtn').addEventListener('click', function() {
  // Exibe o container de resultados
  var resultadoContainer = document.getElementById('resultadoContainer');
  resultadoContainer.classList.remove('hidden');
  resultadoContainer.scrollIntoView({ behavior: 'smooth' });
});



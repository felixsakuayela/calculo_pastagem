document.getElementById('save-pdf').addEventListener('click', function () {
    // Seleciona o elemento que será salvo como PDF. Use 'document.body' para salvar a página inteira.
    const element = document.body;

    // Configurações para o PDF
    const options = {
        margin:       0.5,             // Margem em polegadas
        filename:     'pagina.pdf',    // Nome do arquivo PDF
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },    // Escala para a conversão
        jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
    };

    // Gera PDF
    html2pdf().from(element).set(options).save();
});

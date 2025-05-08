function toggleOptions(optionId) {
    const checkbox = document.getElementById(optionId);
    const optionsContainer = document.getElementById('optionsContainer');

    // Mostrar las opciones si al menos un checkbox está seleccionado
    const checkboxes = document.querySelectorAll('.form-check-input');
    const isAnyChecked = Array.from(checkboxes).some(cb => cb.checked);

    optionsContainer.style.display = isAnyChecked ? 'block' : 'none';
}

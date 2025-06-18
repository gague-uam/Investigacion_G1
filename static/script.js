async function ordenar() {
    const algoritmo = document.getElementById('algoritmo').value;
    const arrayInput = document.getElementById('array').value;
    const resultadoElem = document.getElementById('resultado');

    try {
        const arr = arrayInput.split(',').map(num => parseFloat(num.trim()));
        if (arr.some(isNaN)) {
            resultadoElem.textContent = "Por favor, ingrese solo números separados por coma.";
            return;
        }

        const response = await fetch('/ordenar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ algoritmo, arr })
        });

        if (!response.ok) {
            const error = await response.json();
            resultadoElem.textContent = error.error || "Ocurrió un error al ordenar.";
            return;
        }

        const data = await response.json();
        resultadoElem.textContent = `Resultado ordenado: ${data.sorted_array.join(', ')}`;
    } catch (error) {
        resultadoElem.textContent = "Error en la comunicación con el servidor.";
        console.error(error);
    }
}

import flet as ft

# --- Radix Sort adaptado para números negativos ---
def radix_sort_with_negatives(arr):
    if not arr:
        return []

    negatives = [-x for x in arr if x < 0]  # Convertimos a positivos temporalmente
    positives = [x for x in arr if x >= 0]

    radix_sort(negatives)
    radix_sort(positives)

    # Revertimos el orden de negativos porque se ordenaron al revés
    negatives = [-x for x in reversed(negatives)]
    return negatives + positives

# --- Radix Sort base (solo para no negativos) ---
def radix_sort(arr):
    if not arr:
        return []

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# --- Counting Sort (estable) usado dentro de Radix Sort ---
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Solo dígitos del 0 al 9

    # Contamos ocurrencias del dígito en la posición actual
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    # Sumamos posiciones acumuladas
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construimos el array de salida estable
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

# --- INTERFAZ VISUAL CON FLET ---
def main(page: ft.Page):
    page.title = "Radix Sort Visual (con negativos)"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campo de entrada
    input_field = ft.TextField(
        label="Introduce números separados por coma",
        hint_text="Ej: -50, 45, -5, 0, 100",
        width=500,
        filled=True,
        border_radius=10
    )

    output_text = ft.Text(size=16, selectable=True)
    explanation = ft.Text(size=14, color=ft.Colors.BLUE_GREY)

    # Función cuando se hace clic en "Ordenar"
    def ordenar_click(e):
        try:
            raw_input = input_field.value.strip()
            numbers = [int(x.strip()) for x in raw_input.split(",") if x.strip()]
            ordenado = radix_sort_with_negatives(numbers)

            output_text.value = f"🔢 Resultado ordenado: {ordenado}"
            explanation.value = (
                "📘 Radix Sort ordena los números por dígitos:\n"
                "→ Primero separa negativos y positivos.\n"
                "→ Ordena cada grupo por dígitos (de derecha a izquierda).\n"
                "→ Reinvierte los negativos y combina todo ordenado.\n\n"
                "✨ Ideal para muchos enteros pequeños/medianos."
            )
        except Exception as err:
            output_text.value = f"❌ Error: {err}"
            explanation.value = ""

        page.update()

    # Botón para ordenar
    ordenar_boton = ft.ElevatedButton(
        text="Ordenar con Radix Sort",
        icon=ft.Icons.SORT,
        on_click=ordenar_click,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), padding=20)
    )

    # Layout general
    page.add(
        ft.Column([
            ft.Text("⚙️ Visualizador de Radix Sort", size=24, weight="bold"),
            input_field,
            ordenar_boton,
            ft.Divider(),
            output_text,
            ft.Divider(),
            explanation
        ])
    )

ft.app(target=main)

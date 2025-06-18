import flet as ft

# Función de ordenamiento por inserción
def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

# Función principal de la app
def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Gestor de Elementos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Campo de texto para ingresar nuevos elementos
    input_text = ft.TextField(
        label="Agregar nuevo elemento",
        hint_text="Escribe aquí...",
        width=400,
        filled=True,
        bgcolor=ft.Colors.AMBER_50,
        border_radius=10
    )

    # Lista visual de elementos (tarjetas)
    items_list = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    # Mensaje para mostrar errores o información
    mensaje = ft.Text("", color=ft.Colors.RED, size=14)

    # Función para insertar un nuevo elemento
    def insertar_click(e):
        texto = input_text.value.strip()
        # Validar que no esté vacío
        if not texto:
            mensaje.value = "El campo no puede estar vacío."
            page.update()
            return
        # Validar que no sea duplicado
        existentes = [item.content.content.value for item in items_list.controls]
        if texto in existentes:
            mensaje.value = "El elemento ya existe en la lista."
            page.update()
            return
        # Si pasa validaciones, agregar
        nuevo_item = ft.Card(
            content=ft.Container(
                content=ft.Text(texto, size=16),
                padding=15,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                ink=True
            ),
            elevation=3
        )
        items_list.controls.append(nuevo_item)
        input_text.value = ""
        mensaje.value = ""
        page.update()

    # Función para ordenar los elementos usando insertion_sort
    def ordenar_click(e):
        # Extrae los textos de los items
        textos = [item.content.content.value for item in items_list.controls]
        # Ordena usando insertion_sort
        textos_ordenados = insertion_sort(textos)
        # Limpia y vuelve a agregar los items ordenados
        items_list.controls.clear()
        for texto in textos_ordenados:
            nuevo_item = ft.Card(
                content=ft.Container(
                    content=ft.Text(texto, size=16),
                    padding=15,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    ink=True
                ),
                elevation=3
            )
            items_list.controls.append(nuevo_item)
        page.update()

    # Botón para insertar elementos
    boton_insertar = ft.ElevatedButton(
        text="Insertar",
        icon=ft.Icons.ADD,
        on_click=insertar_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20
        )
    )

    # Botón para ordenar elementos
    boton_ordenar = ft.ElevatedButton(
        text="Ordenar",
        icon=ft.Icons.SORT,
        on_click=ordenar_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20
        )
    )

    # Estructura visual de la página
    page.add(
        ft.Column([
            ft.Text("📋 Lista de Elementos", size=28, weight="bold"),
            ft.Row([input_text, boton_insertar, boton_ordenar], spacing=10),
            mensaje,  # Aquí se muestra el mensaje de validación
            ft.Divider(),
            ft.Container(content=items_list, height=400, expand=True, border_radius=10, bgcolor=ft.Colors.GREY_100, padding=10)
        ])
    )

# Inicia la aplicación Flet
ft.app(target=main)
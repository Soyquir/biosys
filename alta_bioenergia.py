import flet as ft
import airtable as at
import principal as pri

def main(page: ft.Page):
    
    def guardar_bio(e: ft.ControlEvent):
        cultivo = txt_cultivo.value
        parte = txt_parte.value
        municipio = select_municipio.value if select_municipio.value else ""

        if cultivo == "":
            page.open(ft.SnackBar(ft.Text("Introduce el nombre del cultivo")))
            return
        if parte == "":
            page.open(ft.SnackBar(ft.Text("Introduce la parte del cultivo")))
            return

        try:
            cantidad = float(txt_cantidad.value)
            area = float(txt_area.value)
            energia = float(txt_energia.value)
        except ValueError:
            page.open(ft.SnackBar(ft.Text("Introduce valores numéricos válidos")))
            return

        if municipio == "":
            page.open(ft.SnackBar(ft.Text("Selecciona un municipio")))
            return

        try:
            latitud = float(txt_latitud.value)
            longitud = float(txt_longitud.value)
        except ValueError:
            page.open(ft.SnackBar(ft.Text("Introduce valores numéricos válidos")))
            return

        nueva_bio = at.Bioenergia(
            cultivo=cultivo,
            parte=parte,
            cantidad=cantidad,
            area=area,
            energia=energia,
            municipio=municipio,
            latitud=latitud,
            longitud=longitud
        )

        try:
            nueva_bio.save()
            page.open(ft.SnackBar(ft.Text("Cultivo registrado exitosamente")))
        except Exception as error:
            page.open(ft.SnackBar(ft.Text(str(error))))

    # Configuración de la página
    page.title = "Registro de Bioenergía"
    page.theme_mode = "light"
    page.window_width = 700
    page.window_height = 700

    page.appbar = ft.AppBar(
        title=ft.Text("Nueva Bioenergía"),
        center_title=True,
        leading=ft.Icon("assignment"),
        bgcolor="blue",
        color="white"
    )

    
    txt_cultivo = ft.TextField(label="Cultivo", width=400)
    txt_parte = ft.TextField(label="Parte del cultivo", width=400)
    txt_cantidad = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER, width=400)
    txt_area = ft.TextField(label="Área", keyboard_type=ft.KeyboardType.NUMBER, width=400)
    txt_energia = ft.TextField(label="Energía generada", keyboard_type=ft.KeyboardType.NUMBER, width=400)
    select_municipio = ft.Dropdown(
        label="Municipio",
        width=400,
        options=[ft.dropdown.Option(m) for m in [
            "Balancán", "Cárdenas", "Centla", "Centro", "Comalcalco",
            "Cunduacán", "Emiliano Zapata", "Huimanguillo", "Jalapa",
            "Jalpa de Méndez", "Jonuta", "Macuspana", "Nacajuca",
            "Paraíso", "Tacotalpa", "Teapa", "Tenosique"
        ]]
    )
    txt_latitud = ft.TextField(label="Latitud", keyboard_type=ft.KeyboardType.NUMBER, width=400)
    txt_longitud = ft.TextField(label="Longitud", keyboard_type=ft.KeyboardType.NUMBER, width=400)

    btn_guardar = ft.FilledButton(text="Guardar", icon="check", on_click=guardar_bio, bgcolor="blue", color="white")
    btn_cancelar = ft.FilledButton(text="Cancelar", icon="close", bgcolor="grey", color="white")

    fila_botones = ft.Row(
        controls=[btn_guardar, btn_cancelar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
        width=400
    )

    def volver(e):
        page.floating_action_button = None
        page.floating_action_button_location = None
        page.update()
        page.clean()
        pri.main(page)


    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ARROW_BACK,
        focus_color="black",
        on_click=volver
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.END_FLOAT


    formulario = ft.Column(
        controls=[
            txt_cultivo,
            txt_parte,
            txt_cantidad,
            txt_area,
            txt_energia,
            select_municipio,
            txt_latitud,
            txt_longitud,
            fila_botones
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        width=400  
    )
    
    page.add(
        ft.Row(
            controls=[formulario],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

    page.update()

if __name__ == "__main__":
    ft.app(target=main)

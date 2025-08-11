import flet as ft
import airtable as at
import principal as pri

def main(page: ft.Page):
    page.title = "Consulta de Bioenergías"
    page.theme_mode = "light"
    page.window_width = 900
    page.window_height = 800
    page.vertical_alignment = "start"       
    page.horizontal_alignment = "center"    

    page.appbar = ft.AppBar(
        title=ft.Text("Consulta de Bioenergías"),
        center_title=True,
        leading=ft.Icon("eco"),
        bgcolor="green",
        color="white"
    )

    # Encabezados de la tabla
    encabezados = [
        ft.DataColumn(ft.Text("Cultivo")),
        ft.DataColumn(ft.Text("Parte")),
        ft.DataColumn(ft.Text("Cantidad")),
        ft.DataColumn(ft.Text("Área")),
        ft.DataColumn(ft.Text("Energía")),
        ft.DataColumn(ft.Text("Municipio")),
        ft.DataColumn(ft.Text("Latitud")),
        ft.DataColumn(ft.Text("Longitud")),
    ]

    # Filas
    filas = []
    datos = at.Bioenergia.all()
    for d in datos:
        fila = ft.DataRow([
            ft.DataCell(ft.Text(d.cultivo)),
            ft.DataCell(ft.Text(d.parte)),
            ft.DataCell(ft.Text(str(d.cantidad))),
            ft.DataCell(ft.Text(str(d.area))),
            ft.DataCell(ft.Text(str(d.energia))),
            ft.DataCell(ft.Text(d.municipio)),
            ft.DataCell(ft.Text(str(d.latitud))),
            ft.DataCell(ft.Text(str(d.longitud))),
        ])
        filas.append(fila)

    tabla_bio = ft.DataTable(columns=encabezados, rows=filas)

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

    page.add(
        ft.Column(
            controls=[tabla_bio],
            alignment="start",               
            horizontal_alignment="center"    
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

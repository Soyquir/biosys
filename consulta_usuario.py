import flet as ft
import airtable as at
import principal as pri

def main(page: ft.Page):
    page.title = "Consultas"
    page.theme_mode = "light"
    page.window_width = 600
    page.window_height = 800

    page.appbar = ft.AppBar(
        title=ft.Text("Consultas en la nube"),
        center_title=True,
        leading=ft.Icon("cloud"),
        bgcolor="blue",
        color="white"
    )

    encabezados = [
        ft.DataColumn(ft.Text("Clave")),
        ft.DataColumn(ft.Text("Contraseña")),
        ft.DataColumn(ft.Text("Nombre completo")),
        ft.DataColumn(ft.Text("Es administrador")),
    ]

    filas = []
    datos = at.Usuario.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.clave))
        celda2 = ft.DataCell(ft.Text(d.contra, color="white"))
        celda3 = ft.DataCell(ft.Text(d.nombre))
        celda4 = ft.DataCell(ft.Text(str(d.admin)))  
        fila = ft.DataRow([celda1, celda2, celda3, celda4])
        filas.append(fila)

    
    tbl_usuarios = ft.DataTable(columns=encabezados, rows=filas)

    
    scroll_area = ft.Container(
        content=tbl_usuarios,
        expand=True,
        alignment=ft.alignment.top_center,
        bgcolor="lightgrey",
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


    page.add(
        ft.Column(
            [
                scroll_area
            ],
            expand=True,
            scroll=ft.ScrollMode.ALWAYS
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

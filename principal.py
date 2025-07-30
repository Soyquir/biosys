import flet as ft
def main (page:ft.Page):

    def mostrar_registro(e:ft.ControlEvent ):
        page.clean()
        
    page.title="menu principal"
    page.theme_mode="light"
    page.appbar=ft.AppBar(
        title=ft.Text ("SISTEMA DE GESTION DE ENERGIAS"),
        leading=ft.Icon("energy_savings_leaf"),
        color="white",
        bgcolor="purple"
    )

    btn_registro=ft.ElevatedButton("registro")
    btn_consultas=ft.ElevatedButton("consultas")
    page.add(btn_registro,btn_consultas)
    page.update()
ft.app(target=main)
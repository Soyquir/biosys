import flet as ft
import alta_usuario as al
import consulta_usuario as cu
import alta_bioenergia as alb
import consulta_bio as cbio

def main(page: ft.Page):
    
    def mostrar_registro(e):
        page.clean()
        al.main(page)

    def consultar_usuario(e):
        page.clean()
        cu.main(page)

    def agregar_bioenergia(e):
        page.clean()
        alb.main(page)

    def consultar_bioenergia(e):
        page.clean()
        cbio.main(page)

    # Configuración de la página
    page.title = "Menú principal"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        title=ft.Text("Sistema de gestión de bioenergías", size=20, weight="bold"),
        leading=ft.Icon(ft.Icons.ENERGY_SAVINGS_LEAF),
        color="white",
        bgcolor=ft.Colors.GREEN_800 
    )

    btn_registro = ft.ElevatedButton(
        "Registro de usuario",
        icon=ft.Icons.PERSON_ADD,
        bgcolor=ft.Colors.LIGHT_GREEN_500, 
        color="white",
        style=ft.ButtonStyle(padding=20),
        on_click=mostrar_registro
    )
    btn_consultas = ft.ElevatedButton(
        "Consulta de usuario",
        icon=ft.Icons.SEARCH,
        bgcolor=ft.Colors.CYAN_500,
        color="white",
        style=ft.ButtonStyle(padding=20),
        on_click=consultar_usuario
    )
    btn_nueva = ft.ElevatedButton(
        "Registro de bioenergía",
        icon=ft.Icons.ADD_CIRCLE,
        bgcolor=ft.Colors.AMBER_500,
        color="white",
        style=ft.ButtonStyle(padding=20),
        on_click=agregar_bioenergia
    )
    btn_bionergia = ft.ElevatedButton(
        "Consulta de bioenergía",
        icon=ft.Icons.LIST_ALT,
        bgcolor=ft.Colors.DEEP_PURPLE_500,
        color="white",
        style=ft.ButtonStyle(padding=20),
        on_click=consultar_bioenergia
    )

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Menú Principal", size=30, weight="bold", color="Green"),
                    ft.Divider(height=20, thickness=2, color="Green"),
                    btn_registro,
                    btn_consultas,
                    btn_nueva,
                    btn_bionergia
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            padding=50,
            expand=True
        )
    )

# Iniciar app
if __name__ == "__main__":
    ft.app(target=main)

import flet as ft  
from airtable import Usuario as Usuario 
import principal as pr
from pyairtable.formulas import match

Usuario.api_key = "pat81Apk92CVnEQlf.54197eabffa1531e1f94835d5f6f006b2f3e6ea593ed4cd4ce109f9adc9dbdc4"
Usuario.base_id = "appFRo8CEre58zIr5"
Usuario.table_name = "USUARIO"

def main(page: ft.Page):
    def ingresar(e: ft.ControlEvent):
        usuario_valor = txt_usuario.value.strip()
        password_valor = txt_contraseña.value.strip()
        try:
            formula = match({"clave": usuario_valor, "contra": password_valor})
            registro = Usuario.first(formula=formula)
            if registro:
                print("¡Funciona!")
                page.clean()
                pr.main(page)  
            else:
                page.snack_bar = ft.SnackBar(ft.Text(f"Usuario '{usuario_valor}' no encontrado."), bgcolor="red", open=True)
                page.update()
        except Exception as error:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error de Airtable: {error}"), bgcolor="red", open=True)
            page.update()

    # Configuración de la página
    page.theme_mode = "light"
    page.title = "Inicio de Sesión"
    page.window_width = 400
    page.window_height = 550
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.appbar = ft.AppBar(
    title=ft.Text("Inicio de Sesión", size=20, weight="bold"),
    center_title=True,
    bgcolor=ft.Colors.BLUE_GREY,
    color="white",
    )


    # Componentes
    logo = ft.Icon(name=ft.Icons.PERSON, size=120, color="Blue")
    txt_bienvenido = ft.Text("Bienvenido", size=32, weight="bold", color="Grey")
    txt_usuario = ft.TextField(label="Usuario o correo", width=320, autofocus=True)
    txt_contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=320)
    btn_login = ft.FilledButton(
        text="Iniciar Sesión",
        icon=ft.Icons.LOGIN,
        width=320,
        bgcolor=ft.Colors.BLUE_GREY_500,
        color="white",
        on_click=ingresar,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.symmetric(horizontal=20, vertical=15)
        )
    )

    container = ft.Container(
        content=ft.Column(
            controls=[
                logo,
                txt_bienvenido,
                txt_usuario,
                txt_contraseña,
                btn_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            width=340,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        expand=True,
        padding=20,
    )

    page.add(container)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

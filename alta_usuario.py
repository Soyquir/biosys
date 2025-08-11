import flet as ft 
import airtable as at
import main as ma

def main(page: ft.Page):

    def guardar_usuario(e: ft.ControlEvent):
        clave = txt_clave.value
        contra = txt_contra.value
        contra2 = txt_contra2.value
        nombre = txt_nombre.value

        if clave == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu clave de usuario"), bgcolor="orange", show_close_icon=True))
            return

        if contra == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu contraseña"), bgcolor="yellow", show_close_icon=True))
            return    

        if nombre == "":
            page.open(ft.SnackBar(ft.Text("Escribe tu nombre"), bgcolor="red", show_close_icon=True))
            return

        if contra != contra2:
            page.open(ft.SnackBar(ft.Text("Contraseña incorrecta"), bgcolor="red", show_close_icon=True))
            return

        nuevo = at.Usuario(
            clave=clave,
            contra=contra,
            nombre=nombre,
            admin=chk_admin.value
        )
        try:
            nuevo.save()
            page.open(ft.SnackBar(ft.Text("Usuario registrado"), bgcolor="blue", show_close_icon=True))
        except Exception as error:
            page.open(ft.SnackBar(ft.Text(str(error)), bgcolor="red", show_close_icon=True))

    # Configuración de la página 
    page.title = "Altas"
    page.theme_mode = "light"
    page.window_width = 800
    page.window_height = 600

    page.appbar = ft.AppBar(
        title=ft.Text("Nuevo usuario"),
        leading=ft.Icon("person_add"),
        color="white",
        bgcolor="purple"
    )

    txt_clave = ft.TextField(label="Clave del usuario", width=400)
    txt_contra = ft.TextField(label="Contraseña", password=True, width=400)
    txt_contra2 = ft.TextField(label="Confirmar contraseña", password=True, width=400)
    txt_nombre = ft.TextField(label="Nombre completo", width=400)
    chk_admin = ft.Checkbox(label="¿Es administrador?")

    btn_guardar = ft.FilledButton(
        text="Guardar",
        icon="save",
        on_click=guardar_usuario,
        bgcolor="purple",
        color="white",
        style=ft.ButtonStyle(padding=ft.padding.symmetric(horizontal=30, vertical=10))
    )
    btn_cancelar = ft.FilledButton(
        text="Cancelar",
        icon="cancel",
        bgcolor="grey",
        color="white",
        style=ft.ButtonStyle(padding=ft.padding.symmetric(horizontal=30, vertical=10))
    )

    def volver(e):
        page.floating_action_button = None
        page.floating_action_button_location = None
        page.update()
        page.clean()
        ma.main(page)


    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ARROW_BACK,
        focus_color="black",
        on_click=volver
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.END_FLOAT


    fila = ft.Row(
        controls=[btn_guardar, btn_cancelar],
        alignment=ft.MainAxisAlignment.START,
        spacing=20
    )

    formulario = ft.Column(
        controls=[txt_clave, txt_contra, txt_contra2, txt_nombre, chk_admin, fila],
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

# Iniciar app
if __name__ == "__main__":
    ft.app(target=main)

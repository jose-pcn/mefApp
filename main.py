import flet as ft
from assets import cores

def main(page: ft.Page):
    page.title = "Método dos Elementos Finitos"
    page.window.width = 950
    page.window.height = 700
    page.window.resizable = False
    page.window.maximizable = False
    page.bgcolor = cores.AZUL_MARINHO_ESCURO
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.center()

    # Registre a fonte antes de aplicá-la no tema
    page.fonts = {
        "Roboto_regular": "./assets/fonts/Roboto-Regular.ttf",
        "Roboto_black": "./assets/fonts/Roboto-Black.ttf"
    }

    # Aplicando a fonte Roboto em toda a página
    page.theme = ft.Theme(font_family="Roboto_regular")

    # Adicionando a logo
    imagem_logo = ft.Image(
        src="assets/images/logo.png",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    # Retângulo (container) do menu
    rectangle_menu = ft.Container(
        width=450,
        height=630,
        bgcolor="white",
        border_radius=20,
        alignment=ft.alignment.top_center,
        content=ft.Text("PROJETOS", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),  # Fonte aplicada corretamente
    )

    # Colocando a imagem e o container lado a lado em um Row
    page.add(
        ft.Row(
            controls=[imagem_logo, rectangle_menu],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=100,
        )
    )

# Executando a aplicação
ft.app(target=main)

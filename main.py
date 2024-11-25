import flet as ft

def main(page: ft.Page):
    page.title = "Método dos Elementos Finitos"
    page.window.width = 950
    page.window.height = 700
    page.window.resizable = False
    page.bgcolor = "#001b40"

    # Aplicando a fonte Roboto em toda a página
    page.font_family = "Roboto"

    # Adicionando a logo
    imagem_logo = ft.Image(
        src="assets/images/logo.png",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    # Retângulo (container) do menu
    rectangle_menu = ft.Container(
        width=475,
        height=630,
        bgcolor="white",
        border_radius=20,
        alignment=ft.alignment.center,
        content=ft.Text("Projeto", size=18, color="black"),
    )

    # Colocando a imagem e o container lado a lado em um Row
    page.add(
        ft.Row(
            controls=[imagem_logo, rectangle_menu],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Ajusta o espaçamento entre os itens
            vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza os itens verticalmente
        )
    )

# Executando a aplicação
ft.app(target=main)

import flet as ft
from assets import cores


def create_project(page: ft.Page):
    # Limpando as pages para garantir que não há sobreposição
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    rectangle_background = ft.Container(
        width=850,
        height=630,
        bgcolor="white",
        border_radius=20,
        alignment=ft.alignment.top_center,
        content=ft.Column(
            controls=[
                ft.Text("PROJETOS", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black")
            ]
        )
    )
    # Adicionando uma nova view
    page.views.append(
        ft.View(
            "/create_project",
            bgcolor=cores.AZUL_MARINHO_ESCURO,
            controls=[
                rectangle_background
            ]
        )
    )

    # Atualizando a página
    page.update()

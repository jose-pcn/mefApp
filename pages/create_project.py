import flet as ft
from assets import cores


def create_project(page: ft.Page):
    # Limpando as pages para garantir que não há sobreposição
    page.views.clear()

    # Adicionando uma nova view
    page.views.append(
        ft.View(
            "/create_project",
            controls=[
                ft.Container(
                    width=450,
                    height=630,
                    bgcolor="white",
                    border_radius=20,
                    alignment=ft.alignment.top_center,
                    content=ft.Text(
                        "PROJETO",
                        size=30,
                        color=cores.AZUL_MARINHO_ESCURO,
                        font_family="Roboto_black"
                    )
                )
            ]
        )
    )

    # Atualizando a página
    page.update()

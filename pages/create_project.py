import flet as ft
from assets import cores
from configs import button_configs

def create_project(page: ft.Page):
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    caixa_nome_projeto = ft.TextField(label="Nome do projeto", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_nome_aluno = ft.TextField(label="Nome do aluno", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_tipo_elemento = ft.Dropdown(
        label="Tipo de elemento",
        width=400,
        height=50,
        options=[ft.dropdown.Option("Barra")]
    )
    botao_voltar_home = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/"))

    rectangle_background = ft.Container(
        width=500,
        height=630,
        bgcolor="white",
        border_radius=20,
        alignment=ft.alignment.center,
        padding=ft.padding.all(40),
        content=ft.Column(
            spacing=40,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("DADOS DO PROJETO", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
                caixa_nome_projeto,
                caixa_nome_aluno,
                caixa_tipo_elemento,
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[botao_voltar_home, botao_continuar]
                )
            ]
        )
    )

    # Adicionando uma nova view
    page.views.append(
        ft.View(
            "/create_project",
            bgcolor=cores.AZUL_MARINHO_ESCURO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[rectangle_background]
        )
    )

    # Atualizando a página
    page.update()

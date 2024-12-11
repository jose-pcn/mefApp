import flet as ft
from assets import cores
from configs import button_configs
import csv
import os


def criar_carregamentos(page: ft.Page):
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    caixa_tipo_carregamento = ft.Dropdown(label="Tipo de apoio", width=200, height=50, options=[
        ft.dropdown.Option("Concentrado"),
        ft.dropdown.Option("Distribuído")
    ])
    caixa_coordenadas_carregamento = ft.TextField(label="(x, y)", width=200, height=50,
                                     border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_intensidade_carregamento = ft.TextField(label="Intensidade", width=200, height=50,
                                                  border_color=cores.AZUL_MARINHO_ESCURO)
    botao_adicionar_carregamento = button_configs.criar_botao(texto="+", on_click=lambda _: print("Adicionado"))
    botao_voltar = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/pagina_apoios"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/pagina_esforcos"))

    rectangle_background = ft.Container(
        width=900,
        height=630,
        bgcolor="white",
        border_radius=20,
        alignment=ft.alignment.center,
        padding=ft.padding.all(40),
        content=ft.Column(
            spacing=40,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("CARREGAMENTOS", size=30, color=cores.AZUL_MARINHO_ESCURO,
                        font_family="Roboto_black"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[caixa_tipo_carregamento, caixa_coordenadas_carregamento, caixa_intensidade_carregamento]
                ),
                botao_adicionar_carregamento,
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[botao_voltar, botao_continuar]
                )
            ]
        )
    )

    # Adicionando uma nova view
    page.views.append(
        ft.View(
            "/pagina_carregamentos",
            bgcolor=cores.AZUL_MARINHO_ESCURO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[rectangle_background]
        )
    )

    # Atualizando a página
    page.update()

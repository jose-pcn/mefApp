import flet as ft
from assets import cores
from configs import button_configs
import csv
import os


def criar_apoios(page: ft.Page):
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    caixa_tipo_apoio = ft.Dropdown(label="Tipo de apoio", width=400, height=50, options=[
        ft.dropdown.Option("Fixo"),
        ft.dropdown.Option("Móvel")
    ])
    caixa_coordenadas = ft.TextField(label="(x, y)", width=400, height=50,
                                     border_color=cores.AZUL_MARINHO_ESCURO)

    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: print("Adicionado"))
    botao_voltar_home = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/pagina_geometria"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/pagina_carregamentos"))

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
                ft.Text("APOIOS", size=30, color=cores.AZUL_MARINHO_ESCURO,
                        font_family="Roboto_black"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[caixa_tipo_apoio, caixa_coordenadas]
                ),
                botao_adicionar_elemento,
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
            "/pagina_apoios",
            bgcolor=cores.AZUL_MARINHO_ESCURO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[rectangle_background]
        )
    )

    # Atualizando a página
    page.update()

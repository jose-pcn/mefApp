import flet as ft
from assets import cores
from configs import button_configs
import csv
import os


def criar_geometria(page: ft.Page):
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    caixa_coordenada_no_1 = ft.TextField(label="(x\u2081, y\u2081)", width=400, height=50,
                                      border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_coordenada_no_2 = ft.TextField(label="x\u2082, y\u2082", width=400, height=50,
                                    border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_area = ft.TextField(label="Área", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_mod_e = ft.TextField(label="Módulo de elasticidade", width=400, height=50,
                               border_color=cores.AZUL_MARINHO_ESCURO)

    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: print("Adicionado"))
    botao_voltar_home = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/create_project"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/pagina_apoios"))

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
                ft.Text("GEOMETRIA E PROPRIEDADES", size=30, color=cores.AZUL_MARINHO_ESCURO,
                        font_family="Roboto_black"),
                ft.Row(
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[caixa_coordenada_no_1, caixa_coordenada_no_2]
                ),
                ft.Row(
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[caixa_area, caixa_mod_e]
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
            "/pagina_geometria",
            bgcolor=cores.AZUL_MARINHO_ESCURO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[rectangle_background]
        )
    )

    # Atualizando a página
    page.update()

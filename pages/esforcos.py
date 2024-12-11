import flet as ft
from assets import cores
from configs import button_configs
import csv
import os


def criar_esforcos(page: ft.Page):
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    botao_voltar = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/pagina_carregamentos"))

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
            controls=[botao_voltar]
        )
    )


    # Adicionando uma nova view
    page.views.append(
        ft.View(
            "/pagina_esforcos",
            bgcolor=cores.AZUL_MARINHO_ESCURO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[rectangle_background]
        )
    )

    # Atualizando a página
    page.update()

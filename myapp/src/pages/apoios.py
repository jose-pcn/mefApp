import flet as ft
from src.assets import cores
from src.configs import button_configs


def criar_campo_apoio(n: int):
    caixa_tipo_apoio = ft.Dropdown(label="Tipo de apoio", width=200, height=50, options=[
        ft.dropdown.Option("Fixo"),
        ft.dropdown.Option("Móvel")
    ])
    caixa_coordenadas = ft.TextField(label="x, y", width=200, height=50,
                                     border_color=cores.AZUL_MARINHO_ESCURO)
    return [
    ft.Text(f"Apoio {n}", size=15, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_normal", text_align=ft.TextAlign.START),
    ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[caixa_tipo_apoio, caixa_coordenadas]
    )
]


indice_apoio = 1
lista_apoios = []
lista_apoios.extend(criar_campo_apoio(1))


def adicionar_campo_apoio(page):
    page.scroll = True
    global indice_apoio
    indice_apoio += 1
    lista_apoios.extend(criar_campo_apoio(indice_apoio))
    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: adicionar_campo_apoio(page))
    botao_voltar = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/pagina_geometria"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/pagina_carregamentos"))
    # Atualizar a lista de controles na página
    page.views[-1].controls[0].content.controls = [
        ft.Text("APOIOS", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
        *lista_apoios,
        botao_adicionar_elemento,
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[botao_voltar, botao_continuar]
        )
    ]
    page.update()


def aplicar_campo_apoios(page: ft.Page):
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    botao_voltar_home = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/pagina_geometria"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/pagina_carregamentos"))
    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: adicionar_campo_apoio(page))
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
            scroll=ft.ScrollMode.AUTO,
            controls=  [
                ft.Text("APOIOS", size=30, color=cores.AZUL_MARINHO_ESCURO,font_family="Roboto_black"),
                *lista_apoios,
                botao_adicionar_elemento,
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[ botao_voltar_home,
                                botao_continuar]
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

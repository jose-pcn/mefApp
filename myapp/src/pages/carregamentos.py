import flet as ft
from src.assets import cores
from src.configs import button_configs


def criar_campo_carregamento(n: int):
    caixa_tipo_carregamento = ft.Dropdown(label="Tipo de carregamento", width=250, height=50, options=[
        ft.dropdown.Option("Concentrado"),
        ft.dropdown.Option("Distribuído")
    ])
    caixa_coordenadas = ft.TextField(label="(x, y)", width=250, height=50,
                                     border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_intensidade = ft.TextField(label="Intensidade", width=250, height=50,
                                     border_color=cores.AZUL_MARINHO_ESCURO)
    return [
        ft.Text(f"Carregamento {n}", size=15, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_normal",
                text_align=ft.TextAlign.START),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[caixa_tipo_carregamento, caixa_coordenadas, caixa_intensidade]
        )
    ]


indice_carregamento = 1
lista_carregamentos = []
lista_carregamentos.extend(criar_campo_carregamento(1))


def adicionar_campo_carregamento(page):
    page.scroll = True
    global indice_carregamento
    indice_carregamento += 1
    lista_carregamentos.extend(criar_campo_carregamento(indice_carregamento))
    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: adicionar_campo_carregamento(page))
    botao_voltar = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/pagina_apoios"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/pagina_esforcos"))
    # Atualizar a lista de controles na página
    page.views[-1].controls[0].content.controls = [
        ft.Text("CARREGAMENTOS", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
        *lista_carregamentos,
        botao_adicionar_elemento,
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[botao_voltar, botao_continuar]
        )
    ]
    page.update()


def criar_carregamentos(page: ft.Page):
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    botao_adicionar_carregamento = button_configs.criar_botao(texto="+", on_click=lambda _: print("Adicionado"))
    botao_voltar = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/pagina_apoios"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/pagina_esforcos"))
    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: adicionar_campo_carregamento(page))
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
            controls=[
                ft.Text("CARREGAMENTOS", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
                *lista_carregamentos,
                botao_adicionar_elemento,
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

import flet as ft
from src.assets import cores
from src.configs import button_configs


def subscript_number(n: int) -> str:
    """
    Função que converte um número inteiro em uma string com os dígitos em formato de subscrito.
    :param n:
    :return:
    """
    subscripts = "₀₁₂₃₄₅₆₇₈₉"
    return ''.join(subscripts[int(digit)] for digit in str(n))


def criar_campo_geometria(n: int):
    """
    Função que cria um campo para inserção de dados de um elemento.
    :param n:
    :return:
    """
    n_sub = subscript_number(n)
    n_sub_pos = subscript_number(n + 1)
    return [
        ft.Text(f"Elemento {n}", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
        ft.Row(
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[ft.TextField(label=f"x{n_sub}, y{n_sub}", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO),
                      ft.TextField(label=f"x{n_sub_pos}, y{n_sub_pos}", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO)]
        ),
        ft.Row(
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[ft.TextField(label="Área", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO),
                      ft.TextField(label="Módulo de elasticidade", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO)]
        )
    ]


indice = 1
lista_propriedades_geometricas = []
lista_propriedades_geometricas.extend(criar_campo_geometria(indice))


def adicionar_elemento(page):
    """
    Função que adiciona um novo elemento à lista de elementos.
    :param page:
    :return:
    """
    page.scroll = True
    global indice
    indice += 1
    lista_propriedades_geometricas.extend(criar_campo_geometria(indice))
    # Atualizando a interface.
    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: adicionar_elemento(page))
    botao_voltar_home = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/create_project"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: page.go("/pagina_apoios"))
    page.views[-1].controls[0].content.controls = [
        ft.Text("GEOMETRIA E PROPRIEDADES", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
        *lista_propriedades_geometricas,
        botao_adicionar_elemento,
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[botao_voltar_home, botao_continuar]
        )
    ]
    page.update()


def criar_geometria(page: ft.Page):
    """
    Função que cria a página de geometria e propriedades.
    :param page:
    :return:
    """
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: adicionar_elemento(page))
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
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text("GEOMETRIA E PROPRIEDADES", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
                *lista_propriedades_geometricas,
                botao_adicionar_elemento,
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[botao_voltar_home, botao_continuar]
                )
            ]
        )
    )


    page.views.append(
        ft.View(
            "/pagina_geometria",
            bgcolor=cores.AZUL_MARINHO_ESCURO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[rectangle_background]
        )
    )


    page.update()

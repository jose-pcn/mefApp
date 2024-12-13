import flet as ft
from assets import cores
from configs import button_configs


def subscript_number(n: int) -> str:
    subscripts = "₀₁₂₃₄₅₆₇₈₉"
    return ''.join(subscripts[int(digit)] for digit in str(n))

def criar_campo_geometria(n: int):
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


coluna_propriedades_geometricas = criar_campo_geometria(1)


def adicionar_elemento(evento):
    novo_indice = (len(coluna_propriedades_geometricas) // 2) + 1  # Calcula o próximo índice corretamente
    novos_campos = criar_campo_geometria(novo_indice)

    # Localize o container principal e adicione os novos campos diretamente
    container_principal = evento.control  # Assume que o botão é o evento acionador
    while not isinstance(container_principal, ft.Container):
        container_principal = container_principal.parent  # Navega para o container pai

    # Adiciona os novos controles à lista do container
    if isinstance(container_principal.content, ft.Column):
        container_principal.content.controls[-2:-2] = novos_campos  # Insere antes do botão de CONTINUAR

    container_principal.update()  # Atualiza o container com as novas alterações


def criar_geometria(page: ft.Page):
    page.views.clear()
    page.scroll=True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    botao_adicionar_elemento = button_configs.criar_botao(texto="+", on_click=lambda _: adicionar_elemento)
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
                ft.Text("GEOMETRIA E PROPRIEDADES", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
                *coluna_propriedades_geometricas,
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

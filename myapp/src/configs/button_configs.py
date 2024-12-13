import flet as ft
from assets import cores


# noinspection PyTypeChecker
def criar_botao(
    texto: str,
    on_click: callable,
    largura: int = 200,
    altura: int = 50,
    cor_texto_default: str = cores.AZUL_MARINHO_ESCURO,
    cor_fundo_default: str = cores.BRANCO,
    cor_fundo_hover: str = cores.BRANCO,
    cor_texto_hover: str = cores.BRANCO,
) -> ft.ElevatedButton:
    return ft.ElevatedButton(
        text=texto,
        on_click=on_click,
        width=largura,
        height=altura,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.padding.all(10),
            elevation={
                ft.MaterialState.DEFAULT: 5,
                ft.MaterialState.HOVERED: 5,
            },
            text_style=ft.TextStyle(font_family="Roboto_regular", size=18),
            bgcolor={
                ft.MaterialState.DEFAULT: cor_fundo_default,
                ft.MaterialState.HOVERED: cor_fundo_hover,
            },
            color={
                ft.MaterialState.DEFAULT: cor_texto_default,
                ft.MaterialState.HOVERED: cor_texto_hover,
            },
        ),
    )

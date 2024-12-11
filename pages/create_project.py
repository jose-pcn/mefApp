import flet as ft
from assets import cores
from configs import button_configs
import csv
import os

projeto_csv = "./data/dados_projeto.csv"

def gerar_nome_arquivo(nome_projeto):
    # Substituir espaços por underscores e remover caracteres especiais
    nome_sanitizado = "".join(c if c.isalnum() or c in "_-" else "_" for c in nome_projeto.strip())
    # Caminho completo para o arquivo
    return os.path.join("data", f"{nome_sanitizado}.csv")

def salvar_dados_csv(nome_projeto, nome_aluno, tipo_elemento):
    caminho_arquivo_dados = gerar_nome_arquivo(nome_projeto)
    with open(caminho_arquivo_dados, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nome do projeto", "Nome do aluno", "Tipo de elemento"])
        writer.writerow([nome_projeto, nome_aluno, tipo_elemento])

    print(caminho_arquivo_dados)

def carregar_dados_csv():
    if not os.path.exists(projeto_csv):
        return "", "", ""
    with open (projeto_csv, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        try:
            return next(reader)
        except StopIteration:
            return "", "", ""

def create_project(page: ft.Page):
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nome_projeto, nome_aluno, tipo_elemento = carregar_dados_csv()

    caixa_nome_projeto = ft.TextField(label="Nome do projeto", width=400, height=50,
                                      border_color=cores.AZUL_MARINHO_ESCURO, value=nome_projeto)
    caixa_nome_aluno = ft.TextField(label="Nome do aluno", width=400, height=50,
                                    border_color=cores.AZUL_MARINHO_ESCURO, value=nome_aluno)
    caixa_tipo_elemento = ft.Dropdown(
        label="Tipo de elemento",
        width=400,
        height=50,
        options=[ft.dropdown.Option("Barra")],
        value=tipo_elemento
    )
    botao_voltar_home = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _:
    salvar_dados_csv(caixa_nome_projeto.value, caixa_nome_aluno.value, caixa_tipo_elemento.value)
    or page.go("/pagina_geometria"))

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

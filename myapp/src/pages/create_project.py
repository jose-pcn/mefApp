import flet as ft
from src.assets import cores
from src.configs import button_configs
import csv, re

def salvar_projeto(page, nome_projeto, nome_aluno):
    nome_arquivo = re.sub(r'[^a-zA-Z0-9_-]', '', nome_projeto.replace(" ","_")) + ".csv"
    cabecalho = ["Nome do Projeto", "Nome do Aluno", "Tipo de Elemento"]
    nome_projeto = re.sub(r'[^a-zA-Z0-9_-]', '', nome_projeto.replace(" ","_"))
    nome_aluno = re.sub(r'[^a-zA-Z0-9_-]', '', nome_aluno.replace(" ","_"))

    dados = [[nome_projeto, nome_aluno]]

    # Salvar os dados no arquivo CSV
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(cabecalho)
        escritor.writerows(dados)

    # Salvar o nome do arquivo no client_storage
    page.client_storage.set("nome_arquivo", nome_arquivo)

    print(f"Projeto {nome_projeto} salvo com sucesso!")
    print(f"Nome do arquivo salvo no storage: {nome_arquivo}")



def create_project(page: ft.Page):
    # Carregar valores armazenados, caso existam
    nome_projeto = page.client_storage.get("nome_projeto")
    if nome_projeto is None:
        nome_projeto = ""
    nome_aluno = page.client_storage.get("nome_aluno")
    if nome_aluno is None:
        nome_aluno = ""
    page.views.clear()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    caixa_nome_projeto = ft.TextField(label="Nome do projeto", width=400, height=50,
                                      value=nome_projeto,
                                      border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_nome_aluno = ft.TextField(label="Nome do aluno", width=400, height=50,
                                    value=nome_aluno,
                                    border_color=cores.AZUL_MARINHO_ESCURO)
    caixa_tipo_elemento = ft.Dropdown(
        label="Tipo de elemento",
        width=400,
        height=50,
        options=[ft.dropdown.Option("Barra")],
    )
    botao_voltar_home = button_configs.criar_botao(texto="VOLTAR", on_click=lambda _: page.go("/"))
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _:
    [page.client_storage.set("nome_projeto", caixa_nome_projeto.value),page.client_storage.set("nome_aluno", caixa_nome_aluno.value),
     salvar_projeto(page,caixa_nome_projeto.value, caixa_nome_aluno.value),page.go("/pagina_geometria")])

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

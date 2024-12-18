import flet as ft
from src.assets import cores
from src.configs import button_configs
import csv, os


def salvar_geometria(page, elemento, x1y1, x2y2, area, modulo_elasticidade):
    # Caminho absoluto onde o arquivo será salvo
    pasta_dados = r"data"

    # Cria a pasta caso não exista
    os.makedirs(pasta_dados, exist_ok=True)

    # Nome do arquivo completo
    nome_arquivo = page.client_storage.get("nome_arquivo")
    print(f"Storage atual: {page.client_storage.get('nome_arquivo')}")

    if not nome_arquivo:
        print("Erro: Nome do arquivo não foi definido.")
        return
    arquivo_geometria = os.path.join(pasta_dados, f"{os.path.splitext(nome_arquivo)[0]}_geometria.csv")

    # Cabeçalho do arquivo CSV
    cabecalho = ["Elemento", "x1, y1", "x2, y2", "Area", "Modulo de Elasticidade"]

    try:
        # Verifica se o arquivo já existe para evitar sobrescrever o cabeçalho
        escrever_cabecalho = not os.path.exists(arquivo_geometria)

        with open(arquivo_geometria, mode='a', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            if escrever_cabecalho:
                escritor.writerow(cabecalho)  # Escreve o cabeçalho se necessário

            # Escreve o dado do elemento
            escritor.writerow([elemento, x1y1, x2y2, area, modulo_elasticidade])

        print(f"Elemento {elemento} salvo com sucesso no arquivo {arquivo_geometria}!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


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
    elemento_inicial = ft.TextField(label=f"x{n_sub}, y{n_sub}", width=400, height=50,
                                    border_color=cores.AZUL_MARINHO_ESCURO)
    elemento_final = ft.TextField(label=f"x{n_sub_pos}, y{n_sub_pos}", width=400, height=50,
                                  border_color=cores.AZUL_MARINHO_ESCURO)
    area = ft.TextField(label="Área", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO)
    campo_mod_e = ft.TextField(label="Módulo de elasticidade", width=400, height=50, border_color=cores.AZUL_MARINHO_ESCURO)
    return [
        ft.Text(f"Elemento {n}", size=30, color=cores.AZUL_MARINHO_ESCURO, font_family="Roboto_black"),
        ft.Row(
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[elemento_inicial,elemento_final]

        ),
        ft.Row(
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[area,
                      campo_mod_e]
        )
    ]

indice = 1
lista_propriedades_geometricas = []
lista_propriedades_geometricas.extend(criar_campo_geometria(indice))


def botao_continuar_on_click(page):
    dados = []

    # Coleta os dados de cada controle (linha por linha)
    for controle in lista_propriedades_geometricas:
        if isinstance(controle, ft.Row):
            # Itera sobre os controles dentro do Row
            for campo in controle.controls:
                if isinstance(campo, ft.TextField) and campo.value:  # Garante que o campo tem valor
                    dados.append(campo.value)

    # Verificação dos dados coletados
    print(f"Dados coletados: {dados}")  # Exibe os valores para depuração

    # Itera sobre os dados coletados e organiza em grupos de 4 (x1y1, x2y2, area, modulo_elasticidade)
    for i in range(0, len(dados), 4):
        if i + 4 <= len(dados):  # Garante que há valores suficientes para um elemento
            elemento = f"Elemento {i // 4 + 1}"  # Calcula o número do elemento
            x1y1, x2y2, area, modulo_elasticidade = dados[i:i + 4]

            # Salva os dados do elemento
            salvar_geometria(page, elemento, x1y1, x2y2, area, modulo_elasticidade)
        else:
            print(f"Erro: Dados incompletos para o elemento {i // 4 + 1}. Dados recebidos: {dados[i:]}")

    print("Todos os dados foram processados.")


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
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: [botao_continuar_on_click(page),page.go("/pagina_apoios")])
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
    botao_continuar = button_configs.criar_botao(texto="CONTINUAR", on_click=lambda _: [botao_continuar_on_click(page),page.go("/pagina_apoios")])

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

import flet as ft
from pages.home_page import home_page
from pages.create_project import create_project
from pages.geometria_propriedades import criar_geometria
from pages.apoios import aplicar_campo_apoios
from pages.carregamentos import criar_carregamentos
from pages.esforcos import criar_esforcos

import sys
import os

# Adicionar o diretório raiz ao caminho | Não tenho muita certeza de porque precisa.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main(page: ft.Page):
    """
    Função principal da aplicação.
    Função que define os caminhos de rotas
    :param page:
    :return:
    """
    # Função chamada ao mudar a rota
    def route_change(_):

        page.views.clear()
        # Rota inicial ("/")
        if page.route == "/":
            home_page(page)

        # Rota para criação de projeto
        elif page.route == "/create_project":
            create_project(page)

        elif page.route == "/pagina_geometria":
            criar_geometria(page)

        elif page.route == "/pagina_apoios":
            aplicar_campo_apoios(page)

        elif page.route == "/pagina_carregamentos":
            criar_carregamentos(page)
        # Atualizar a exibição da página

        elif page.route == "/pagina_esforcos":
            criar_esforcos(page)
        page.update()

    # Configuração do evento de mudança de rota
    page.on_route_change = route_change

    # Navegar para a rota atual (ou padrão)
    page.go(page.route)

# Executar a aplicação
ft.app(target=main)

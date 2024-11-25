import flet as ft
from pages.home_page import home_page
from pages.create_project import create_project


def main(page: ft.Page):
    # Função chamada ao mudar a rota
    def route_change(e):
        page.views.clear()

        # Rota inicial ("/")
        if page.route == "/":
            home_page(page)

        # Rota para criação de projeto
        elif page.route == "/create_project":
            create_project(page)

        # Atualizar a exibição da página
        page.update()

    # Configuração do evento de mudança de rota
    page.on_route_change = route_change

    # Navegar para a rota atual (ou padrão)
    page.go(page.route)


# Executar a aplicação
ft.app(target=main)

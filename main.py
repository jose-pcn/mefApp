import flet as ft

def main(page: ft.Page):
    page.title = "Método dos Elementos Finitos"
    page.window.width = 950
    page.window.height = 700
    page.window.resizable = False
    page.bgcolor = "#001b40"

    # Aplicando a fonte Roboto em toda a página
    page.font_family = "Roboto"

    # Dividindo a tela
    rectangle = ft.Container(
        width=475,
        height=630,
        bgcolor="white",
        border_radius=20,
        alignment=ft.alignment.top_center,
        content=ft.Text("Projeto", size=18, color="black")
    )

    # Adicionando o retângulo à janela
    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[rectangle],
                    alignment=ft.MainAxisAlignment.END
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    rectangle =ft.Container()
# Executando a aplicação
print("Teste commit")
ft.app(target=main)

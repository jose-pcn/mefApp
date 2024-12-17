# Calculadora de Treliças Planas

Este projeto foi desenvolvido como parte da avaliação da disciplina **Introdução ao Método dos Elementos Finitos** da **Universidade Federal do Piauí**. A aplicação tem como objetivo calcular treliças planas, considerando a entrada de dados textuais sobre as propriedades da estrutura, apoios, carregamentos e esforços.

## Logo do Projeto

![Logo](src/assets/images/logo.png)

## Funcionalidades

- **Página inicial**: Exibe o painel inicial com as opções do usuário.
- **Criação de projeto**: Permite ao usuário criar um novo projeto e configurar suas propriedades iniciais.
- **Definir geometria e propriedades**: Permite a definição da geometria da estrutura e suas propriedades.
- **Aplicação de apoios**: Configura os apoios da estrutura.
- **Carregamentos**: Define os carregamentos aplicados à estrutura.
- **Esforços**: Exibe os esforços atuantes na estrutura.

## Objetivo do Projeto

Este projeto foi desenvolvido com fins acadêmicos, especificamente para o estudo de treliças planas utilizando o Método dos Elementos Finitos (MEF). A ferramenta permite a entrada de dados textuais para calcular as forças e reações nas barras da treliça. **Importante**: a aplicação não possui interface gráfica para desenho, sendo restrita à entrada de dados em formato de texto.

## Limitações

- **Entrada de dados**: A aplicação aceita apenas exemplos de barras para treliças, ou seja, não é possível desenhar a treliça diretamente.
- **Interface**: Não há suporte para desenhos ou gráficos, a entrada é totalmente baseada em texto.

## Pré-requisitos

Este projeto utiliza a biblioteca **Flet** para a criação da interface gráfica, que deve ser instalada antes de rodar a aplicação. Não há bibliotecas adicionais necessárias.

### Como instalar as dependências

Para instalar a biblioteca **Flet**, use o seguinte comando:

```bash
pip install flet

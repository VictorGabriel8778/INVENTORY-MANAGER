from stock import *
import PySimpleGUI as sg

def janela_cadastro():
    
    sg.theme("SystemDefault")
    
    estoque = Estoque()
    produtos = estoque.listar_produtos()
    
    layout_cadastro = [
        [sg.Text("Nome do produto              ", font=(4, 15)),sg.Text("Quantidade de produto      ", font=(4, 15)),sg.Text("Preço de produto", font=(4, 15))],
        [sg.Input(size=(30, 1),key="-NOME-"),sg.Text("  "),sg.Input(size=(30, 1),key="-QUANTIDADE-"),sg.Text("    "),sg.Input(size=(30, 1),key="-PRECO-"),sg.Button("ADICIONAR", size=(24, 1), font=(4, 10)), sg.Button("CANCELAR", size=(24, 1), font=(4, 10))],
        [sg.HorizontalSeparator()],
        [sg.Text()],
        [sg.Table(
            values=produtos,
            headings=["ID", "Nome", "Qtd", "Preço"],
            auto_size_columns=False,
            justification="center",
            key="-TABELA-",
            num_rows=min(15, len(produtos)),
            expand_x=True, 
            col_widths=[5, 20, 10, 10]  ,
            font=(1,15),
            header_border_width=0
        )],
        [sg.Text("Desenvolvido por Victor Gabriel F.B Dias")]
    ]

    window = sg.Window("CADASTRO DE PRODUTOS", layout_cadastro, resizable=True, finalize=True, size=(1200,500))

    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == "CANCELAR":
            window.close()
            break

        elif event == "ADICIONAR":
            try:
                nome = value["-NOME-"]
                qtd = int(value["-QUANTIDADE-"])
                preco = str(value["-PRECO-"])
                preco = float(preco.replace(',', '.'))
                estoque.adicionar_produtos(nome,qtd,preco)
                
                produtos = estoque.listar_produtos()
                window['-TABELA-'].update(produtos)
                
                sg.popup("Produto adicionado com sucesso!")
            except:
                sg.popup("Valores inválidos!")

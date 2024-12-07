from stock import *
import PySimpleGUI as sg

def remover_produtos():
    
    estoque = Estoque()
    produtos = estoque.listar_produtos()
    
    sg.theme("SystemDefault")
    
    layout_remover = [
        [sg.Text("ID do produto",font=(4,15)),sg.Input(size=(25,1),font=(4,13),key="-ID_PRODUTO-"),sg.Button("REMOVER",size=(20,1),font=(4,13)),sg.Button("CANCELAR",size=(20,1),font=(4,13))],
        [sg.HorizontalLine()],
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
            border_width=0,
            header_border_width=0
        )],
        [sg.Text("Desenvolvido por Victor Gabriel F.B Dias")]
    ]
    
    window = sg.Window("REMOVER PRODUTOS", layout_remover, layout_remover, resizable=True, finalize=True, size=(1200,500))
    
    while True:
        event, value = window.read()
        
        if event == sg.WIN_CLOSED or event == "CANCELAR":
            window.close()
            break
        
        if event == "REMOVER":
            id_produto = value["-ID_PRODUTO-"]
            estoque.remover_produtos(id_produto)
            
            produtos = estoque.listar_produtos()
            window["-TABELA-"].update(produtos)

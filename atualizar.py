import PySimpleGUI as sg
from stock import *

def atualizar_qtd():
    
    sg.theme("SystemDefault")
    
    sg.Text("Quantidade   ",font=(4,15))
    
    estoque = Estoque()
    produtos = estoque.listar_produtos()
    
    layout_atualizar = [
        [sg.Text("Id do produto",font=(4,15)),sg.Text("                       "),sg.Text("Quantidade   ",font=(4,15))],
        [sg.Input(size=(25,1),font=(4,13), key="-ID-"),sg.Input(size=(25,1),font=(4,13), key="-QTD-"),sg.Button("ATUALIZAR",size=(16,1),font=(4,12)  ),sg.Button("CANCELAR",size=(16,1),font=(4,12))],
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
            col_widths=[5, 20, 10, 10],
            font=(1,15),
            border_width=0,
            header_border_width=0
        )],
        [sg.Text("Desenvolvido por Victor Gabriel F.B Dias")]
    ]
    
    window = sg.Window("ATUALIZAR QUANTIDADE", layout_atualizar, resizable=True, finalize=True, size=(1200,500))
    
    while True:
        event, value = window.read()
        
        if event == sg.WIN_CLOSED or event == "CANCELAR":
            window.close()
            break
        
        if event == "ATUALIZAR":
            try:
                id_produto = int(value["-ID-"])
                qtd_produto = int(value["-QTD-"])
                estoque = Estoque()
                estoque.atualizar_lista(id_produto,qtd_produto)
                
                produtos = estoque.listar_produtos()
                window['-TABELA-'].update(produtos)
                
                sg.popup("Produtos atualizados")
            except:
                sg.popup("Valores invalidos")    

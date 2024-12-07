from stock import *
import PySimpleGUI as sg
from cadastro import *
from remover import *
from atualizar import *

sg.theme("SystemDefault")

estoque = Estoque()
produtos = estoque.listar_produtos()

layout_principal = [
    [sg.Text("Sistema de Gestão de Estoque",font=(2,15))],
    [sg.HorizontalLine()],
    [sg.Button("CADASTRAR PRODUTO",size=(25,1),font=(4,15)),
    sg.Button("REMOVER PRODUTO",size=(25,1),font=(4,15)),
    sg.Button("ATUALIZAR QUANTIDADE",size=(25,1),font=(4,15)),
    sg.Button("CANCELAR",size=(25,1),font=(4,15))],
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

window = sg.Window("GESTAO DE ESTOQUE", layout_principal, resizable=True, finalize=True, size=(1200,500))

while True:
    event, value = window.read()
    
    if event == sg.WIN_CLOSED or event == "CANCELAR":
        break
    
    if event == "CADASTRAR PRODUTO":
        window.hide()
        janela_cadastro()
        window.un_hide()
        
    elif event == "REMOVER PRODUTO":
        window.hide()
        remover_produtos()
        window.un_hide()
        
    elif event == "ATUALIZAR QUANTIDADE":
        window.hide()
        atualizar_qtd()
        window.un_hide()
        
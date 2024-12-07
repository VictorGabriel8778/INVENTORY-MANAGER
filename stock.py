import sqlite3 

class Produtos:
    
    def __init__(self,id_produto,nome,qtd,preco):
        self.id_produto = id_produto
        self.nome = nome
        self.qtd = qtd
        self.preco = preco
        
class Estoque:
    
    def __init__(self, db_name="estoque.db"):
        self.estoque = sqlite3.connect(db_name)
        self.criar_tabela()
        
    def criar_tabela (self):
        query = """
            CREATE TABLE IF NOT EXISTS produtos (
                id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                qtd INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        """

        self.estoque.execute(query)
        self.estoque.commit()
        
    def adicionar_produtos(self,nome,qtd,preco):
        query = "INSERT INTO produtos (nome, qtd, preco) VALUES (?,?,?)"
        self.estoque.execute(query, (nome,qtd,preco))
        self.estoque.commit()
        print ("Produto adicionado!")
        
    def listar_produtos(self):
        query = "SELECT * FROM produtos"
        return self.estoque.execute(query).fetchall()
    
    def atualizar_lista(self,id_produto,qtd):
        query = "UPDATE produtos SET qtd = ? WHERE id_produto = ?"
        self.estoque.execute(query, (qtd,id_produto))
        self.estoque.commit()
        
    def remover_produtos(self, id_produto):
        query = "DELETE FROM produtos WHERE id_produto = ?"
        self.estoque.execute(query,(id_produto))
        self.estoque.commit()
        print ("Produtos removidos!")

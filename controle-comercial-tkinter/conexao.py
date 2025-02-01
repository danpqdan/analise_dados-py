import sqlite3
import os
from assets.router_path import dir
import os
import sqlite3
import bcrypt

class Conexao:
    def __init__(self, db_name="comercial.db"):
        self.db_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "comercial-sql")
        os.makedirs(self.db_folder, exist_ok=True)
        self.db_file = os.path.join(self.db_folder, db_name)
        self.db = None
        self.connect()

    def connect(self):
        if not os.path.exists(self.db_file):
            print(f"Banco de dados não encontrado. Criando novo banco em: {self.db_file}")
            self.db = sqlite3.connect(self.db_file)
            self.create_tables()
            self.create_entry_data()
        else:
            print(f"Conexão estabelecida com o banco existente: {self.db_file}")
            self.db = sqlite3.connect(self.db_file)


    def create_tables(self):
        try:
            cursor = self.db.cursor()
            cursor.execute('''create table IF NOT EXISTS prodserv (
                    codigo varchar(13) not null,
                    tipo varchar(10) not null,
                    descricao varchar(60) not null,
                    quantidade mediumint,
                    custo decimal(10,2),
                    preco decimal(10,2),
                    primary key (codigo));
                ''')
            cursor.execute('''create table IF NOT EXISTS clientes (
                        codigo mediumint not null,
                        nome varchar(50) not null,
                        telefone varchar(30) not null,
                        email varchar(50) not null,
                        observacao varchar(255),
                        primary key (codigo));
                           ''')
            cursor.execute("""create table IF NOT EXISTS auto_num (
                           num_venda bigint not null,
                           primary key (num_venda))
            """)
            cursor.execute('''create table IF NOT EXISTS vendas_cab (
                           num_venda bigint not null,
                           codigo_cli mediumint not null,
                           data_hora Timestamp not null,
                           total_venda decimal(10,2),
                           primary key (num_venda));
                           ''')
            cursor.execute('''create table IF NOT EXISTS vendas_lin (
                           num_venda bigint not null,
                           lin_venda smallint not null,
                           codigo_prod varchar(13) not null,
                           quantidade mediumint,
                           valor_unit decimal(10,2),
                           valor decimal(10,2),
                           primary key (num_venda, lin_venda)
                           )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS login (
                        codigo_int INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario VARCHAR(30) NOT NULL UNIQUE,
                        nome VARCHAR(50) NOT NULL,
                        senha VARCHAR(20),
                        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')
            self.db.commit()
            print("Tabelas criadas com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")

        
    # def save_snapshot(self):
    #     try:
    #         with sqlite3.connect(self.db_file) as backup_connection:
    #             self.db.backup(backup_connection)
    #         print(f"Snapshot salvo em: {self.db_file}")
    #     except sqlite3.Error as e:
    #         print(f"Erro ao salvar snapshot: {e}")

    def load_snapshot(self):
        connection = sqlite3.connect(":memory:")
        try:
            with sqlite3.connect(self.db_file) as backup_connection:
                backup_connection.backup(connection)
            print(f"Snapshot carregado de: {self.db_file}")
        except sqlite3.Error as e:
            print(f"Erro ao carregar snapshot: {e}")
        return connection

    def gravar(self, sql, params=None):
        try:
            cursor = self.db.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            self.db.commit()
            print("Gravação bem-sucedida.")
        except sqlite3.Error as e:
            print(f"Erro ao gravar no banco: {e}")
            return False
        return True

    def consultar(self, sql, params=None):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, params or [])
            response = cursor.fetchone()
            return response
        except sqlite3.Error as e:
            print(f"Erro ao consultar no banco: {e}")
            return None

    def consultar_tree(self, sql, params=None):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, params or [])
            response = cursor.fetchall()
            return response
        except sqlite3.Error as e:
            print(f"Erro ao consultar no banco: {e}")
            return None

    def fechar(self):
        # self.save_snapshot()
        if self.db:
            self.db.close()
            print("Conexão encerrada.")

    def create_entry_data(self):
        self.gravar('''insert into prodserv (codigo, tipo, descricao, quantidade, custo, preco)
                        values (?, ?, ?, ?, ?, ?)''',
            ('7899334343001', 'PRODUTO', 'ARROZ BRANCO 5KG', 19, 15.70, 22.76))
        self.gravar('''insert into prodserv (codigo, tipo, descricao, quantidade, custo, preco )
                        values (?, ?, ?, ?, ?, ?)''',
            ('7899334343002', 'PRODUTO', 'FEIJAO CARIOCA 1KG', 43, 3.65, 6.23))
        self.gravar('''insert into prodserv (codigo, tipo, descricao, quantidade, custo, preco )
                        values (?, ?, ?, ?, ?, ?)''',
            ('7899334343003', 'PRODUTO', 'ACUCAR REFINADO BRANCO', 77, 3.80, 5.45))
        self.gravar('''insert into prodserv (codigo, tipo, descricao, quantidade, custo, preco )
                        values (?, ?, ?, ?, ?, ?)''',
            ('7899334343004', 'PRODUTO', 'OLEO DE SOJA', 52, 5.30, 7.82))
        self.gravar('''insert into prodserv (codigo, tipo, descricao, quantidade, custo, preco )
                        values (?, ?, ?, ?, ?, ?)''',
            ('7899334343005', 'PRODUTO', 'BOTIJAO DE GAS 13 KG', 7, 99.32, 125.50))
        self.gravar('''insert into prodserv (codigo, tipo, descricao, quantidade, custo, preco )
                        values (?, ?, ?, ?, ?, ?)''',
            ('1', 'SERVICO', 'ENTREGA REGIAO CENTRAL', 1, 8, 10))
            
        consulta = self.consultar("SELECT * FROM clientes WHERE codigo = ?", (1,))
        print(f"Consulta individual: {consulta}")
        if consulta:
            print('Cliente já existe...')
        else:
            self.gravar('''insert into clientes (codigo, nome, telefone, email, observacao)
                        values (?, ?, ?, ?, ?)''',
                      (1, 'JOSE DA SILVA','11 99111-0001','JOSESILVA001@JALUC.COM.BR','OTIMO CLIENTE'))
            self.gravar('''insert into clientes (codigo, nome, telefone, email, observacao)
                        values (?, ?, ?, ?, ?)''',
                       (2, 'CARLOS MARTINS','11 99222-0001','CARLOSMARTINS001@JALUC.COM.BR','NOVO CLIENTE'))
            self.gravar('''insert into clientes (codigo, nome, telefone, email, observacao)
                        values (?, ?, ?, ?, ?)''',
                      (3, 'SUELI DOS SANTOS','11 99333-0001','SUELISANTOS001@JALUC.COM.BR','CLIENTE EXIGENTE'))
            self.gravar('''insert into clientes (codigo, nome, telefone, email, observacao)
                        values (?, ?, ?, ?, ?)''',
                      (4, 'JOANA SILVA','11 99444-0001','JOANASILVA@JALUC.COM.BR','CLIENTE VIP'))

        consulta = self.consultar('SELECT * FROM login WHERE usuario = ?', ('admin',))
        if consulta:
            print('Usuário já existe...')
        else:
            salt = bcrypt.gensalt()
            senha_hash = bcrypt.hashpw('admin'.encode('utf-8'), salt)
            self.gravar('''insert into login (usuario, nome, senha)
                        values (?, ?, ?)''',
                      ('admin', 'Administrador padrão', senha_hash))
        



    
'''
class conexao(object):
    def __init__(self):

        
        #Conexão Máquina Local
        self.db = mysql.connector.connect(host ="localhost", user = "root",
                                        password = "root", db ="controle")     


    #127.0.0.1        
    def gravar(self, sql):
        try:
            cur=self.db.cursor()
            cur.execute(sql)
            cur.close()
            self.db.commit()
        except:
             return False;
        return True;
        
    def consultar(self, sql):
        rs=None
        try:
            cur=self.db.cursor()
            cur.execute(sql)
            rs=cur.fetchone()
        except:
            return None
        return rs

    def consultar_tree(self, sql):
        rs=None
        try:
            cur=self.db.cursor()
            cur.execute(sql)
            rs=cur.fetchall()
        except:
            return None
        return rs    


    def fechar(self):
        self.db.close()
'''
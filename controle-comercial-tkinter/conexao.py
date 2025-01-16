import mysql.connector
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

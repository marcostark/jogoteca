class Usuario:

    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_senha(self):
        return self.senha
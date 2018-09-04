class Jogo:
    def __init__(self, nome, categoria, plataforma, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def get_plataforma(self):
        return self.plataforma


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
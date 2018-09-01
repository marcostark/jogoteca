class Jogo:
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome;
        self.categoria = categoria
        self.plataforma = plataforma

    def get_nome(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def get_plataforma(self):
        return self.plataforma


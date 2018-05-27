class Proprietario(object):

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def getNome(self):
        return self.nome

    def getTelefone(self):
        return self.telefone
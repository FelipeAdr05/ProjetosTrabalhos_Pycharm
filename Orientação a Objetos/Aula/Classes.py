class Pessoa:
    # atributos
    def __init__(self, idade, sexo, nome):
        self.idade = idade
        self.nome = nome
        self.sexo = sexo


pessoa1 = Pessoa(17, 'Masculino', 'Felipe')
pessoa2 = Pessoa(16, 'Masculino', 'Gustavo')




print(pessoa1.nome)



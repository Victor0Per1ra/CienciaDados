class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade

# Criando uma instância da classe Pessoa
pessoa = Pessoa("João", 30)

print(dir(pessoa))

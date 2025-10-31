import dataclasses 
from dataclasses import dataclass

@dataclass
class Endereco:
        logadouro:str
        numero:int


@dataclass
class Pessoa:
        nome:str
        idade:int
        endereco:Endereco #relacionamento com a classe 



def expondo_dados(self):

    print(F"olá seja bem vindo{self.nome}, idade: {self.idade},endereço:{self.endereco} ")
    print(f"{self.logadouro}, número:{self.numero}")


cliente=Pessoa(nome=input("qual o seu nome:"),
               idade=input("qual sua idade:"),
               endereco=input("informe seu endereço:"),)


localização=Endereco(logadouro=input("informe o logadouro:"), numero=input("informe o número:"))

cliente.expondo_dados
localização.expondo_dados
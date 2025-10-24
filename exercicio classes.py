import os
from dataclasses import dataclass

@dataclass
class Dados:
    nome=str
    cpf:str
    telefone:str

    #Funções
    def  mostrar_dados(self):
            print(f"nome:{self.nome}")
            print(f"cpf:{self.cpf}")
            print(f"telefone:{self.telefone}")
        
    def dados_marketing(self):
            print(f"telefone:{self.telefone}")
    
#vetor
lista_de_pessoas=[] 

#inserindo dados
for i in range(3):
    p=Dados(nome=input("qual o seu nome:\n"),
    cpf=input("qual o seu cpf:\n"),
    telefone=input("informe o telefone:\n"))
lista_de_pessoas.append(p)


#mostrando os dados
for p in lista_de_pessoas:
    p.mostrar_dados_dados()
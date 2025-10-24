

import os 
from dataclasses import dataclass

@dataclass
class Dados:
        nome:str
        email:str
        endereço:str

        
def dados_1(self):
                nome=input("informe o seu nome:\n")
                email=input("informe endereço de e-mail:\n")
                endereço=input("informe o endereço:")
                lista_de_dados.append(nome, email, endereço)
                print(f"nome:{self.nome}")
                print(f"endereço:{self.endereço}")
                print(f"{self.nome}")
                print(f"{self.endereço}")

lista_de_dados=[]
for i in range(2):
    pessoa=Dados(nome=input("informe o seu nome:\n"),
                email=input("informe endereço de e-mail:\n"),
                endereço=input("informe o endereço:"),)
lista_de_dados.append(pessoa)
  
   


for pessoa in lista_de_dados:
     
     pessoa.mostrar_dados_dados()

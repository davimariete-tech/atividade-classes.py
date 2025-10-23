import os
from dataclasses import dataclass

@dataclass
class dados:
        nome:str
        email:str
        telefone:float
        endereço:str

resultado=dados(nome=input("informe seu nome:"),email=input("informe o seu email:"),telefone=input("informe o seu telefone:"),endereço=input("informe o seu endereço:"))


print("=exibindo dados=")
print(f"nome:{resultado.nome}")
print(f"email:{resultado.email}")
print(f"telefone:{resultado.telefone}")
print(f"endereço:{resultado.endereço}")




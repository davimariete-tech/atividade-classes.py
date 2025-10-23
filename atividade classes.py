import os 
from dataclasses import dataclass

@dataclass
class pessoa:
        nome:str
        idade: int
        peso: float
        altura: float

inf=pessoa(nome=input("digite seu nome:"),idade=input("informe a idade:"),peso=input("informe o seu peso:"),altura=input("informe sua altura:"))

print(f"nome:{inf.nome}")
print(f"idade:{inf.idade}")
print(f"peso:{inf.peso}")
print(f"altura:{inf.altura}")

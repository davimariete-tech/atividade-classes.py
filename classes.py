from dataclasses import dataclass
@dataclass 
class Pessoa:
        nome:str
        idade:int
    
    
        @dataclass
        class pet:
            nome:str
            idade:int

pessoa1=Pessoa("marta",20)



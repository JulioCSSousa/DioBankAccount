from BankAccount2v.models.client import Client

class NPClient(Client):
    def __init__(self, address, cpf: str, name: str, birth_date: str):
        super().__init__(address)
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date

    def __str__(self):
        return f"{self.name} - {self.cpf} {self.birth_date}"
        
    
    
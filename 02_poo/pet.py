'''
# =====================================
# ARQUIVO : pet.py
# Disciplina : Programação de Sistemas (2026-2)
# Aula       : Aula 20 - Por que POO?
# Autor      : [Luiz Carlos Oliveira Neto]
# conceitos  : Classe, Objeto, Atributos, Métodos, Encapsulamento
# Atividade  : classe Pet
# =====================================
'''
class Pet:
    '''
    Esta classe representa um Pet em um sistema simples de hotel para pets.
    
    Em vez de guardar os dados do pet em um dicionário solto, como 
    fazíamos
    na programação estrutura, agora agrupamos od dados e comportamentos dentro de uma classe.
    '''

    def __init__(self, nome, especie, idade, raça="Desconhecida", nome_dono="Desconhecido", peso=0):
        '''
        Método construtor.
        
        Ele é executado automaticamente quando criamos um novo objeto 
        Pet.
        
        Exemplo:
        pet1 = Pet("Rex", "Cachorro", 5)
        
        Parâmetros:
        - nome: nome do pet
        - especie: espécie do pet
        - idade: idade do pet
        '''

        self.nome = nome
        self.nome_dono = nome_dono
        self.raça = raça
        self.peso = peso
        self.especie = especie 
        self.idade = idade
        self.hospedado = False

    def exibir_dados(self):
        '''
        Exibe os dados principais do pet.
        
        Atualmente, mostra apenas nome, espécie e idade e status de hospedagem.
        '''

        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade} anos")
        print(f"Status de hospedagem: {'Hospedado' if self.hospedado else 'Não hospedado'}")
        print(f"Raça: {self.raça}")
        print(f"Nome do dono: {self.nome_dono}")
        print(f"Peso: {self.peso} kg")



    def registrar_entrada(self):
        '''
        Registra a entrada do pet no hotel.
        
        Se o pet ainda não estiver hosdpedado, muda o atributo hospedado 
        para True.

        ativida:
        melhore este método para verificar se o pet já esta hospedado.
        Se já estiver, mostre uma mensagem avisando.
        '''

        if not self.hospedado:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")
        else:
            print(f"{self.nome} já está hospedado.")


    def registrar_saida(self):
            '''
            registra a saida do pet do hotel.
            se o pet estiver hospedado, muda o atributo hospedado para false.

            Atividade:
            melhore este método para verificar se o pet realmente esta hospedado.
            se não estiver, mostre uma mensagem avisando.
            '''

            if self.hospedado:
                self.hospedado = False
                print(f"{self.nome} saiu do hotel.")
            else:
                print(f"{self.nome} não está hospedado.")

    def calcular_diaria(self):

        if self.especie.lower() == "cachorro":
            return 40
        elif self.especie.lower() == "gato":
            return 50
        else:
            return 30


def verificar_vacinacao(self):

        if self.idade > 1:
            return True
        else:
            return False

        
def atualizar_peso(self, novo_peso):

        self.peso = novo_peso
        print(f"O peso de {self.nome} foi atualizado para {self.peso} kg.")



def emitir_resumo(self):
        
        self.exibir_dados()
        print(f"Vacinação em dia: {'Sim' if self.verificar_vacinacao() else 'Não'}")
        print(f"Valor da diária: R$ {self.calcular_diaria()}")

pet1 = Pet("Rex", "Cachorro", 5)

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.exibir_dados()
pet1.registrar_saida()
pet1.calcular_diaria()



pet2 = Pet("Terror", "Gato", 3)

pet2.exibir_dados()
pet2.registrar_entrada()
pet2.exibir_dados()
pet2.registrar_saida()
pet2.calcular_diaria()


pet3 = Pet("Rogerin", "Periquito", 1)

pet3.exibir_dados()
pet3.registrar_entrada()
pet3.exibir_dados()
pet3.registrar_saida()
pet3.calcular_diaria()
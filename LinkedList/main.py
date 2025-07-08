class ListaEncadeadaSimples:
    class Nodo:
        def __init__(self, card, cardNumber):
            self.card = card
            self.cardNumber = cardNumber    
            self.proximo = None

    def __init__(self):
        self.head = None

    def inserir(self, card, cardNumber):
        nodo = self.Nodo(card, cardNumber)
        if self.head is None:
            self.head = nodo

        if card == 'A':
            self.inserirComPrioridade(nodo)
        else:
            self.inserirSemPrioridade(nodo)

def inserirSemPrioridade(self, nodo):
    if self.head is None:
        self.head = nodo
    else:
        nodoAtual = self.head
        while nodoAtual.proximo is not None:
            nodoAtual = nodoAtual.proximo
        nodoAtual.proximo = nodo
    

def inserirComPrioridade(self, nodo):
    nodoAtual = self.head
    anterior = None 
    while nodoAtual is not None:
        if nodoAtual.card == 'A' and nodo.cardNumber < nodoAtual.cardNumber:
            break
        if nodoAtual.card == 'V':
            break
        anterior = nodoAtual
        nodoAtual = nodoAtual.proximo

    if anterior is None:
        nodo.proximo = self.head
        self.head = nodo
    else:
        nodo.proximo = nodoAtual
        anterior.proximo = nodo


def imprimirListaEspera():
    # Função para imprimir a lista de espera
    pass

def atenderPaciente():
    # Função para atender o paciente
    pass


# PROGRAMA PRINCIPAL
fila = ListaEncadeadaSimples()

while True: 
    option = int(input(''' 
      [1] Adicionar paciente a fila.
      [2] Mostrar pacientes na fila.
      [3] Chamar paciente.
      [4] Sair.
      Escolha uma opção: 
      ''' ))

    if option == 1:
        card = input('Informe a cor do cartão do paciente: (A/V) ').upper()
        cardNumber = int(input('Informe o número do cartão do paciente: '))
        fila.inserir(card, cardNumber)

    elif option == 2:
        print('LISTA DE PACIENTES:')
        fila.imprimirListaEspera()
        
    elif option == 3:
        fila.atenderPaciente()
        
    elif option == 4:
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Por favor, tente novamente.')




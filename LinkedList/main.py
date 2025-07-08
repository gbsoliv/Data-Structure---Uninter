#retirar os comentários e completar o código

def inserir():
  card = input('Informe a cor do cartão do paciente: (A/V) ')
  cardNumber = int(input('Informe o número do cartão do paciente: '))
  
def inserirSemPrioridade(nodo):
    # Função para inserir paciente sem prioridade
    pass

def inserirComPrioridade(nodo): 
    # Função para inserir paciente com prioridade
    pass

def imprimirListaEspera():
    # Função para imprimir a lista de espera
    pass

def atenderPaciente():
    # Função para atender o paciente
    pass

# Inicio do codigo principal

while True: 
    option = int(input(print(''' 
      [1] Adicionar paciente a fila.
      [2] Mostrar pacientes na fila.
      [3] Chamar paciente.
      [4] Sair.
      Escolha uma opção: 
      ''' )))

    if option == 1:
        inserir()
        # Aqui você deve adicionar o paciente na fila de espera.
    elif option == 2:
        print('LISTA DE PACIENTES:')
        imprimirListaEspera()
        # Aqui você deve implementar a lógica para mostrar os pacientes na fila de espera.
    elif option == 3:
        atenderPaciente()
        # Aqui você deve implementar a lógica para chamar o paciente da fila de espera.
    elif option == 4:
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Por favor, tente novamente.')




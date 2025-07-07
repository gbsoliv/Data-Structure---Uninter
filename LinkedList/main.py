option = int(input(print(''' 
      [1] Adicionar paciente a fila de espera.
      [2] Mostrar pacientes na fila de espera.
      [3] Chamar paciente.
      [4] Sair.
      Escolha uma opção: 
      ''' )))

if option == 1:
    card = input('Informe a cor do cartão do paciente: (A/V) ')
    cardNumber = int(input('Informe o número do cartão do paciente: '))
    # Aqui você deve adicionar o paciente na fila de espera.
elif option == 2:
      print('LISTA DE PACIENTES:')
    # Aqui você deve implementar a lógica para mostrar os pacientes na fila de espera.
elif option == 3:
    print('Atendendo o paciente cartao cor {} e numero {}:')


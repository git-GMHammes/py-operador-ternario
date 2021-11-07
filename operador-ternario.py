#
# Operador ternario em python
#
print()
#
idade = input('Qual é a sua iadade? ')
if not idade.isnumeric():  # Caso não seja numerico pare aqui!
    print('Você precisa digitar apenas números!')
else:
    idade = int(idade)  # garante valor inteiro na variável idade
    maiorIdade = (idade >= 18)  # maiorIdade recebe uma condição
    # Operador ternário
    print('\n Pode acessar' if maiorIdade else '\n Não pode acessar')
#
logUser = True if maiorIdade else False # Melhor exemlo básico de operador ternário
#
if logUser:
    status = 'Usuário Logado - On'
else:
    status = 'Usuário Deslogado - Off'
#
print(status)
#
print('Resultado logUser - True \n' if logUser else 'Resultado logUser - False \n')
#

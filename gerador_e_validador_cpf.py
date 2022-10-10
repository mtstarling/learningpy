from random import randint
random = str(randint(100000000, 999999999))

while True:

    # ESCOLHA DA FUNÇÃO DO PROGRAMA (VALIDAR OU CRIAR CPF):

    choise = input('Você deseja [V]alidar ou [C]riar um CPF? ').lower()

    while choise != 'v' and choise != 'c':
        choise = input('Digite [V] para Validar ou [C] para Criar: ').lower()

    if choise == 'v':
        CPF = input('Digite um CPF: ')
        create_or_validade = 11
    elif choise == 'c':
        CPF = random
        create_or_validade = 9


    # MENSAGEM DE CARACTERES INVÁLIDOS:

    while len(CPF) != create_or_validade:
        print('DIGITE OS 11 NÚMEROS DO CPF!')
        CPF = input('Digite o CPF novamente: ')

    while not CPF.isnumeric():
        print('DIGITE SOMENTE NÚMEROS!')
        CPF = input('Digite o CPF novamente: ')

    # VERIFICAÇÃO DO PRIMEIRO DÍGITO FINAL:

    verify = 10
    add = 0
    digit = [0, 0]

    for x in range(len(CPF)-2):
        ver = int(CPF[x]) * (verify)
        add += ver
        verify -= 1

    digit[0] = 11 - (add % 11)

    if digit[0] > 9:
        digit[0] = 0

    # VERIFICAÇÃO DO SEGUNDO DÍGITO FINAL:

    verify = 11
    add = 0
    ver = 0

    for y in range(len(CPF)-1):
        ver = int(CPF[y]) * (verify)
        add += ver
        verify -= 1

    digit[1] = 11 - (add % 11)

    if digit[1] > 9:
        digit[1] = 0

    # PREPARANDO PARA IMPRESSÃO:

    CPF_print = (f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{digit[0]}{digit[1]}')

    # VALIDAÇÃO CPF:

    if choise == 'c':
        CPF += str(digit[0])
        CPF += str(digit[1])

    if (int(CPF[-2]) == digit[0]) and (int(CPF[-1]) == digit[1]):
        print(f'O CPF "{CPF_print}" É VÁLIDO.')
    else:
        print(f'O CPF "{CPF_print}" É INVÁLIDO.')

    # RESPOSTA PARA LAÇO WHILE:

    answer = input('Você deseja continuar [S]im ou [N]ão? ').lower()

    if answer == 'n':
        break
    elif answer == 's':
        continue
    else:
        while answer != 's' and answer != 'n':
            answer = input('Digite um valor válido [S] ou [N]: ').lower()
        else:
            if answer == 'n':
                break
            elif answer == 's':
                continue

    if (int(CPF[-2]) == digit[0]) and (int(CPF[-1]) == digit[1]):
        print(f'VOCÊ GEROU O CPF: "{CPF_print}" \n'
              f'(VÁLIDO)')
    else:
        print(f'VOCÊ GEROU O CPF: "{CPF_print}" \n'
              f'(INVÁLIDO)')

    # RESPOSTA PARA LAÇO WHILE:

    answer = input('Você deseja continuar [S]im ou [N]ão? ').lower()

    while answer != 's' and answer != 'n':
        answer = input('Digite um valor válido [S] ou [N]: ').lower()

    if answer == 'n':
        break
    elif answer == 's':
        continue
while True:

    CPF = input('Digite um CPF: ')

    while len(CPF) != 11:
        print('DIGITE OS 11 NÚMEROS DO CPF!')
        CPF = input('Digite o CPF novamente: ')

    while not CPF.isnumeric():
        print('DIGITE SOMENTE NÚMEROS!')
        CPF = input('Digite o CPF novamente: ')

    verify = 10
    add = 0
    digit = [0, 0]

    # VERIFICAÇÃO DO PRIMEIRO DÍGITO FINAL:

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

    # VALIDAÇÃO DO CPF:

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
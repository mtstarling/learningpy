while True:

    CPF = input('Digite um CPF: ')

    while len(CPF) != 11:
        print('DIGITE OS 11 NÚMEROS DO CPF!')
        CPF = input('Digite o CPF novamente: ')

    while not CPF.isnumeric():
        print('DIGITE SOMENTE NÚMEROS!')
        CPF = input('Digite o CPF novamente: ')

    CPF_size = len(CPF)
    CPF_split = list(CPF)

    # VERIFICAÇÃO DO PRIMEIRO DÍGITO FINAL:

    verify_1 = 10
    add_1 = 0

    for x in range(CPF_size - 2):
        CPF_split[x] = int(CPF_split[x])
        ver_digit_1 = CPF_split[x] * (verify_1)
        add_1 += ver_digit_1
        verify_1 -= 1

    digit_1 = 11 - (add_1 % 11)

    if digit_1 > 9:
        digit_1 = 0

    # VERIFICAÇÃO DO SEGUNDO DÍGITO FINAL:

    verify_2 = 11
    add_2 = 0

    for y in range(CPF_size - 1):
        CPF_split[y] = int(CPF_split[y])
        ver_digit_2 = CPF_split[y] * (verify_2)
        add_2 += ver_digit_2
        verify_2 -= 1

    digit_2 = 11 - (add_2 % 11)

    if digit_2 > 9:
        digit_2 = 0

    # PREPARANDO PARA IMPRESSÃO:

    CPF_print = (f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:10]}{CPF[10:11]}')

    # VALIDAÇÃO DO CPF:

    if (int(CPF_split[-2]) == digit_1) and (int(CPF_split[-1]) == digit_2):
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

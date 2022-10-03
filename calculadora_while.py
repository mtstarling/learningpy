import operator

operator_list = ['+', '-', '*', '/', '**']
#                 0    1    2    3    4

print()
print()
print()
print('        ###########################')
print('        WELCOME TO THE MTCALCULATOR')
print('   - An calculter to use only 2 numbers -')
print('        ----------#######----------')

while True:

    print()
    num_1 = input('- First number: ')
    operator_input = input('- Operator sign: ')
    num_2 = input('- Second number: ')

    if num_1.isnumeric() and num_2.isnumeric():
        num_1 = int(num_1)
        num_2 = int(num_2)
    elif not num_1.isnumeric() or not num_2.isnumeric():
        try:
            num_1 = float(num_1)
            num_2 = float(num_2)
        except:
            print('#### Type an valid number #### \n'.upper())
            continue

    if operator_input not in operator_list:                            # INVALID OPERATOR
        print()
        print('#### Type an valid operator #### \n'.upper())
        print('TRY AGAIN: \n')
        continue

    match operator_input:
        case '+':
            result = operator.add(num_1, num_2)                         # ADDITION #
            choise = '+'
        case '-':
            result = operator.sub(num_1, num_2)                         # SUBTRACTION #
            choise = '-'
        case '*':
            result = operator.mul(num_1, num_2)                         # MULTIPLICATION #
            choise = '*'
        case '/':
            result = operator.truediv(num_1, num_2)                     # TRUE DIVISION #
            choise = '/'
        case '**':
            result = operator.pow(num_1, num_2)                         # POTENTIATION #
            choise = '**'

    print(f'RESULT OF ({num_1} {choise} {num_2}) = {result:.2f}')

    answer = ['y', 'n']
    print()
    break_input = input('Do you want to leave [Y]es or [N]o: ').lower()

    while break_input not in answer:
        break_input = input('Try [Y]es or [N]o to proceed: ').lower()     # INVALID ANSWER #

    if break_input == 'y':
        break

    print('------------------------------------------------------------')

print()
print('        ###########################')
print('        THANKS FOR USE MTCALCULATOR')
print('                    BYE!!                ')
print('        ----------#######----------')

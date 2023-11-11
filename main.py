# ----------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print('------------------------')
        print('Question Number '+str(question_num)+':')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)
        print(question_num)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# ----------------------------
def check_answer(answer,guess):
    if answer == guess:
        print('CORRECT!')
        return 1
    else:
        print("WRONG!")
        return 0
# ----------------------------
def display_score(correct_guesses, guesses):
    print('------------------------')
    print("RESULTS")
    print('------------------------')

    print("Answers: ", end='')
    for i in questions:
        print(questions.get(i),end='')
    print()

    print('Guesses: ', end= '')
    for i in guesses:
        print(i, end='')
    print()

    score = int((correct_guesses/len(questions))*100)

    print('Your score is: '+str(score)+'%')

# ----------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ").upper()

    if response == 'YES':
        return True
    else:
        return False

# ----------------------------

questions = {
'Não faz parte dos elementos básicos de um processador: ': 'A',
'Considere que a máquina X possui uma frequencia baseada em um processador de 800MHz. Portanto, a máquina X possui um tempo de ciclo de clock de: ': 'B',
'O que é multiprogramação: ': 'C',
'O que é um barramento multiplexado?: ': 'D'
}

options = [["A. Contador de instrução", "B. Registrador de instrução", "C.Relogio ou clock", "D. Unidade de controle"],
           ["A. 1,25 microssegundos","B. 1,25 nanossegundos","C. 0,125 nanossegundos","D. 0,125 microssegundos"],
           ['''A. É um modelo de computação onde existe apenas um programa de usuário carregado na memoria
 principal. Quando esse programa ganha a CPU, ele executa, sem interrupção, até terminar''',
            '''B. É uma técnica de projeto de hardware onde a linguagem de máquina não é executada 
 diretamente pelo hardware, mas sim interpretada por um microcodigo.''',
            '''C. É um modelo de computação onde existem vários programas de usuário
 carregados na memoria ao mesmo tempo. Esses programas concorrem entre si pelo uso da CPU.''', 
             '''D. É um processador de proposito geral construído em um único chip'''],
           ['''A. Um barramento multiplexado é aquele que tem linhas dedicadas para o barramento de dados,
 o barramento de endereço e o barramento de controle.''',
            '''B.Um barramento multiplexado é uma arquitetura de comunicação em que múltiplos bits de dados
 são transmitidos simultaneamente através de canais separados. Cada bit tem seu próprio 
 caminho dedicado  ''',
            '''C. Um barramento em multiplexado é uma arquitetura de comunicação onde os bits de dados são 
 transmitidos sequencialmente por um único caminho. ''',
            '''D. Um barramento multiplexado é aquele onde os barramentos
 de dados e de endereço compartilham a mesmas linhas. Ou seja, o barramento tem linhas dedicadas
 para o barramento de controle, mas não para os barramentos de dados e de endereço''']]
new_game()
while play_again():
    new_game()
print('Byeeee!')

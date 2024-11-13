print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a Ilha do Tesouro.\n")
print("Sua missão é encontrar o Tesouro!\n")
escolha1=str(input('Você está em uma encruzilhada, para onde deseja ir?\n'
                   'Esquerda ou direita?\n')).lower()
if escolha1=='esquerda':
    escolha2=str(input('Você encontrou um lago.\n'
                       'Digite "Nadar" para atravessar nadando.\n'
                       'Digite "Esperar" para esperar um barco \n')).lower()
    if escolha2=='esperar':
       escolha3= str(input('Você chega à ilha ileso.\n'
              'Há uma casa com três portas.\n'
              'Uma [0;31mVermelha\n'
              'Uma Amarela\n'
              'e uma Azul\n'
              'Qual você escolhe? \n'))
       if escolha3=='vermelho':
        print('É uma sala cheia de fogo!. FIM DE JOGO')
       elif escolha3=='azul':
        print('Você entrou numa sala cheia de bestas selvagens. FIM DE JOGO')
       elif escolha3=='amarelo':
        print('Você encontrou a sala do tesouro. VOCÊ VENCEU!!')
       else:
           print('Você escolheu uma porta que não existe. FIM DE JOGO')
    else:
        print('Você foi atacado por um tubarão. FIM DE JOGO')
else:
    print('Você caiu em um buraco. FIM DE JOGO')
print('Obrigado por jogar!')
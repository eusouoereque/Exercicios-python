import random


valor = int(random.randint(1,100))

while True:
    chute = int(input("Digite um número entre 1 e 100: "))
    
    if chute < valor:
        print("O número é MAIOR do que o chute.")
    elif chute > valor:
        print("O número é MENOR do que o chute.")
    else:
        print("Parabéns! Você acertou o número.")
        break
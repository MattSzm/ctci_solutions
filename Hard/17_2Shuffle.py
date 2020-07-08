import random

def Shuffle(size:int=52)->list:
    deck = [x for x in range(1, size+1, 1)]
    for iter in range(0, size, 1):
        index = random.randint(0, iter)
        deck[iter], deck[index] = deck[index], deck[iter]
    return deck


if __name__ == '__main__':
    output = Shuffle()
    print(output)
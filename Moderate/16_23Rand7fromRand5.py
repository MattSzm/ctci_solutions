import random

def rand7():
    while True:
        x = 5*random.randint(0,5) + random.randint(0,5)
        if x < 21:
            return x%7

if __name__ == '__main__':
    print(rand7())
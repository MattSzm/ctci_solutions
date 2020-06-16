class Person:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death



def Living(input, start, end):
    memo =  [0 for _ in range(end-start+2)]
    for single in input:
        for itera in range(single.birth, single.death+1):
            memo[itera-start] += 1

    maxValue = 0
    for itera in range(1, len(memo)):
        if memo[itera] > memo[maxValue]:
            maxValue = itera

    return maxValue + start


if __name__ == '__main__':
    a = Person(1908,1909)
    b = Person(1910,1951)
    c = Person(1928,1986)
    d = Person(1903,1932)
    input = [a,b,c,d]
    output = Living(input,1900,2000)
    print(output)

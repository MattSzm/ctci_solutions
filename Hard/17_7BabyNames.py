
class dataStr:
    def __init__(self,name,value):
        self.names = [name]
        self.value = value

    def __str__(self):
        if len(self.names) > 0:
            return self.names[0]

class set:
    def __init__(self, inputDicts, Syno):
        self.Set = []
        for i in inputDicts:
            self.Set.append(dataStr(i, inputDicts[i]))
        self.Syno = Syno


    def algo(self):
        for [firstName, secondName] in self.Syno:
            firstFound = None
            secondFound = None
            for people in self.Set:
                if firstName in people.names:
                    firstFound = people
                elif secondName in people.names:
                    secondFound = people

                if firstFound and secondFound:
                    firstFound.names.extend(secondFound.names)
                    firstFound.value += secondFound.value
                    self.Set.remove(secondFound)
                    break

        for people in self.Set:
            print(people, '  ', people.value)


if __name__ == '__main__':
    names = {
        'John':15,
        'Jon':12,
        'Chris':13,
        'Kris':4,
        'Christopher':19
    }
    synonyms = [('Jon', 'John'), ('John', 'Johnny'), ('Chris', 'Kris'), ('Chris', 'Christopher')]
    setV1 = set(names, synonyms)
    setV1.algo()
    print('\n')

    namesV2 = {
        'John':10,
        'Jon':3,
        'Davis':2,
        'Kari':3,
        'Johny':11,
        'Carlton':8,
        'Carleton':2,
        'Jonathan':9,
        'Carrie':5
    }
    synonymsV2 = [('Jonathan','John'),('Jon','Johny'),('Johny','John'),('Kari','Carrie'),
                  ('Carleton','Carlton')]
    setV2 = set(namesV2, synonymsV2)
    setV2.algo()

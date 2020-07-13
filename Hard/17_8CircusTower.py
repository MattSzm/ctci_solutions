
class Person:
    def __init__(self,ht, wt):
        self.ht = ht
        self.wt = wt
        self.used = False

def algo(PeopleInput):
    sortedByHt = sorted(PeopleInput, key=lambda x:x.ht)
    sortedByWt = sorted(PeopleInput, key=lambda x:x.wt)
    firstEmpty = Person(0,0)
    memo = {}
    output = recursion(sortedByHt, sortedByWt, 0, 0, 0, firstEmpty, memo)
    return output


def recursion(sortedByHt, sortedByWt, htIndex, wtIndex, currOutput, lastOne, memo):
    key = f'{lastOne.ht}:{lastOne.wt}'
    if memo.get(key, False):
        return memo[key]

    byHeight = currOutput
    if htIndex != len(sortedByHt):
        iter = 0
        while htIndex + iter != len(sortedByHt):
            if (sortedByHt[htIndex+iter].ht > lastOne.ht and
                    sortedByHt[htIndex+iter].wt > lastOne.wt and
                    not sortedByHt[htIndex+iter].used):
                sortedByHt[htIndex + iter].used = True
                byHeight = recursion(sortedByHt, sortedByWt, htIndex+iter+1, wtIndex,
                                     currOutput+1, sortedByHt[htIndex+iter], memo)
                sortedByHt[htIndex + iter].used = False
                break
            iter += 1

    byWeight = currOutput
    if wtIndex != len(sortedByWt):
        iter = 0
        while wtIndex + iter != len(sortedByWt):
            if (sortedByWt[wtIndex+iter].ht > lastOne.ht and
                    sortedByWt[wtIndex+iter].wt > lastOne.wt and
                    not sortedByWt[wtIndex+iter].used):
                sortedByWt[wtIndex+iter].used = True
                byWeight = recursion(sortedByHt, sortedByWt, htIndex, wtIndex+iter+1,
                                    currOutput+1, sortedByWt[wtIndex+iter], memo)
                sortedByWt[wtIndex + iter].used = False
                break
            iter += 1

    outputValue =  byHeight if byHeight >= byWeight else byWeight
    memo[key] = outputValue
    return outputValue


if __name__ == '__main__':

    input = [Person(65,100),Person(70,150),Person(56,90),Person(75,190),Person(60,95),Person(68,110)]
    output = algo(input)
    print(output)
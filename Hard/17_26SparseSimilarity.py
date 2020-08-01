class Pair:
    def __init__(self, totalLength=None, similar=1):
        self.total = totalLength
        self.similar = similar
        self.similarity = 0

    def changeSimilarity(self):
        self.similarity = float(self.similar/self.total)


def Similarity(listOfDocuments):
    memo = {}
    pairs = {}
    for id in listOfDocuments.keys():
        for singleValue in listOfDocuments[id]:
            if memo.get(singleValue):
                memo[singleValue].append(id)
            else:
                memo[singleValue] = [id]

    for singleValue in memo:
        createPairs(listOfDocuments, memo[singleValue], pairs)

    output = {}
    for key in pairs:
        output[key] = pairs[key].similarity
    return output

def createPairs(listOfDocuments, ids, pairs):
    idIndex = 0
    while idIndex < len(ids):
        secondIdIndex = idIndex + 1
        while secondIdIndex < len(ids):
            smallerId = min(ids[idIndex], ids[secondIdIndex])
            biggerId = max(ids[idIndex], ids[secondIdIndex])
            keyBuilder = f'{smallerId}, {biggerId}'
            if keyBuilder in pairs.keys():
                pairs[keyBuilder].similar += 1
                pairs[keyBuilder].total -= 1
            else:
                length = len(listOfDocuments[ids[idIndex]]) + len(listOfDocuments[ids[secondIdIndex]]) - 1
                pairs[keyBuilder] = Pair(length)
            pairs[keyBuilder].changeSimilarity()
            secondIdIndex += 1
        idIndex += 1

if __name__ == '__main__':
    input = {13:[14,15,100,9,3],
             16:[32,1,9,3,5],
             19:[15,29,2,6,8,7],
             24:[7,10]}
    output = Similarity(input)
    for singleOutput in output:
        print(str(singleOutput) + ': ' + str(output[singleOutput]))

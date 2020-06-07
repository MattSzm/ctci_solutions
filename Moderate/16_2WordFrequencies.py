class freq:
    def __init__(self, book):
        self.memo = {}
        self.book = book

    def freqWrapper(self, word):
        if not word or word == ' ':
            return -1
        if word in self.memo.keys():
            print('working!')
            return self.memo[word]
        return self.freqAlgo(word)

    def freqAlgo(self, word):
        #for line in self.book:
        for singleWord in self.book.split(' '):
            if singleWord[len(singleWord)-1] in '.,?/!@()%':
                singleWord = singleWord[:len(singleWord)-1]
            if singleWord == word:
                if not self.memo.get(word):
                   self.memo[word] = 1
                else:
                    self.memo[word] += 1
        if self.memo.get(word):
            return self.memo[word]
        return 0

if __name__ == '__main__':
    book = 'writing some code, ctci ctci, moderate!'
    freq1 = freq(book)
    print(freq1.freqWrapper('apples'))
    print(freq1.freqWrapper('code'))
    print(freq1.freqWrapper('ctci'))
    print(freq1.freqWrapper(None))
    print(freq1.freqWrapper(' '))
    print(freq1.freqWrapper('ctci'))
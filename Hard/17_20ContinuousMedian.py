class ContinuousMedian:
    def __init__(self, input:list):
        self.array = sorted(input)
        self.medianValue = self.median()

    def median(self):
        if len(self.array)%2 == 1:
            return self.array[int((len(self.array)+1)/2)-1]
        else:
            index = int(len(self.array)/2) - 1
            return (self.array[index]+self.array[index+1])/2

    def add_new_element(self, input):
        self.array.append(input)

        key = input
        i = len(self.array)-2
        while i >= 0 and self.array[i] > key:
            self.array[i+1] = self.array[i]
            i -= 1
        self.array[i+1] = key
        self.medianValue = self.median()



if __name__ == '__main__':
    input = [6,2,8,1,9,10,3,3]
    median = ContinuousMedian(input)
    print(median.medianValue)
    median.add_new_element(4)
    print(median.medianValue)
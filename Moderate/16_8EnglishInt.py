
class EnglishInt:
    smalls = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
     "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
     "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens =["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
     "Eighty", "Ninety"]
    bigs = ["", "Thousand", "Million", "Billion"]
    hundred = 'hundred'
    neg = 'negative'

    def algo(self, input)->str:
        if input == 0:
            return self.smalls[0]
        if input < 0:
            input *= -1

        output = ''
        count = 0
        stack = []
        while input > 0:
            if input % 1000 != 0:
                smallOutput = self.convert(input%1000) + self.bigs[count]
                stack.append(smallOutput)
            input = int(input/1000)
            count += 1
        while stack:
            output += stack.pop() + ' '
        return output


    def convert(self, input)->str:
        output = ''
        if input >= 100:
            output += self.smalls[int(input/100)] + ' '
            output += self.hundred + ' '
            input %= 100
        if input >= 10 and input <= 19:
            output +=  self.smalls[input] + ' '
        elif input > 19:
            output += self.tens[int(input/10)] + ' '
            input %= 10
        if input < 10 and input > 0:
            output += self.smalls[input] + ' '
        return output


if __name__ == '__main__':
    conv = EnglishInt()
    print(conv.algo(5501))
    print(conv.algo(46213513514))
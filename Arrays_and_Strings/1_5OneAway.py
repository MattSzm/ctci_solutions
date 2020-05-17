import unittest

def OneAway(Fstring, Sstring):
    FL = len(Fstring)
    SL = len(Sstring)
    lenghtdiff = FL - SL
    if lenghtdiff < 0:
        lenghtdiff = -lenghtdiff
    if lenghtdiff > 1:
        return False
    elif lenghtdiff == 1:
        i=0
        j=0
        yellowFlag = False
        while i < FL and j < SL:
            if Fstring[i] != Sstring[j]:
                if yellowFlag:
                    return False
                yellowFlag = True
                if FL > SL:
                    i += 1
                else:
                    j += 1
            else:
                i += 1
                j += 1
    else:
        i=0
        j=0
        yellowFlag = False
        while i < FL and j < SL:
            if Fstring[i] != Sstring[j]:
                if yellowFlag:
                    return False
                yellowFlag = True
            i += 1
            j += 1
    return True

class test(unittest.TestCase):
    dataT = [
        ('pale', 'ple'),
        ('pales', 'pale'),
        ('pale', 'bale'),
        ('pale', 'pale'),
    ]
    dataF = [
        ('pale', 'bae'),
        ('ma', 'mamr'),
        ('pale', 'pblt'),
    ]

    def test_True(self):
        for [string1, string2] in self.dataT:
            result = OneAway(string1, string2)
            self.assertTrue(result)

    def test_False(self):
        for [string1, string2] in self.dataF:
            result = OneAway(string1, string2)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
def Convert(string):
    output = 0
    for j in string:
        output += ord(j.lower())
    return output

def GroupAnagrams(input):
    lenght = len(input)
    QuickSort(input, 0, lenght-1)

def QuickSort(input, p, q):
    if p <= q:
        m = QuickCompare(input, p, q)
        QuickSort(input, p, m-1)
        QuickSort(input, m+1, q)

def QuickCompare(input, p, q):
    key = Convert(input[q])
    j = p-1
    for i in range(p,q):
        if Convert(input[i]) <= key:
            j += 1
            input[j],input[i] = input[i],input[j]
    input[q],input[j+1] = input[j+1],input[q]
    return j+1

input =['mama', 'yafas', 'TaT', 'AmMA', 'urgd', 'fsaay', 'att','dfs']
GroupAnagrams(input)
for i in input:
    print(i)
def unique(input_string):
    memory = {}
    for item in input_string:
        k = memory.get(item)
        if k:
            return False
        else:
            memory[item] = True
    return True

input = 'cbafbgro'
print(unique(input))
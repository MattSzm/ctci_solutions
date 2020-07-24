def shortest(longer:list, shorter:list):
    memo = {}
    for item in shorter:
        memo[item] = None

    for_the_first_time = True
    best_result = {'left': 0, 'right': len(longer)}
    for index in range(len(longer)):
        item = longer[index]
        if item in memo:
            memo[item] = index
            if for_the_first_time:
                for el in memo.values():
                    if not el:
                        break
                else:
                    for_the_first_time = False
                    check_best_result(memo, best_result)
            else:
                check_best_result(memo, best_result)

    if best_result['right']-best_result['left'] == len(longer):
        return -1, -1
    return best_result['left'], best_result['right']

def check_best_result(memo, best_result):
    minV = min(memo.values())
    maxV = max(memo.values())
    if maxV-minV <= best_result['right']-best_result['left']:
        best_result['left'] = minV
        best_result['right'] = maxV


if __name__ == '__main__':
    shorter = [1,5,9]
    longer = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    left, right = shortest(longer, shorter)
    print(str(left)+'  '+str(right))
import copy

ans = list(input())
answer = [''] + ans
cnt = 0
k = 0
def asdf(a='', lst=[]):
    global cnt
    global k
    if k != 0:
        return
    result = copy.deepcopy(lst)
    result.append(a)
    if answer == result:
        cnt += 1
        k += 1
        return
    else:
        k = 0
    if len(result) == 4:
        cnt += 1
        return
    return asdf('A', result), asdf('B', result), asdf('C', result), asdf('D', result)
a = asdf()
print(f'{cnt}번째')
def dup(arry):
    res = []
    for i in arry:
        s = ''
        for j in range(len(i) - 1):
            if i[j] != i[(j + 1) % len(i)]:
                s+=i[j]
        if i[-1] != s[-1]:
            s += i[-1]
            res.append(s)
    return res

li = ['aaaba', 'smss']
print(dup(li))

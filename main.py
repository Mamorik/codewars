def spin_words(sentence):
    res = []
    liWord = sentence.split()
    for word in liWord:
        if len(word) < 5:
            res.append(word)
        else:
            st = ''
            for i in reversed(word):
                st+=i
            res.append(st)

    return (' '.join(res))


string = "Hello wordasasas"
print(spin_words(string))

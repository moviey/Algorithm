def solution(n, words):
    test = [words[0]]
    for i in range(len(words)-1) :
        if words[i+1] in test or not words[i+1].startswith(words[i][-1]):
            return [(i+1)%n+1, (i+1)//n+1]
        test.append(words[i+1])
    return [0,0]
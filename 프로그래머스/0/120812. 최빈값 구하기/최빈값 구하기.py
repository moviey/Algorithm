def solution(array):
    temp = {num:array.count(num) for i,num in enumerate(array)}
    mval = max(temp.values())
    count, answer =0,0
    for k, v in temp.items():
        if v==mval:
            count+=1
            answer=k
    return -1 if count >1 else answer
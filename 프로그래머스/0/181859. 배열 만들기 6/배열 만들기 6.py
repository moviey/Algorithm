def solution(arr):
    stk = []
    for num in arr :
        if len(stk)==0 :
            stk.append(num)
        elif stk[-1] == num :
            stk.pop()
        else :
            stk.append(num)
            
    return [-1] if len(stk)==0 else stk
def solution(k, tangerine):
    tan_dict = {}
    cnt = 0
    #딕셔너리는 정말 용량을 덜 잡아먹나보다
    for i in set(tangerine):
        tan_dict[i] = 0   
    for i in tangerine:
        tan_dict[i] += 1
    
    counts = sorted((i for i in tan_dict.values()), reverse = True) 
    
    for i, num in enumerate(counts):
        cnt+=num
        if cnt >= k : return i+1
    
    
    
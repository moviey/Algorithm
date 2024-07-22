def solution(a, b, n):
    total, rest = 0, 0
    while n>a:
        if n%a != 0 : rest = n%a 
        total += (n//a)*b 
        n = (n//a)*b + n%a
    return total + (n//a)*b
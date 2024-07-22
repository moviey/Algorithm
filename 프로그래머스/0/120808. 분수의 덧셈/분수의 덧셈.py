from math import gcd

def solution(numer1, denom1, numer2, denom2):
    idx2 =denom1*denom2 // gcd(denom1,denom2)
    idx1 = idx2//denom1*numer1 + idx2//denom2*numer2
    return [idx1//gcd(idx1,idx2), idx2//gcd(idx1,idx2)]
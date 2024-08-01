def solution(dots):
    dots.sort()
    x = abs(dots[0][0]-dots[-1][0])
    y = abs(dots[0][1]-dots[-1][1])
    return x*y
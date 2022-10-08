#link: https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    cont = 1

    while n > 0:
        
        print(' ' * (n-1) + '#'* cont )

        cont += 1 

        n -= 1

staircase(9)
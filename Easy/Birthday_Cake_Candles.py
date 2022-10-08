# link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles):
    cont = 0

    maior = max(candles)

    for c in candles:
        if maior == c:
            cont += 1

    print(maior)
    print(cont)

        
    

birthdayCakeCandles([3,2,1,3])
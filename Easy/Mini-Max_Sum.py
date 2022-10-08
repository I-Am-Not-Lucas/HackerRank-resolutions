#link: https://www.hackerrank.com/challenges/mini-max-sum/problem
from array import array


def miniMaxSum(arr):
    arr = sorted(arr)

    cont = len(arr) - 1
    tamanho_invertido = len(arr) -1 
    tamanho = 0

    min = [] 
    max = []

    while cont >= 0 and tamanho != len(arr) - 1:
        
        min.append(arr[tamanho])


        max.append(arr[tamanho_invertido])

        cont -= 1 
        tamanho += 1
        tamanho_invertido -= 1
  
    print(sum(min),sum(max))



        

miniMaxSum([7, 69, 2, 221, 8974])
        
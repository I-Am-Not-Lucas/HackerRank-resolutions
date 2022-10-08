#link: https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    
    total =  0 
    positive = 0
    negative  = 0
    zero = 0 
    # Write your code here
    
    for c in arr:
        if c == 0:
            zero += 1
            total += 1
        
        elif c > 0:
            positive += 1 
            total += 1
        
        else:
            negative += 1
            total += 1

    print(positive / total)
    print(negative / total)
    print(zero / total)


plusMinus([-4, 3, -9, 0, 4, 1])

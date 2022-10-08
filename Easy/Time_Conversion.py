#link: https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    conversor = ''
    if 'PM' in s:
        for c in s:
            if c != 'P' and c != 'M':
                conversor += c
        if conversor[0:2] != '12':
            conversor = conversor.replace(conversor[0:2], str((int(conversor[0:2]) + 12)))
        else:
            pass
        

    if 'AM' in s:
        for c in s:
            if c != 'A' and c != 'M':
                conversor += c
        
        if conversor[0:2] != '12':
            pass
        else:
            conversor = conversor.replace(conversor[0:2], '00')
    

    return conversor



print(timeConversion('07:05:45PM'))
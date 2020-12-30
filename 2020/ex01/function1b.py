import os

with open('inputreal.txt') as f:
    inputstr = []
    for line in f:
        w = int(line)
        inputstr.append(w)
    leni = len(inputstr)
    i = 0
    while i < leni:
        j = i + 1
        while j < leni:
            k = j + 1
            while k < leni:
                test = inputstr[i]+inputstr[j]+inputstr[k]
                if test == 2020:
                    result = inputstr[i]*inputstr[j]*inputstr[k]
                    print('found match i,j,k',i,j,k,'sum = ',inputstr[i],'+',inputstr[j],'+',inputstr[k],'=',test,'multiplication = ',result)
                    break
                else:
                    pass
                k += 1
            j += 1
        i += 1
        
f.close()

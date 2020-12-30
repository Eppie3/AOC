import os

with open('inputreal.txt') as f:
    inputstr = []
    for line in f:
        w = int(line)
        inputstr.append(w)
#    print(inputstr)
    leni = len(inputstr)
#    print(leni)
    i = 0
    while i < leni:
        j = i + 1
        while j < leni:
            test = inputstr[i]+inputstr[j]
#            print(test,i,j)
            if test == 2020:
                result = inputstr[i]*inputstr[j]
                print('found match i, j',i,j,'sum = ',inputstr[i],'+',inputstr[j],'=',test,'multiplication = ',result)
                break
            else:
                pass
            j += 1
        i += 1
        
#  print(len(inputstr)

f.close()

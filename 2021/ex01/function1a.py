def ask_ok(pr):
   lenpr = len(pr)
   num = pr.split(" ")
   i01 = num[0].split("-")
   i0 = int(i01[0])
   return i0

def increase_depth(d0,d1):
   if (d0<d1): return 1
   return 0

import os

#with open('input.txt') as f:
#with open('inputreal.txt') as f:
with open('input2a-real.txt') as f:
    num = [0]*100000
    numlin =0
    for line in f:
        lenl = len(line)
        num[numlin] = ask_ok(line)
        numlin += 1

    d0 = num[0]
    i = 1
    inc = 0
    while i < numlin:
         d1 = num[i]
#         print('depth d0,d1',d0,d1)
         inc += increase_depth(d0,d1)
         i += 1
         d0 = d1

    print('Number of increases: ',inc)

f.close()

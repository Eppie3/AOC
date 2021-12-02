def ask_ok(pr):
   lenpr = len(pr)
   num = pr.split(" ")
   i01 = num[0].split("-")
   i0 = int(i01[0])
#   print('i0',i0)

   return i0

def increase_depth(d0,d1):
   if (d0<d1):
#      print('Increase in depth',d0,d1)
      return 1
   return 0

import os

#with open('inputreal.txt') as f
#with open('input2b-real.txt') as f:
with open('input2a-real.txt') as f:
    num = [0]*100000
    yvalid,nvalid = 0,0
    numlin =0
    for line in f:
        lenl = len(line)
        num[numlin] = ask_ok(line)
        numlin += 1

    dsum = [0]*4
    iuse = [-1]*4
    i = 0
    inc = 0
    imod = [1,0,-1,-2]
    icd1  = [0,1,2,3]
    icd2  = [1,2,3,0]
#    for ic in range(4):
#       print ('icd[ic]',ic,icd1[ic],icd2[ic])
    
    while i < numlin:
         d1 = num[i]

         for ic in range(4):
            #print ('i,ic ',i,ic)
            if i < 1 and ic == 1: continue
            if i < 2 and ic == 2: continue
            if i < 3 and ic == 3: continue
            iuse[ic] = (i+imod[ic])%4
            #print('ic,iuse[ic]',i,ic,iuse[ic])

            if iuse[ic] > 0: dsum[ic] += d1
         for ic in range(4):
            if iuse[ic] == 0:
               #print('compare d0,d1',dsum[icd1[ic]],dsum[icd2[ic]])
               inc += increase_depth(dsum[icd1[ic]],dsum[icd2[ic]])
               dsum[ic] = 0
         
         i += 1
         
    print('Number of increases: ',inc)

f.close()

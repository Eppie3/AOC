def ask_ok(pr):
   lenpr = len(pr)
   num = pr.split(" ")
   i01 = num[0].split("-")
   i0 = int(i01[0])
   print('i0',i0)

#   chpw = num[1].strip(":")
#   print('password char:',chpw)

#   pw = pr.rsplit(": ")
#   pwd = pw[1]
#   print('pw:',pwd)

#   ic,i = 0,0
#   while i < len(pwd):
#       if pwd[i]==chpw:
#          ic += 1
#       i += 1
#
#   if ic < i0:
#       return 0
#
#   if ic > i1:
#       return 0

#  valid
   return i0

def increase_depth(d0,d1):
   if (d0<d1):
      print('Increase in depth',d0,d1)
      return 1
   return 0

import os

#with open('input.txt') as f:
#with open('inputreal.txt') as f:
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
    while i < numlin:
         d1 = num[i]

         iuse[0] = (i+1)%4
         print('iuse[0]',iuse[0])
         if i > 0: iuse[1] = (i)%4
         print('iuse[1]',iuse[1])
         if i > 1: iuse[2] = (i-1)%4
         print('iuse[2]',iuse[2])
         if i > 2: iuse[3] = (i-2)%4
         print('iuse[3]',iuse[3])

         if iuse[0] > 0: dsum[0] += d1
         if iuse[1] > 0: dsum[1] += d1
         if iuse[2] > 0: dsum[2] += d1
         if iuse[3] > 0: dsum[3] += d1

         if iuse[0] == 0:
            print('compare d0,d1',dsum[0],dsum[1])
            inc += increase_depth(dsum[0],dsum[1])
            dsum[0] = 0
         if iuse[1] == 0:
            print('compare d0,d1',dsum[1],dsum[2])
            inc += increase_depth(dsum[1],dsum[2])
            dsum[1] = 0
         if iuse[2] == 0:
            print('compare d0,d1',dsum[2],dsum[3])
            inc += increase_depth(dsum[2],dsum[3])
            dsum[2] = 0
         if iuse[3] == 0:
            print('compare d0,d1',dsum[3],dsum[0])
            inc += increase_depth(dsum[3],dsum[0])
            dsum[3] = 0
         
         i += 1
         d0 = d1

    print('Number of increases: ',inc)

f.close()

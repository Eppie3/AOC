def ask_ok(pr):
   lenpr = len(pr)
   num = pr.split(" ")
   i01 = num[0].split("-")
   i0 = int(i01[0])
   i1 = int(i01[1])
#   print('i0-i1',i0,i1)

   chpw = num[1].strip(":")
#   print('password char:',chpw)

   pw = pr.rsplit(": ")
   pwd = pw[1]
#   print('pw:',pwd)

   ic,i = 0,0
   while i < len(pwd):
       if pwd[i]==chpw:
          ic += 1
       i += 1

   if ic < i0:
       return 0

   if ic > i1:
       return 0

#  valid
   return 1


import os

#with open('input.txt') as f:
#with open('inputreal.txt') as f:
with open('input2a-real.txt') as f:
    inputstr = []
    yvalid,nvalid = 0,0
    for line in f:
        lenl = len(line)
        valid = ask_ok(line)
        if valid:
#            print('Valid pwd: ',line)
            yvalid += 1
        else:
#            print('Non-Valid pwd: ',line)
            nvalid += 1

    print('Number of   valid passwords: ',yvalid)
    print('Number of invalid passwords: ',nvalid)

f.close()

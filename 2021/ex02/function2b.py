def forward(pr):
   lenpr = len(pr)
   num = pr.split(" ")
   ix = int(num[1])
   if (num[0]=='forward'):return ix
   return 0

def down(pr):
   lenpr = len(pr)
   num = pr.split(" ")
   ix = int(num[1])
   if (num[0]=='down'):return ix
   return 0

def up(pr):
   lenpr = len(pr)
   num = pr.split(" ")
   ix = int(num[1])
   if (num[0]=='up'):return -ix
   return 0

import os

#with open('input2a.txt') as f:
with open('input2a-real.txt') as f:
    x,y,aim = 0,0,0
    for line in f:
        aim += down(line)
        aim += up(line)
        x   += forward(line)
        y   += aim*forward(line)
##        print('Running aim:         ',aim)
##        print('Running horizontal:  ',x)
##        print('Running depth:       ',y)
        

    print('Position horizontal:  ',x)
    print('Position depth:       ',y)
    print('ANSWER             :  ',x*y)

f.close()

import os
data=open('sketch.txt')
for i in data:
    if i.find(":")==-1:
        print i
    else:
        (role,word)=i.split(':',1)
        print role,"said:",word
    if raw_input()=="":
        continue

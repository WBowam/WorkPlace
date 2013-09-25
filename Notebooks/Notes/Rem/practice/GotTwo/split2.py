import os
data=open('sketch.txt')
for i in data:
    try:
        (role,word)=i.split(':',1)
        print role,"said:",word
    except:
        print i          
    if raw_input()=="":
        continue
data.close()

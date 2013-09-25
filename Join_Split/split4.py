import os
man=[]
otherman=[]
try:
    with open('sketch.txt') as data:
        for target1 in data:
            target1=target1.strip()
            try:
                (role,word)=target1.split(':',1)
                print(role+':'+word)
            except:
                print(target1)
            if role=="Man":
                man.append(word)
            elif role=="Other Man":
                otherman.append(word)
            if input()=="":
                continue
    with open('man2.out','w')as manout,open('otherout2.out','w')as otherout:
        print(man,file=manout)
        print(otherman,file=otherout)
except IOError as err:
    print('File missing!'+str(err))

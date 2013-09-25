import os
man=[]
otherman=[]
try:
    
    data=open('sketch.txt')
    for i in data:
        try:
            (role,word)=i.split(':',1)
            word=word.strip()
            if role=="Man":
                man.append(word)
            else:
                otherman.append(word)
        except:
            pass
        outman=open("manout.out","w")
        outother=open("otherout.out","w")
        print(man,file=outman)
        print(otherman,file=outother)
        
        
except IOError as err:
    print ("the datafile is missing!"+str(err))
finally:
    if 'outman' in locals() and 'outother' in locals():
        outman.close()
        outother.close()


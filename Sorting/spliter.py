import os
try:
    
    with open('james.txt') as data_all:   
        for target1 in range(8):        
            (mem,data_all)=data_all.strip().split(',',1)
            list1.append(mem)
        list1.append(data_all)
    print(list1)
except IOError as error:
    print(error)

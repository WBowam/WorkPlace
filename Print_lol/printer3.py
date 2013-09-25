#printer3.1
#indent:缩进
test1=[1,[2,[3,[4,[5,[6,7,8,9]]]]]]
if input("indent or not?Y/N")=='Y':
    bool1=True
else:
    bool1=False
def printer(the_list,level=0,indent=bool1):
    for i in the_list:
        if isinstance(i,list):
            printer(i,level+1)
        else:
            if indent==True:                                            
                for i2 in range(level):
                    print('\t',end='')
            print(i)
printer(test1,2)

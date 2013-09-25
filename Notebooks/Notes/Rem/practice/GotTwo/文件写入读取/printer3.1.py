#printer3.1
#indent:缩进
test1=[1,[2,[3,[4,[5,[6,7,8,9]]]]]]
list_in=[]
i_tab=''
if input("indent or not?Y/N")=='Y':
    bool1=True
else:
    bool1=False
def printer(the_list,level=0,indent=bool1,filepath='sys.stdout'):
    for i in the_list:
        if isinstance(i,list):
            printer(i,level+1)
        else:
            if indent==True:                                            
                for i2 in range(level):
                    print('\t',end='')
                    
            print(i)
            try:
                with open('sys.stdout','a') as data:                   
                    print(i,file=data)
            except IOError as error:
                print('File write wrong!'+str(error))
printer(test1,2)

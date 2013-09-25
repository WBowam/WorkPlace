#printer4
#indent:缩进
import os,time
test1=[1,[2,[3,[4,[5,[6,7,8,9]]]]]]
list_in=[]
i_tab=''
if input("indent or not?Y/N")=='Y':
    bool1=True
else:
    bool1=False
dir_input=input("请输入写入文件的目录及文件：")
if not os.path.exists(dir_input):
    dir_input='sys.stdout'
def printer(the_list,level=0,indent=bool1,filepath=dir_input):
    for i in the_list:
        if isinstance(i,list):
            printer(i,level+1)
        else:
            if indent==True:                                            
                for i2 in range(level):
                    print('\t',end='')
                    
            print(i)
            try:
                with open(filepath,'a') as data:                   
                    print(i,'-----',time.strftime('%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())),file=data)
            except IOError as error:
                print('File write wrong!'+str(error))
print(time.strftime('%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())))
printer(test1,2)

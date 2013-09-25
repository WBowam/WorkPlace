#printer4
#indent:缩进
import os,time
#coding=utf-8
###存在的问题：当文件存在时读取正常，但怎么还是输出怀疑字样啊？
print('使用说明：输入reader()开始读取你想要读取的文件，然后输入printer()开始打印你已读取的文件内容到你想要的文件中，这过程中内容也会被打印在屏幕，如果你觉得这样不够隐私，请升级本软件到最新版本！！！千万不要怀疑我的判断！！！')

###以下为读取部分
list_read=[]
dir_read=''
def reader():
    global dir_read

    dir_read=input("请输入读取文件的目录及文件：")
    if not os.path.exists(dir_read):
        dir_read='nonpath.txt'
    try:
        with open(dir_read) as data:
            for target1 in data:
                list_read.append(target1)
    except IOError as error:
        pass



    
###以下为写入部分
#test1=[1,[2,[3,[4,[5,[6,7,8,9]]]]]]##3版本input模块中使用的实验列表


def printer(level=0):
    if input("你要写入的文件如果是嵌套列表，缩进吗？Y/N")=='Y':
        indent=True
    else:
        indent=False
    dir_input=input("请输入写入文件的目录及文件：")
    if not os.path.exists(dir_input):
        dir_input='sys.stdout'
    for i in list_read:
        if isinstance(i,list):
            printer(i,level+1)
        else:
            if indent==True:                                            
                for i2 in range(level):
                    print('\t',end='')                   
            print(i)
            try:
                with open(dir_input,'a') as data:                   
                    print(i,'-----',time.strftime('%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())),file=data)
            except IOError as error:
                print('File write wrong!'+str(error))
            if dir_read=='nonpath.txt':
                print('按‘h’键怀疑我！，其他键继续')
                if  input()!='h':
                    break
                else:
                    continue
print(time.strftime('%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())))
print (list_read)

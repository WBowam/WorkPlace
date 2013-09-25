james=[]
#转list
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return(data.strip().split(','))
    except IOError as ierror:
        print('File error:'+str(ierror))
        return(None)
###格式化列表项
def sanitize(time_string):
    if '-' in time_string:
        spliter='-'
    elif ':' in time_string:
        spliter=':'
    else:
        return(time_string)
    (min,secs)=time_string.split(spliter)
    return(min+'.'+secs)


###输出最终结果
##james=get_coach_data('james.txt')
##print(sorted(set([sanitize(t) for t in james]))[0:3])

sarah=get_coach_data('sarah2.txt')
(sarah_name,sarah_dob)=sarah.pop(0),sarah.pop(0)
print(sarah_name+"'s fastest times are:"+str(sorted(set([sanitize(t) for t in sarah]))[0:3]))


            

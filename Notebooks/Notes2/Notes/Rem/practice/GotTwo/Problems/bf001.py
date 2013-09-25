#####sanitize
'''
def sanitize(the_string):
    if '-' in the_string:
        spliter='-'
    elif ':' in the_string:
        spliter=':'
    else:
        return(the_string)
    (min,sec)=the_string.strip().split(spliter)
    return(str(min.sec))
'''
import sanitize
with open('james.txt') as jaf:
    data=jaf.readline()
    james=data.strip().split(',')
with open('time/julie.txt') as juf:
    data=juf.readline()
    julie=data.strip().split(',')
clean_james=[]
#clean_julie=[]
for i in james:
    clean_james.append(sanitize(i))
print(clean_james)







    


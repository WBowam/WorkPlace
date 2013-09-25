def sanitize(the_string):
    if '-' in the_string:
        spliter='-'
    elif ':' in the_string:
        spliter=':'
    else:
        return(the_string)
    (min,sec)=the_string.strip().split(spliter)
    return(str(min.sec))

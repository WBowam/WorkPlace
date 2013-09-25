def find_same(items,test):
    same=[]
    for i in items:
        for t in test:
            if t==i:
                same.append(t)
                #print("found"+' '+t+' '+'in'+' '+items)
                break
            else:
                continue
    print('same items:'+str(sorted(set(same))))

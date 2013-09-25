same=[3,4]
def find_same(items,test):
    global same=[1,2]
    for i in items:
        for t in test:
            if t==i:
                same.append(t)
                #print("found"+' '+t+' '+'in'+' '+items)
                break
            else:
                continue
    print('same items:'+str(sorted(set(same))))

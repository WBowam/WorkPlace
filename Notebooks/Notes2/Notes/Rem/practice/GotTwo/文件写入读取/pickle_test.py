import pickle
with open('test_in.txt','wb') as data_in:
    pickle.dump('{a:1,b:2}',file=data_in)
with open('test_in.txt','rb') as data_out:
    list1=pickle.load(data_out)
print(list1)

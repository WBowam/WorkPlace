import pickle
with open('mydate.pickle','rb')as out_data:
	list1=pickle.load(out_data)
with open('1.txt','a')as out_dir:
	print(list1,end='',file=out_dir)

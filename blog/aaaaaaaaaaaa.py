l = [233,44,55,4,5,41,405,666,2232]
l.sort(reverse=True)
for i in l[::-1]:
    print(i)
print(l)


list = {'1':3,'2':4,'4':1}
list = dict(sorted(list.items(),key=lambda x:x[1],reverse=True))
print(list)
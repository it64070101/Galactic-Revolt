mylist = [1,2,3,4]
yourlist = {'haha' : 1, 'hoho' : 20}
for i in yourlist.values():
    if i in mylist:
        print('yes', i)
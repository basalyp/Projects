def FD(mylist):
    dexist = []
    sortlist = mylist
    sortlist.sort()
    for i in sortlist:
        if (i*2) in (sortlist):
            dexist.append(i)
    print (dexist)

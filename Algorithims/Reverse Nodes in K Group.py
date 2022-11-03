def knode(head,k): # where heas is a linked list and K is the nodes of the list
    pos1=0
    pos2=k
    outputlist=[]
    lenhead = len(head)
    loops = lenhead/int(k) # To avoid that a for loop goes beyond the amount of list changes
    for i in range (int(loops)):
        listchanged = head[pos1:pos2]
        listchanged.reverse()
        outputlist.extend(listchanged)
        pos1=pos1+k
        pos2=pos2+k
    outputlist.extend(head[pos1:])
    print (outputlist)
        
        

def areacode(file):
    openfile = open(file,'r') #Open File
    readfile= openfile.read() #Set file to read
    Uniquecode = []           #An empty list that is empty to append the Unique codes in 
    listopenfile = list(readfile.split("\n"))  #Splitting the file by new line & creating a list of the numbers
    for i in listopenfile:                     #For loops for all arrays in the set
        if i[0:3] not in Uniquecode:           #[0:3] is the area code
            Uniquecode.append(i[0:3])
    x = len(Uniquecode)
    print ("The number of unique codes are {} where they are {}".format(x,Uniquecode))
    
            
    
'''
This Code is meant to get the Unique codes in a text viles given there are only Phone Numbers

The program has  a problem that even if a normal line was written in text, it will append it as a unique code so our assumtion only phone numbers are in
the textfile.

We can make a list with only the three digits and then use the unique Function
'''

def swapping():
    #file 1 read
    file1=input("Enter your file name:-")
    f=open(file1,'r')
    fileContents=f.read()
    print(fileContents)

    #file2 read
    file2=input("Enter file 2 pls:-")
    g=open(file2,'r')
    fileContents2=g.read()
    print(fileContents2)

    #opening files again
    f=open(file1,'w')
    g=open(file2,'w')

    #swapping contents
    f.write(fileContents2)
    g.write(fileContents)

    #closing contents
    f.close()
    g.close()
swapping()

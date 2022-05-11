def countWordsFromFile():
    fileName=input("enter the file name = ")
    file=open(fileName,"r")
    words=0
    for line in file:
        w=line.split()
        words=words+len(w)
    print("words=",words)
countWordsFromFile()
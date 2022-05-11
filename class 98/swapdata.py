def swapData():
    file1=input("enter 1st file name =>")
    file2=input("enter 2nd file name =>")
    with open(file1,"r") as z:
        f1=z.read()
    with open(file2,"r") as a:
        f2=a.read()
    with open(file1,"w") as x:
        x.write(f2)
    with open(file2,"w") as y:
        y.write(f1)
swapData()
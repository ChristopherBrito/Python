Stud = ['who', 'what', 'where', 'when', 'how']
print(Stud)#prints everything in list
print(Stud[1])#prints whats in that index
Stud[1] = "Whence"#changes whats in that index into what you write
print(Stud)
Stud[3] = 25#You can input any variable
print(Stud)
def main():
    Stud = ['who', 'what', 'where', 'when', 'how']
    printListWithIndices(Stud)
    
def printListWithIndices(someList):
    length = len(someList)
    for i in range(-1, -length-1, -1):
        print(f"Index {i} : {someList[i]}")


main()

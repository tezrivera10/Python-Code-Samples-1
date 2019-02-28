#Raul Rivera
#2/29/18

#function receieve list and prints out only the unqiue elements.

def uniquelist (numbers):
    newlist =[]
    for i in numbers:
        if i not in newlist:
            newlist.append(i)
    return newlist

print (uniquelist([1,1,1,5,5,5,7,8,2,4,4,5,10]))

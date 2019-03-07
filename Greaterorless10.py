#Raul Rivera
#3/7/19
#finding if two inputs equal or greater then or less than 10.

number1 = int(input("Enter in number 1: "))
number2 = int(input("Enter in number 2: "))

def numberCheck(n1, n2):
    
    if n1 + n2 ==10:
        print ("equal")
    elif n1 + n2 > 10:    
        print ("Greater Then")
    else:
        print ("Less Than")
    

#numberCheck(number1, number2)
print (numberCheck(number1,number2))

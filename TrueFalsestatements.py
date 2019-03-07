#Raul Rivera
#3/7/19

#Finding if the inputs equals or not.

number1 = int(input("Enter in number 1: "))
number2 = int(input("Enter in number 2: "))

def numberCheck(n1, n2):
    if n1 == n2:
#        print ("True")
        return True
    else:
#        print ("False")
        return False

#numberCheck(number1, number2)
print (numberCheck(number1,number2))

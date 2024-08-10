#Filename:total-ages_NayleneRondon
#Date:02/15/2017
#Programmer: Naylene Rondon
#Purpose: Asks for two ages and add them together using the
#function Sum.

#Start

#Main Function
def main():
    """This function as the program."""
    
    #Calling Intro Function
    intro()
    
    #Input
    print("\nWhat's the first age? ")
    firstAge = int(input())
    print("\nWhat's the second age? ")
    secondAge = int(input())

    #Call Sum Function
    bothAges = Sum(firstAge, secondAge) #Returned Results 

    #Output
    print("The sum of the ages " + str(firstAge)+ " and " + str(secondAge)
          + " is " + str(bothAges) + ".")

    
#Intro Function
def intro():
    """Gives Introduction"""
    print("Welcome!")
    print("This program will return the sum of two ages.")



#Sum Function
def Sum(age1, age2):
    """Adds together the two numbers."""
    result = int(age1 + age2)   #Calculates Result
    return result  #Return result



#Program
main()  #Calling main function


#End


#Filename: greeter2_NayleneRondon.py
#Programmer: Naylene Rondon
#Date: 02/13/2017
#Purpose: Example of A Function

#Input
username = input("Enter your username: ")

#Function
def greet_user(username):    #Define Function
    """Display Simple Greeting"""  #Special Comments 
    print("Hello " + username.title() + "!")  #What the Function Does

greet_user(username)  #Call Function

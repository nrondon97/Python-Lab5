#Filename: formatted_name_NayleneRondon.py
#Programmer: Naylene Rondon
#Date: 02/13/2017
#Purpose: Example of A Function with return value

#Start

#Define Function
def get_formatted_name(first, last):
    """Return Full name formatted."""
    full_name = first + " " + last
    return full_name.title()

#Program
musician = get_formatted_name("JIMINI", "hendrick")
print(musician)

musician = get_formatted_name("micea", "wallin")
print(musician)

#End

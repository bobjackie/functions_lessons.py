#jackie and breanna
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.

def atrributions(**kwargs):

    return len(kwargs)

# Testing the function
print(atrributions(a=5, b=7, c=9))  
print(atrributions(name="pip", age=25)) 
print(atrributions()) 







# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.

def charaterics(name, **kwargs):
    print(f"Characteristics of {name}:")
   
    for key, value in kwargs.items():
        print(f"{key}: {value}")

charaterics("Nicole", eye_color="pink", hair_color="pink")











# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black


def charaterics(name, **kwargs):
    print(f"Characteristics of {name}:")
   
    for key, value in kwargs.items():
        print(f"{key}: {value}")


charaterics("Bob", eye_color="turquiose", hair_color="untoned yellow")
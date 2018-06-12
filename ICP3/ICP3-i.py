def dict_exercise(name):
    # creating a dictionary
    dictionary=dict()
    name=name.lower()

    for words in name.split():

        if words not in dictionary:
            dictionary[words]=1
        else:
            dictionary[words]+=1
    return dictionary

# taking input from user
name=input("enter a string")
print(dict_exercise(name))
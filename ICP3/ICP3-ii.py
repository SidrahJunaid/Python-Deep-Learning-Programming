def vowel_count(string):
    # create set for vowels
    vowels=set("aeiou")
    count=0
    string=string.lower()
    for a in string:
        if a in vowels:
            count+=1
    print("Number of vowels in string "+str(count))

string="my name is sidrah"
vowel_count(string)

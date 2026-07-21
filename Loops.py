name = ["Suresh","Ramesh","Naresh","Paresh","Haresh","Rajesh"]
height_inches = [67,66,70,73,69,72]
min_height_inches = 67
max_height_inches = 72
for index, (name, height_inches) in enumerate (zip (name, height_inches)):
    if height_inches <= min_height_inches :
        print (name,"The actor", height_inches, "is lower than character requirement in play, hence rejected for casting")
    elif height_inches >= max_height_inches:
        print (name,"The actor", height_inches, "is higher than character requirement in play, hence rejected for casting")
    else:
        print(name,"The actor", height_inches, "is matching the character requirement in play, hence shortlisted for casting")
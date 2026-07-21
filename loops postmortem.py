names= ["Suresh","Ramesh","Naresh","Paresh","Haresh","Rajesh"]
height_inches = [67,66,70,73,69,72]
min_height_inches = 67
max_height_inches = 72
for name, height in zip (names, height_inches):
    if height <= min_height_inches:
        print (name,"The actor",height,"is less than character requirement in play hence rejected")
    elif height >= max_height_inches:
        print (name,"The actor",height,"is more than character requirement in play hence rejected")
    else: 
        print (name,"The actor",height,"is as per character requirement in play hence shortlisted")
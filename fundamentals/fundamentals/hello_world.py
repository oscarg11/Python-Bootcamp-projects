# 1. TASK: print "Hello World"
print("Hello World")
# 2. Print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello",name) #with comma
print("Hello " + name) # with +
# 3. print "Heloow 42!" with the number in a variable
name = 42
print("Hello",name,"!") #with comma
print("Hello " + str(name) + "!") #with + (fixed error by casting name to be a string)
# 4 print "I love to eat sushi and pizza." with the food in the variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) #with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") #with f string
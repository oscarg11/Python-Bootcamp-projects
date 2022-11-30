#1.) Basic - Print all integers from 0 to 150.
print("question 1:")
for i in range(0,151):
    print(i)

#2.) Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("question 2:")
for m in range(5,1001):
    if m % 5 == 0:
        print(m)
#or 
#for m in range (5, 1001,5)
#    print(m)

#3.) Counting, the Dojo Way - print integers 1 to 100.
#if divisible by 5, print "Coding" instead. 
#if divisible by 10, print "Coding Dojo"
print("question 3:")
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#4.) Whoa. That sucker's huge - Add odd integers from 0 to 500,000.
#and print the final sum
print("question 4")
sum = 0
for o in range(0, 500001):
    if o % 2 != 0:
        sum += o
        print(o)
print(" the final sum is ", sum)

#5.) Countdown by fours - print positive numbers starting at 2018,
#counting down by fours
print("question 5:")
for i in range(2018,0,-4):
    print(i)

#6.) Flexible Counter - Set three variables: lowNum, highNum, mult.
#starting at lowNum and going through highNum, print only the integers that are 
#a multiple of mult.
#For example if lowNum = 2, highnum = 9, and mult = 3, the loop should print 3,6,9(on succesive lines)
print("question 6:")
lowNum = 2
highNum = 10
mult = 3
for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)

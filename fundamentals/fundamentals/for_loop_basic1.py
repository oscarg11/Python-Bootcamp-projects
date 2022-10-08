# 1. Basic - Print all integers from 0 to 150
print("all integers from 0 to 150")
for i in range(151):
    print(i)

# 2. Multiples of 5 - Print all mulitples of 5 from 5 to 1,000
print("all multiples of 5 from 5 to 1,000")
for i in range(5,1001):
    if i%5==0:
        print(i)

# 3. Counting, the Dojo way - Print integers from 1 to 100. If divisible by 5, print "coding" instead.
#if divisible by 10 print, print "Coding Dojo"
print("(3. Counting the Dojo Way)")
for i in range(1, 101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

# 4. Add odd integers from 0 to 500,000 and print the final sum
print("4 .(add all odd integers from 0 to 500,000 and prints the final sum)")
total=0
for i in range(500001):
    if i % 2 != 0:
        total=total + i
print("Sum of all odd numbers is",total)

# 5. Countdown by Fours - Print positive numbers starting at 2018, conting down by fours
print("5. print positive numbers starting at 2018, counting down by fours.")
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult.
#starting at lowNum and going through highNum, print only the integers
#that are a multiple of mult. For example, if lowNum =2, highNum = 9, and mult =3,
#the loop should print 3,6,9 (on succesive lines)
print("question 6")
lowNum =2
highNum =9
mult = 3
for i in range(lowNum, highNum + 1):
    if i% mult ==0:
        print(i)
# 1) Countdown - Create a function that accepts a number as an input
#Return a new list that counts down by one, from the number
#(as the 0th elment) down to 0 (as the last element)
print("1.) Countdown")
def countDown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
    print(list)
numbers = countDown(10)
print(numbers)

# 2) Print and Return - Create a function that will recieve a list with two
#numbers. Print the first value and return the second.
print("2.) Print and return")
def print_and_return():
    


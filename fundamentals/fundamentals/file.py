num1 = 42 #variable declaration number
num2 = 2.3
boolean = True#boolean
string = 'Hello World'#string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#tuple
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))#type check
print(pizza_toppings[1])#access value
pizza_toppings.append('Mushrooms')#add value
print(person['name'])
person['name'] = 'George'#add value
person['eye_color'] = 'blue'# add value
print(fruit[2])#access value

if num1 > 45:#if
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:#else if
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):#for loop start
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()#delete value
pizza_toppings.pop(1)# access value and delete it

print(person)
person.pop('eye_color')#access value and delete
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
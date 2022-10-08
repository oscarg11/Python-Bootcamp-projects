#1.) Update the values in Dictionaries and Lits
print('1)------------')
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#a.) change the value 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]]
x[1][0]=15
print(x)

#b.) change the last_name of the first student from "Jordan" to "Bryant"
print('------------')
students[0]["last_name"]= "Bryant"
print(students[0])

#c.) In the sports_directory, change "messi" to "andres"
print('------------')
sports_directory['soccer'][0]="Andres"
print(sports_directory)

#d.)change the value 20 in z to 30
print('------------')
z[0]["y"]=30
print(z)
#2.) Interate through a List of Dictionaries
#create a function iterateDictionary(some_list) that, given a list of dictionaries, the
#function loops through each dictionary in the list and prints each key and the associatied value

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
print('2)------------')
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'}, #index 0
    {'first_name' : 'John', 'last_name' : 'Rosales'},   #index 1
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},   #index 2
    {'first_name' : 'KB', 'last_name' : 'Tonel'}        #index 3
    ]
def iterateDictionary(x):
    for index in range(len(x)):
        for key, value in x[index].items():
            print(key, "-", value)

iterateDictionary(students)

#3. Get values form a Lis of Dictionairies -

#Create a function 'iterateDictionary2(key_name, some_list)
#that, given a list of dictionaiiries and key names, the function
#prints the value stored in that key for each dictionary.
print('3)------------')
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#4. Iterate Through a Dictionary with List Values-
#create a function 'printInfo(some_dict) that given a
#dictionary whose values are all list, prints the name of each
#key alonng with the size of its list, and then prints the 
#associated values within each key's list.
print('4)------------')
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(someDict):
    for key, values in someDict.items():
        print(len(values),key.upper())
        for i in values:
            print(i)
printInfo(dojo)

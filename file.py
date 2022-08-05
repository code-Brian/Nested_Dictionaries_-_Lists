# Here we go! We got this.😎
# 1. Update Values in Dictionaries and Lists
    # 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ] 
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
    # 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)

    # 3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

    # 4. Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)

# 2. Iterate Through a List of Dictionaries
    # Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
    # the function loops through each dictionary in the list and prints each key and the 
    # associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(0, len(list)):
        print(list[i]["first_name"], list[i]["last_name"])

# Question 2: Bonus for formatting
def iterateDictionaryBonus(list):
    for i in range(0, len(list)):
        print(f"first_name - {list[i]['first_name']}, last_name - {list[i]['last_name']}")

iterateDictionary(students) 
iterateDictionaryBonus(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

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

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'andres'
z[0]['y'] =30

print("===========================")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(list):
    for i in range(0,len(list)):
        for key,vul in list[i].items():
            print(f"{key}, {vul},")

def iterateDictionary2(first_name, list) :
    for i in range(len(list)):
        print(list[i]["first_name"])

def iterateDictionary3(last_name, list) :
    for i in range(len(list)):
        print(list[i]["last_name"])

iterateDictionary(students)
iterateDictionary2(students, students)
iterateDictionary3(students, students)

print("============================")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    for i in dojo:
        print(f"{len(dojo[i])} {i}")
        for j in dojo[i]:
            print(j)
            
printInfo(dojo)



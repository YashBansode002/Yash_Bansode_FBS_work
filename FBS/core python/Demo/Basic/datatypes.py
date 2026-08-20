### numarical 
#1 int

var=10

#2 float 
var=3.14

print(type(var))

#3 comoplex
var = 10+5j #real +imagniary 

### Text 
#1 string
var = '''this us first bit solution '''
var = """this
is
first bit solution var """
var= '''this is first line 
this is second line 
this is therd line 
this is fourth line 
this is the fifth line '''

print(type(var))

### sequential 
#1 list 
var = [10,20,30,40]

#2 tuple 
var=(10,20,30,40)

#3 range
var=range(1,10)

print(type(var)) 

### set type 
#1 set
var={10,20,30,40}

#2 frozenset
var=frozenset({10,20,30,40})

print(type(var))

### mapping
#1 dict 
var = {1:'python',2:'java',3:'c'}

print(type(var))

#### other
#1 bool
var= True

#2 nonetype
var=None
print(type(var))
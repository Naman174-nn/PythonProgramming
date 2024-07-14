# a ={
#     #key : value
#     "mouse" :"animal",
#     "naman" :"nekiye",
#     "list"  : [12,45,63],
#     "number" : 54,
#     "float"  : 0.21,
#     "boolean": False,
#     "nothing": None,
#     "dictionary":{
#         "dict1": 54,
#         "anotherdictionary" : {
#             "dict2": 87
#         }
#     }

# }



#Dictionary Methods

# print(tuple(a.keys()))

# print(type(a))

# print(a.values())
# print(a.items())

# b = {
#     'nam' : 'nek'
# }

# print(
#     a.update(b)
# )
# print(a)

# print(a.get('naman'))#returns none if key not present in dictionary
# print(a['naman'])#throws error if key not present in dictionary


# print( a["mouse"]) 
# print( a["naman"]) 
# print( a["list"]) 
# print( a["number"]) 
# print( a["float"]) 
# print( a["boolean"]) 
# print( a["nothing"]) 
# print( a["dictionary"]) 
# a["dictionary"]['anotherdictionary']['dict2'] = 99
# print( a["dictionary"]['anotherdictionary']['dict2']) 



#sets


# a = {} #empty dictionary

# print(type(a))

# b = set()

# b.add(4)
# b.add('naman')

# b.add({
#     'name': 'naman'  #we can change its contains so we cant add dictionary 
#                      # and lists in sets
# }) 
#if datatype is not hashable we cant add it to sets
#hashable = cannot be changed

# print(b)


 
# a = {2,3,5,87}


# print(len(a)) #prints the length of this set


# a.remove(2) #remove 2 from set
# a.remove(12)
# print(a.union({3,5,8}))
# print(a.intersection({3,5,8}))

# print(a)


#practice set 


#1
 

'''write a program so that user can search any word from the dictionary'''

# t = {
#     "seb" : 'apple',
#     'gadi': ' bike',
#     'vidyalaya' : 'school'
# }

# a = input('search anything to translate: ')

# print('the meaning of your entered word is:', t.get(a))


#2

''' write a program to input eight numbers from the user and display all
  the unique numbers(once)'''


# a = input('enter your 1 number:')
# b = input('enter your 2 number:')
# c = input('enter your 3 number:')
# d = input('enter your 4 number:')
# e = input('enter your 5 number:')
# f = input('enter your 6 number:')
# g = input('enter your 7 number:')
# h = input('enter your 8 number:')


# l = {a,b,c,d,e,f,g,h}

# print(l)


#3

'''can we have a set with 18(int) and "18"(str) as a value in it'''

# a = {18,'18'}
# print(len(a)) #prints 2
# print(a) # both elements will be printed

#4

'''what will be the length of following set s 
   s =set()
   s.add(20)
   s.add(20.0)
   s.add('20')
'''

# s =set()  #this is empty set right now
# s.add(20)
# s.add(20.0)
# s.add('20')
# # s= {20,20.0,'20'}  20 will be counted one time


# print(s)
# print(len(s))


#5 
'''s= {}  what is the type of s '''

# s = {}  # type of set will dict
# print(type(s))


#5
'''Create an empty dictonary. allow 4 friends to enter thier favorite 
   language as values and use keys as their names. Assume that the
   names are unique'''

# dict = {}

# Friend_one_name = input('Enter your name:\n')
# Friend_one_lang = input ('Enter your favorite language:\n')

# Friend_two_name = input('Enter your name:\n')
# Friend_two_lang = input ('Enter your favorite language:\n')

# Friend_three_name = input('Enter your name:\n')
# Friend_three_lang = input ('Enter your favorite language:\n')

# Friend_four_name = input('Enter your name:\n')
# Friend_four_lang = input ('Enter your favorite language:\n')

# TobeUpdated= {
#     Friend_one_name : Friend_one_lang,
#     Friend_two_name : Friend_two_lang,
#     Friend_three_name : Friend_three_lang,
#     Friend_four_name : Friend_four_lang
# }

# dict.update(TobeUpdated)
# print(dict)

#if any two friends name are same,then the recently updated value will overwrite the old value


# 7 
'''can you change the values inside a list which is contained in 
   set s
  
'''
# s =  {8,7,12,'harry',[1,2]}
# print(s)
# list is not hashable so we cant store list in set s






































































































































































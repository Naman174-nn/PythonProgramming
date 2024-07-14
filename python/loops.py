
# i=0
# while i <10:
#     print('yes ' + str(i))
#     i = i+2

# i=1
# while i<51:
#     print(i)
#     i = i+1

# fruits = ['mangoes','banana','grapes','litchi']

# i = 0 
# while i < len(fruits):
#     print(fruits[i])
#     i = i+1


'''For loop'''


# l = [1,7,8]

# for item in l:
#     print(item)

# fruits = ['mangoes','banana','grapes','litchi']

# for item in fruits:
#     print(item)
# else:
#     print('no item')

# for i in range(9,19,2):
#     print(i)



'''The break statement'''



# for i in range(0,10):
#     print(i)
#     if i == 7:
#         break
# else:
#     print('this is inside else of for')



'''The continue statement'''

# for i in range(4):
#     print('printing')
#     if i == 2:
#         continue
#     #code will not look below if i = 2 and will run for i = 3 
#     print(i)



'''Pass Statment'''
#pass is a null statement in python.it instructs the code to do nothing.without it code will throw error

# i = 4

# if i>0:
#     pass


# def num(a,b):
#     pass







'''1)Write a program to print multiplication table of a given number using
    for loop'''

# num = int(input('Enter a number :'))

# list  = [num * 1 = num*1 , num*2,num*3,num*4,num*5,num*6,num*7,num*8,num*9,num*10,]

# for item in list:
#     print(item)



'''2)Write a program to print multiplication table of a given number using
   while loop

'''

# num = int(input('Enter a number :\n'))

# i = 1
# while (num*i <= num*10):
#     print(num*i)
#     i = i+1   

'''3)Write a program to greet all the person names stored in a list l1 and 
   which starts with S'''

'''my attempt 1 '''
# l1 = ["Harry","Sohan", "Sachin" ,"Rahul"]

# i = 0
# while ('s' or 'S' in l1[i] and i<len(l1) ):
#     print('Congratulations' , l1[i])
#     i = i+1
'''attempt > 2'''
# l1 = ["Harry","Sohan", "Sachin" ,"Rahul"]

# for name in l1:
#     if name.startswith('S' or 's'):
#         print('Hello ' + name)
# else:
#     pass


 
'''4)Write a program to find whether a given number is even or prime'''


# num = int(input('Enter a number:'))

# if(num%2 == 0):
#     print('This is even number')

# else:
#     print('This is odd number')


'''5)Write a program to find whether a given number is prime or not'''

'''******************************************'''

# num = int(input('Enter a number:\n'))

# prime = True
# for i in range(2,num):
#     if(num%i == 0 ):
#         prime = False
#         break
# if prime :
#     print('This number is prime')
# else:
#     print('This number is not prime')              



'''6)write a program to find the sum of first n natural numbers using while loop

'''
n = int(input('Enter a number:\n'))

print()
    
    





'''7)write a program to calculate the factorial of a given number using for loop

'''








'''8)write a program to print following star pattern:
        *
       ***
      *****    for n = 3
'''







'''9)write a program to print the following star pattern:

      *
      **
      ***    for n = 3

'''







'''10)write a program to print the following star pattern:
      * * *
      *   *        
      * * *         for n = 3

'''










'''11)write a program to print multiplication table of n using for loop in reversed order

'''





















































































































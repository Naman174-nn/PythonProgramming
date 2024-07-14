
# a = 22

# if (a < 21):
#     print('True')
# elif (a < 23):
#     print('Yes')
# else :
#     print('Maybe')
  


# if(2+4 == 5):
#     print('yes its true')                          

# else:
#     print('no its wrong')    


# weather_bad = 'its raining'
# weather_good= 'its not raining'

# if (weather_bad):
#     print('i will not go to office')
  
# else:
#     print('i will go to office')


# flo= 21.2
# print(int(flo))
# if(int(flo)==21 ):
#     print('Equal')
# else:
#     print('Not equal')    
'''Program to detect whether entered age by user is valid or no'''

# age = input('Enter your age\n')

# if(int(age) >= 18):
#     print('Allowed')
# else:
#     print('Not allowed')

# num1 = 18
# num2 = 2
#and = true if both operands are true elsefalse         
#or = true if at least one operand is true else false
#not = inverts true to false and false to true


# if( not int(num2) == 18):
#     print('true')
# else:
#     print('false')



# a = None
#what does 'is' do  = both a and none points to same object so its true
# if(a is None):
#     print('yes')
# else:
#     print('no')




# a = [54,65,98,31]
#in = checks if given integer is inside the list
#in = can be used to iterate list using for loop
# if(58 in a ):
#     print('yes')
# else:
#     print('no')    



# if(2>6):
#     print('true')
# elif(2<1):
#     print('false')

'''else is optional'''

   

'''practice set'''


'''1) Write a program to find greatest of four numbers entered by the user'''


# num1 = int(input('Enter first number:\n'))
# num2 = int(input('Enter second number:\n'))
# num3 = int(input('Enter third number:\n'))
# num4 = int(input('Enter fourth number:\n'))

''' method - 1 '''
# list = [num1,num2,num3,num4]

# list.sort()
# print(list[-1])


'''method 2 '''

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#    f2 = num2
# else:
#    f2 = num3   

# if(f1>f2):
#     print('greatest number of the four is', f1)
# else:
#     print('greatest number of the four is', f2)



'''2)Write a program to find out whether a student is pass or fail ,if it
   requires total 40% and at least 33% in each subject to pass. Assume
   3 subjects and take marks as an input from the user.
'''

# total of 3 = 300 marks,individual = 100 marks

# Maths = int(input('Enter Maths Marks:\n'))
# English = int(input('Enter English Marks:\n'))
# Hindi = int(input('Enter Hindi Marks:\n'))


# if(Maths <=33) :
#     print('fail')
# elif(English <=33) :
#     print('fail')
# elif(Hindi <=33) :
#     print('fail')
# elif(Maths+English+Hindi < 120 ):
#    print('fail')    
# else:
#     print('pass')   


'''3) A spam comment is defined as a text containing following keywords:
     "make a lot of money","buy now","subscribe this","click this".
      write a program to detect these spams.

'''


# comment = input("Enter the text:\n")

# if('make a lot of money' in comment):
#     spam = True
# elif('buy now' in comment):
#     spam = True
# elif('subscribe this' in comment):
#     spam = True
# elif('click this' in comment):
#     spam = True
# else:
#    spam = False

# if(spam):
#     print('This is a spam.BLOCKED!!')
# else:
#     print('This is not a spam')    


'''4)Write a program to find whether a given username contains less than
     10 characters or not
'''

# username = input('Enter a username:\n')


#this one is wrong when username contains 9 characters.
# if(username.count('') < 10):
#     print('The username contains less than 10 character')
# else:
#     print('The username contains more than 10 character')  

#this one is correct
# username = input('Enter a username:\n')

# if(len(username) < 10):
#     print('The username contains less than 10 character')
# else:
#     print('The username contains more than 10 character')    


'''5)Write a program which finds out whether a given name is present in a list or not.
'''
# name = input('Enter your name to be checked in list:')
# list = ['naman','mango','potato','brocolli','litchi']

# if(name in list ):
#    print('your name is present in list')
# else:
#    print('your name is not present in list')   



'''6)Write a program to calculate the grade of a student from his marks from the following scheme:

90-100 = Ex
80-90 = A
70-80 = B
60-70 = C
50-60 = D
<50 = E

'''

# marks = float(input('Enter your marks:\n'))

# if(marks >= 90):
#     print("Your grade is Excellent")
# elif(marks >= 80 and marks <90):
#     print("Your grade is A")
# elif(marks >= 70 and marks<80):
#     print("Your grade is B")
# elif(marks >= 60 and marks<70):
#     print("Your grade is C")
# elif(marks >= 50 and marks<60):
#     print("Your grade is D")
# else:
#     print("Your grade is E")
    


'''7)Write a program to find out whether a given post is talking about "naman" or not

'''
#we used string aman instead of naman in case the name is in uppercase or lowercase

# name = 'aman'
# post = input('Enter anything: ')

# if(name in post):
#     print('it is talking about naman')
# else:
#     print('it is not talking about naman')    


























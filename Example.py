# Example 01
# message = 'hello world !'
# print(message)


# Example 02
"""name= "mohammadreza"
family = 'vossoughi'
age = 37
ave= 18.35
x = True
y = False
print(name+" "+family+" "+str(age) + " years old ")
print(f"{name} {family} {age} years old")"""


# Example 03
"""name = input('pls enter your name  :')
family = input('pls enter your lastname ;')
age  = int(input('pls enter your age ; '))
fullname = name+" "+family +" "+ str(age)
print(fullname)"""

# Example 04
"""name = input('pls enter your name  :')
family = input('pls enter your lastname ;')
age  = int(input('pls enter your age ; '))
fullname = name+" "+family +" "+ str(age)
print(fullname)
if age > 18:
    print("yes")
else:
    print("no")"""


# Example 05
# number = int(input("pls enter number  :"))
# if number > 0:
#     print("posetive ! ")
# elif (number < 0):
#     print("negative !")
# if(number == 0):
#     print("zero")


# Example 06
"""txt  = input("pls enter  text : ")
for item in range(5):
    print(txt)
"""


# Example 07
"""for i in range(1,11):
    print(i)"""


# Example 08
"""def get(txt):
    print(txt)


txt = "hello world !"
get(txt)"""


# Example 09
"""def mult(number):
   return number*2

number = int(input('pls enter number :'))
result = mult(number)
print(result)
"""

# Example 10
"""def proc(x):
    if x % 2 ==0:
        print("number is even")
    else:
        print("number is Odd")
number = int(input("pls enter number "))
proc(number)"""

# Example 11
# 10
# 2+4+6+8+10 = 30
"""number = int(input("pls enter your number :"))
total = 0

for i in range(1,number + 1):
    if i % 2 ==0:
        total += i
print("sum of even numbers : ",total)
print(f"sum of even nubers : {total}")
"""

# Example 12
"""x = int(input('pls enter number 1 :'))
y = int(input('pls enter number 2 :'))
z = int(input('pls enter number 3 :'))

if  x>=y and x>=z:
    print("the largest number is : ",x)
elif y>=x and y>=z:
    print("the largest number is : ",y)
else:
    print("the largest number is : ",z)"""


# Example 13
# word = input("enter a word : ")
# print("number of letters : ",len(word))


# Example 14
"""def calc(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b 
    elif op=="*":
        return a * b   
    elif op=="/":
        if b == 0:
            return "Error : divisuon by  zero  !"
        return a/b   
    else:
        return " Invalid Opretator !"
    

a = int(input("pls first number : "))
b = int(input("pls second number : "))
op = input("Enter opretor  (+,-,*,/) : ")
result = calc(a,b,op)
print(f"the result is  : {result} ")

"""



# Example 15
"""def get_int_input(propmt):
    while True:
        try:
            return int(input(propmt))

        except ValueError:
            print('please enter a vaild inteage ! ')

a= get_int_input("Enter First  number : ")
b =get_int_input("Enter second number : ")
print("sum : ",a+b)"""


# Example 16
secret_number  = 3
while True:
    guess = int(input("Geuss the number  : "))
    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print("Correct ! ")
        break


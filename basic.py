#Write a program to check if a number is positive or negative.

'''
num=int(input("enter a number :"))
if(num<0):
    print("the give number is negative")
elif(num>0):
    print("the given number id positive")
else:
    print("the number is zero")

'''

#Write a Python program to check if a number is even or odd.
'''
num=int(input("enter a number:"))
if(num%2==0):
    print("the given number is even:")
else:
    print("the given is odd")
'''

#check whether a number is divisible by 5
'''
num=int(input("enter a number"))
if(num%5==0):
    print("divisble by 5")
else:
    print("it is not divisible by 5")
'''

#Write a program to check if a person is eligible to vote (age ≥ 18)
'''
age=int(input("enter the age of the person"))
if(age>=18):
    print("the person is eligible to vote")
elif(age<18):
    print("the person must wait for 18years")
else:
    print("mention correct age")
'''

#Accept a number from the user and check if it is less than 100.
'''
num=int(input("enter the number from the user:"))
if(num<100):
    print("yes the given number is less than 100")
else:
    print("no the given number is notless than 100")
'''

#Check whether a character is a vowel or consonant.
'''
str=input("enter a character:")
if(str=='a' or str=='e' or str=='i' or str=='o' or str=='u'):
    print(str,"is vowel")
else:
    print(str,"is not a vowel")
    
'''

#Write a program to find the greater of two numbers
'''
a=int(input("enter the number"))
b=int(input("enter another number"))
if(a>b):
    print("a is big")
elif(b>a):
    print("b is big")
else:
    print("both are equal")

'''

#Accept a number and check if it is a multiple of 3 and 7.
'''
num=int(input("enter a number:"))
if(num%21==0):
    print("yes multiple of 3 and 7")
else:
    print("no not a multiple")
'''

#Check whether the input character is a digit or an alphabet.
'''
a=int(input("enter a number or a string"))
if(a>=0 and a<=9):
    print(a,"is digit")
elif(a>='a' and a<='z' or a>='A' and a<='Z'):
    print(a,"is character")
else:
    print("it is not a digit nor character")
a=input()
'''

#Write a program to check if a year is a leap year.

'''
year=int(input("enter the year"))
if(year%4==0 and (year%100!=0 or year%400==0)):
    print(year,"is a leep year")
else:
    print("not a leep year")

'''

#Find the greatest among three numbers using if-elif-else.
'''
a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print("a is big")
elif(b>c and b>a):
    print("b is big")
elif(c>a and c>b):
    print("c is big")
else:
    print("all are equal")

'''

#accept a character and determine whether it is uppercase, lowercase, digit, or special character.

'''
str=input("enter the charchter:")
if('A'<=str <='Z'):
    print("Uppercase")
elif('a'<=str<='z'):
    print("Lowercase")
elif('0'<=str<='9'):
    print("Digit")
else:
    print("spl charachter")

'''


#Given marks in 5 subjects, calculate percentage and grade using if-elif-else.

'''
name=input("enter the name of the student")
print(f"please enter the marks of {name} ")
sub1=int(input("Telugu marks="))
sub2=int(input("Hindi marks="))
sub3=int(input("Englisg marks="))
sub4=int(input("Maths marks="))
sub5=int(input("Science marks="))
sub6=int(input("Social marks="))
total=sub1+sub2+sub3+sub4+sub5+sub6
print(f"The total marks is {total}/600")
percentage=(total/600)*100
print(f"{name} got {percentage}%")

if(percentage>=90):
    print("Grade A")
elif(percentage>=80):
    print("Grade B")
elif(percentage>=70):
    print("Grade C")
elif(percentage>=60):
    print("Grade D")
elif(percentage>=50):
    print("Grade E")
else:
    print("Fail")


'''

#Accept the age and gender of a person and print "Eligible for insurance" based on:1.Age between 25 and 50 2.Gender must be "M"
'''
gender=input("Enter your Gender:")
age=int(input("Enter your age"))
if(age>=25 and age<=50):
    print("age is ok")
    if(gender=='male'):
        print("your are eligible for insurace")
    else:
        print("it is only for male")
else:
    print("your are not eligble")
'''

#Write a program to check if a triangle is valid (sum of angles = 180).
'''
angle1=float(input("enter the angle1"))
angle2=float(input("enter the angle2"))
angle3=float(input("enter the angle3"))
total=angle1+angle2+angle3
print(total)
if(total==180):
    print("it is a valid triangle")
else:
    print("try angle")
'''

#Accept three sides and check if a triangle is scalene, isosceles, or equilateral.
'''
a=float(input("enter a side"))
b=float(input("enter b side"))
c=float(input("enter c side"))
if(a==b==c):
    print("Equilateral")
elif(a==b or b==c):
    print("isosceles")
else:
    print("scalene")
'''

#Write a program to solve a simple calculator using if-elif for +, −, *, /.
'''
a=int(input("enter a value:"))
b=int(input("enter b value:"))
operator=input()
if(operator=='+'):
    print(a+b)
elif(operator=='-'):
    print(a-b)
elif(operator=='*'):
    print(a*b)
elif(operator=='/'):
    print(a/b)
else:
    print("correct values")

'''

#Check if a character is uppercase and a vowel at the same time.
'''
str=input()
vowels='A'or'E'or'I'or'O'or'U'
if('A'<=str <='Z'):
    print("yes it is a uppercase")
    if(str==vowels):
        print("yes it is vowel tooo")
    else:
        print("it is uppercase but not vowel")
else:
    print("it is not a uppercase charachter")
'''

#Accept a number and check:1.If it's a three-digit number,2.If it is even,3.If the sum of its digits is >15
'''
num = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(num))
print(digit_sum)
if num >= 100 and num <= 999:
    print("Yes, it is a 3-digit number.")
    if num % 2 == 0:
        print("It is an even number too.")
    else:
        print("It is an odd number.")
    if digit_sum > 15:
        print("The sum of digits is greater than 15.")
    else:
        print("The sum of digits is less than or equal to 15.")
else:
    print("Not a 3-digit number.")

'''

#Write a program that simulates a simple ATM menu:Check balance, deposit, withdraw, exit (use if-elif and nested if)

'''
balance=float(input("enter your bank balance"))
print("1.Check balance")
print("2.Deposit")
print("3.Withdraw")
print("4.exit")
choice=int(input("enter yoyr choice"))
if(choice==1):
    print(balance)
elif(choice==2):
    amount=float(input("enter the deposit amount"))
    if amount>0:
        balance=balance+amount
        print(f"deposit:${amount:.2f},balance:${balance:.2f}")
    else:
        print("invalid amount")
elif choice == 3:
    amount = float(input("Enter amount to withdraw: $"))
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"Withdrew: ${amount:.2f}. New balance: ${balance:.2f}")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        print("Invalid amount.")
elif(choice==4):
    print("exit from ATM,GOODBYE!")
else:
    print("choice only 1 option")

'''

#Given a number, check if it is Armstrong number (only for 3-digit).
'''
num = int(input("Enter a 3-digit number: "))
sum_of_cubes = (num // 100) ** 3 + ((num // 10) % 10) ** 3 + (num % 10) ** 3
if num == sum_of_cubes:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
'''
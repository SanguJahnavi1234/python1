#Write a program to create a string and print its length.

'''
str="jahnavi sangu"
print(len(str))
'''

#Print each character of the string "Python" using a loop.
'''
str=input("enter the string")
i=0
while i<len(str):
    print(str[i])
    i=i+1
'''

#Slice the string "HelloWorld" to get "Hello" and "World".
'''
str="HelloWorld"
print(str[:5])
print(str[5:])
'''

#Print every second character in "Programming".
'''
str="Programming"
print(str[::2])
'''


#Concatenate two strings: "Good" and "Morning".
'''
s1='Good'
s2='Morning'
print(s1+s2)
'''

#Concatenate a string with a number after converting it to string.
'''
s="Your total marks are:"
n=700
result=s+str(n)
print(result)
'''
'''
num=400
str="100"
result=num+int(str)
print(result)
'''

'''
num=int(input("enter a number:"))
for i in range(1,11):
    print(num,"X",i,"=",num * i)
'''

#Count how many times "a" appears in "banana".

'''
str="banana"
c=str.count('a')
print(c)
'''

#Write a program to reverse a string using slicing
'''
s="jahnavireddy"
print(s[::-1])
'''
#Extract "data" from "my_data_file.txt".

# str="my_data_file.txt"
# print(str[3:7])



#Check if a string is a palindrome.
'''
str=input("")
if (str==str[::-1]):
    print("it's is palindrome")
else:
    print("not a palindrome")
'''

#Count vowels and consonants in a given string.
'''
string = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
'''



'''
import calendar
month=int(input("enter month"))
year=int(input("enter year"))
cal=calendar.month(year,month)
print(cal)
'''      
#first question :
user_name= input('"your name :"')
user_age= input('"your age : "')
user_address=  input('"Address : street : "') + ' ' + "," + input('"city : ') + ' ' + "," + input ('"country : "')
 #user_country = input ('"country : "')
age= int(user_age) - 5
msg =  'hello' + ' ' + user_name +' ' + 'how are you ?  ' +  '  ' +   '\n your age is :'  + ' ' +  str(age) + '  ' + '\n your address is : ' + ' '+ user_address

print(msg)
print(type(msg) )
print(type(user_name) )
print(type(user_age) )
print(type(user_address) )

#second question :
# name = 'Doaa Reem'
# print('First Letter Is :\t ' + name[0])
# print('Third Letter Is: \t ' + name[2])
# print('Last Letter Is :\t ' + name[8])
# print (name[6:9])
# print (name[0:4])
# print (name[2:7])
# print (name[8:4:-1])
# print (name[0:9:2])

#third question :
# name = "$&$&Mohammed$&$&"
# test_str = ''.join(letter for letter in name if letter.isalnum())
# print(test_str)

#fourth question :
# msg = "I %7 Python And Although I %7 GSG with Zakaria"
# x= msg.replace("%7" , "love")
# print (x)

#bonus question : 11
#title() returns a copy of the string in which the first characters of all the words are capitalized whereas the string method
# capitalize() returns a copy of the string in which just the first word of the entire string is capitalized
# str1 = 'noor osama abo samra'
# str2 = str1.title()
# print (str2)
# str3 = str1.capitalize()
# print(str3)

 #12
# num1 = "4"
# num2 = "56"
# num3 = "963"
# num4 = "385"
# num5 = "8719"
# num6 = "87190"

# multiline_str = """I'm learning Python.
# I refer to TechBeamers.com tutorials.
# It is the most popular site for Python programmers."""
# print("Multiline string: \n" + multiline_str)
# is_male= False
# is_tall= True

# if is_male and is_tall:
#     print("You are a male your also you are tall ")

# elif not(is_male) and is_tall:
#     print("you are not male but you are tall")
# elif is_male and not(is_tall):
#     print("you are male but you are not tall")
# else:
#     print("you are not a male your also your not tall !!!!!!") 


# def number(num1,  num2, num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3
# print(number(4,50,6))





# n=int(input("enter the age"))

# if (n>=18):
#     print("he have voting eligibilty")
# else:
#     print("he doesnt have eligibilty to vote")

# n=int(input("Enter a number "))

# if (n>0):
#     print("number is positive")
# elif(n<0):
#     print("number is negative")
# elif(n==0):
#     print("number is 0")

# m= int(input("enter the mark: "))

# if (90<=m<=100):
#     print("The student got A grade")
# elif (80<=m<90):
#     print("The student got B grade")
# elif (70<=m<80):
#     print("The student got C grade")
# elif (60<=m<=70):
#     print("The student got D grade")
# else:
#     print("failed")


# n=int(input("Enter a number "))

# if (n%2==0):
#     print("The number is even")
# else:
#     print("The number is odd")



# print("leap year")

# year= int(input("Enter the year: "))

# if (year%4==0):
#     print("It is leap year")
# else:
#     print("It is not leap year")

# print("vowels or consonant")
# x=input("Enter a alphabet: ")

# if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
#     print("It's a vowel")
# elif(x=="A" or x=="E" or x=="I" or x=="O" or x=="U"):
#     print("it's a vowel")
# else:
#     print("This is consonant")





# num=int(input("Enter the number: "))

# if (num%7==0):
#     print("the number is divisible")
# else:
#     print("the number not divisible")



# n= int(input("Enter the number: "))

# if(n%5==0):
#     print("Hello")
# else:
#     print("Bye")



# amt= 0
# unit=int(input("Enter the unit: "))

# if (unit<100):
#     amt= 0
# if (unit>100) and (unit<=200):
#     amt=(unit-100)*5
# if (unit>200):
#     amt=500+(unit-200)*10

# print("The amount to pay", amt)


# num=int(input("enter any number: "))
# print("The last digit is ",num%5)


# num=int(input("Enter any number: "))
# id=num%10

# if  (id%3==0):
#     print("The number is divisible by 3")
# else:
#     print("The number is not divisible by 3")


# tax=0
# pr=int(input("Enter the price: "))

# if (pr>100000):
#     tax=15/100*pr
# elif (pr>50000) or (pr<=1000000):
#     tax=10/100*pr
# else:
#     tax=5/100*pr

# print("The payable tax:",tax)



# days=int(input("Enter the number between 1 t0 7: "))

# if (days==1):
#     print("Monday")
# elif (days==2):
#     print("Tuesday")
# elif (days==3):
#     print("Wednesday")
# elif (days==4):
#     print("Thursday")
# elif (days==5):
#     print("friday")
# elif (days==6):
#     print("Saturday")
# elif (days==7):
#     print("Sunday")
# else:
#     print("Please enter the number between 1 to 7")




# month= int(input("Enter the number between 1 to 12: "))

# if (month==1):
#     print("January")
# elif (month==2):
#     print("February")
# elif (month==3):
#     print("March")
# elif (month==4):
#     print("April")
# elif (month==5):
#     print("May")
# elif (month==6):
#     print("June")
# elif (month==7):
#     print("July")
# elif (month==8):
#     print("August")
# elif (month==9):
#     print("September")
# elif (month==10):
#     print("October")
# elif (month==11):
#     print("November")
# elif (month==12):
#     print("December")
# else:
#     print("Enter the number between 1 to 12")



# print("(A)Delhi")
# print("(B)Agra")
# print("(C)Jaipur")

# city= input("Enter the city: ")

# if city=="delhi":
#     print("Monument name is: Red fort")
# elif city=="agra":
#     print("Monument name is: Taj mahal")
# elif city=="jaipur":
#     print("Monument name is: Hawa mahal")
# else:
#     print("Enter the city name from list")

# liters=105
# amt=0
# if liters <= 100:
#     amt=liters * 15
# elif liters <= 200:
#     amt=(100 * 15) + ((liters - 100) * 14)
# else:
#     amt=(100 * 15) + (100 * 14) + ((liters - 200) * 12)

# print(amt)



# a= "python"
# b=""
# for i in a:
#     result = i + b 
#     b = result
# print(result)

# n = 5
# result = 1

# number=range(1, n+1)
# 0
# for num in number:
#     result*=num
# print(result)

# cars= ["toyota", "maruthi","hundai"]
# color =["red","white","black"]

# for i in cars:
#     for j in color:
#         print(i, j)



# n= 5

# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# n= "python"
# b=len(n)
# for i in range(b):
#     for j in range(i+1):
#         print(n[j], end="")
#     print()

# n= 5
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(j, end= "")
#     print()


# n=4

# for i in range(n):
#     for j in range(n):
#         print("*", end= "")
#     print()

# n= 4
# b=1

# for i in range(1, n+1):
#     for j in range(i):
#         print(b, end= " ")
#         b+=1
#     print()

# a=[1,2,3,34,67,21]
# b=[2,6,4,5,78]
# c=[]

# for i in a:
#     if i not in b:
#         c.append(i)       
# print(c)

# a="calculator"
# b=""

# for i in a:
#     if i not in b:
#         b+=i
# print(b)
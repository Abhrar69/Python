# num= [1,2,3,4,5,6,7,8,9]
# squares= []

# for i in num:
#     sq=i**2

#     squares.append(sq)

# print("the new list is:",squares)

# print(list(range(10,21,2)))

# for i in "Abhrar":
    # print(i,"?")

# for i in range(5):
#     print(i)

# for i in range(20,0,-2):
#     print(i)

# num= int(input("Enter any number: "))

# for i in range(1,11):
#     print(num*i)

# num= int(input("Enter any number: "))
# p=1

# while(num):
#     r=num%10
#     p=p*r
#     num=num//10
# print("product digit is:",p)


# num = int(input("Enter number: "))
# f= 1

# for i in range(1,num+1):
#     f=f*i
# print("The factorial is: ",f)

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "h"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
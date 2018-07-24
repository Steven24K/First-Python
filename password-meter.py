print("The password should at least:\n-7 characters long\n-Contain 2 numbers\n-Contain 1 special character\n-Contain Upper- and Lowercase\n\nExample: Abcd12!\n")
# 33 t/m 47 Special characters
# 48 t/m 57 Numbers
# 58 t/m 64 Special characters
# 65 t/m 90 Uppercase
# 91 t/m 96 Speciald characters
# 97 t/m 122 Lowercase

#Variabelen
password = input("Check of your password is strong:  ")
lenght = len(password)
special = 0
number = 0
upper = 0
lower = 0


for i in range(lenght):
    check = ord(password[i]) 
    if 33 <= check <= 47 or 58 <= check <= 64 or 91 <= check <= 96:
        special += 1
    if 48 <= check <= 57:
        number += 1
    if 65 <= check <= 90:
        upper += 1
    if 97 <= check <= 122:
         lower += 1
          

score = lower * upper * number * special

if score < 6:
    print("The password does not fit the minimum requirements, VERRY WEAK!!!")
if score == 6:
    print("The password does exactly fit the requirements, it is good but can be better. MEDIUM!!!")
if score > 6:
    print("The password is VERRY STRONG!!!")

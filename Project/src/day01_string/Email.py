strIn = str(input("Enter your email address: "))
getAt = strIn.find("@")
getAtCount = strIn.count("@")
getDot = strIn.find(".")
#判断是否是正确的邮箱地址
if getAt == -1 or getDot == -1 or getAtCount != 1:
    print("Invalid email address")
else:
    print("Valid email address")
print("----------------------------------")
if "@" in strIn and "." in strIn:
    print("The email address contains '@' and '.'")
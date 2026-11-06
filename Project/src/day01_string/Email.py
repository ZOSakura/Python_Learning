str_in = str(input("Enter your email address: "))
getAt = str_in.find("@")
getAtCount = str_in.count("@")
getDot = str_in.find(".")
#判断是否是正确的邮箱地址
if getAt == -1 or getDot == -1 or getAtCount != 1:
    print("Invalid email address")
else:
    print("Valid email address")
print("----------------------------------")
if "@" in str_in and "." in str_in:
    print("The email address contains '@' and '.'")
String = "- Hello, World! -"
index = String.find("World")
i = String.find("Python") #找不到返回-1
print(index)
print(i)
count = String.count("o")
print(count)
su = String.upper()
print(su)
sl = String.lower()
print(sl)
sp = String.split(",") #按给定的分隔符进行分割，返回一个list
print(sp)
print(type(sp)) #split返回的是一个list
st = String.strip("-").strip()
print(st)
sr = String.replace("World", "Python")
print(sr)
boolean = String.startswith("-")
print(boolean)
print(String) #原本的字符串不会被修改
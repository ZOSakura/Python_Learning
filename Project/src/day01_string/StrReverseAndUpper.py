def strReverseAndUpper(s):
    return s[::-1].upper()
strlist = []
while True:
    str_in = str(input("Enter a string to reverse and convert to uppercase (or type 'exit' to quit): "))
    if str_in.lower() == 'exit':
        break
    res = strReverseAndUpper(str_in)
    strlist.append(res)
print("Reversed and Uppercase Strings:")
for s in strlist:
    print(s)
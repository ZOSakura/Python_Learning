def fact1(x):
    ret = x
    if x < 1 : return 1
    while x > 1 :
        x -= 1
        ret *= x
    return ret
print(fact1(1))
print(fact1(5))
print(fact1(9))
#递归
def fact2(x):
    if x > 1 :
        x *= fact2(x-1)
    else: return 1
    return x
print(fact2(1))
print(fact2(5))
print(fact2(9))
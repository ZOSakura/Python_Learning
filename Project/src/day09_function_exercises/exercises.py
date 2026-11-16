def total_amount(*args, discount_ticket = 0, point_dicount= 0, shipping_fee = 0):
    #total = 0
    #for item in args:
    #    total += item[1] * item[2]
    total_list = [item[1] * item[2] for item in args]
    total = sum(total_list)
    if total >= 5000 and discount_ticket <= total :
        total -= discount_ticket
    if total >= 5000 and int(point_dicount/100) <= total :
        total -= int(point_dicount/100)
    if total < 0 :
        total = 0
    total += shipping_fee
    return total
print(total_amount(("鼠标", 299, 1), ("键盘", 399, 2), ("手机", 4999, 1), discount_ticket=1500, point_dicount=50000, shipping_fee=15))

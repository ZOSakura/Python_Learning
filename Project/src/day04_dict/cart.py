cart = {}
while True:
    print("\n")
    r = input("请选择要执行的操作:\n1.添加商品\n2.修改商品\n3.删除商品\n4.查询商品\n5.退出\n")
    match r:
        case "1":
            name = input("请输入商品名称:")
            if name in cart:
                print("商品已存在！\n请前往更新商品信息。")
                continue
            price = input("请输入商品价格:")
            quantity = input("请输入商品数量:")
            cart[name] = {"价格": price, "数量": quantity}
        case "2":
            name = input("请输入要修改的商品名称:")
            if name in cart:
                price = input("请输入新的商品价格:")
                quantity = input("请输入新的商品数量:")
                cart[name] = {"价格": price, "数量": quantity}
            else:
                print("商品不存在！")
        case "3":
            name = input("请输入要删除的商品名称:")
            if name in cart:
                del cart[name]
                print("商品已删除！")
            else:
                print("商品不存在！")
        case "4":
            for item in cart.items():
                print(f"商品名称: {item[0]}, 价格: {item[1]['价格']}, 数量: {item[1]['数量']}")
        case "5":
            break
        case _:
            print("输入有误，请重新输入！")
            continue
print("感谢使用!")
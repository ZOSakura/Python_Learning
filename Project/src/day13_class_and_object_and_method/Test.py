#定义类
class Test:
    #构造方法使用__init__
    def __init__(self, brand, name, price):
        #self相当于Java中的this
        self.brand: str = brand
        self.name: str = name
        self.price: int = price
    #实例方法
    def running(self):
        print(f"{self.name}正在运行......")
    def total_cost(self, stone_count, discount=0):
        print(f"购买{stone_count}颗源石一共需要{int(stone_count*self.price*(1-discount/100))}元")
t = Test("YJ", "明日方舟", 32.5)
print(t.brand)
print(t.name)
print(t.price)
print(t.__dict__)
t.running()
t.total_cost(64, 50)
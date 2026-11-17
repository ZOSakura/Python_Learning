#类型注解
i: int = 114
f: float = 114.514
string: str = "苦也，这也言周"
boolean: bool = True
t: tuple[str, int, int] = ("明日方舟", 325, 799)
l: list[int] = [1, 2, 3, 4, 5]
s: set[int] = {325, 799, 2021}
d: dict[str, int] = {"舟":325, "呼呼呼":799}
#类型注解是提示，不是强制要求
#函数添加类型注解
def test(*args:tuple[str, int, int]) -> int:
    ret: int = 0
    for item in args:
        ret += item[1] * item[2]
    return ret
test(("舟", 325, 2),("呼呼呼", 799, 1))
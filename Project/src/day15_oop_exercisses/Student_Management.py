class Student:
    def __init__(self, name: str, chinese_score: int, math_score: int, english_score: int) -> None:
        self.name = name
        self.chinese_score = chinese_score
        self.math_score = math_score
        self.english_score = english_score

    def getSummary(self) -> str:
        return (f"姓名: {self.name} | 语文: {self.chinese_score} | 数学: {self.math_score} "
                f"| 英语: {self.english_score} | 总分: {self.chinese_score + self.math_score + self.english_score}")

    def setScore(self, chinese_score: int, math_score: int, english_score: int):
        if chinese_score != -1:
            self.chinese_score = chinese_score
        if math_score != -1:
            self.math_score = math_score
        if english_score != -1:
            self.english_score = english_score


class Management:
    def __init__(self) -> None:
        self.system_ver: str = "1.0.0"
        self.system_name: str = "教务管理系统"
        self.student_dict: dict[str, Student] = {}
        self.currentSelectedStudent = ""
        self.check_result = False

    def addStudent(self, s: tuple[str, int, int, int]) -> str:
        name, chinese_score, math_score, english_score = s
        if name in self.student_dict:
            return "这名学生的数据已存在!"
        if 0 <= chinese_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
            self.student_dict[name] = Student(name, chinese_score, math_score, english_score)
            return "学生数据已添加！"
        return "请检查成绩输入是否有误!"

    def getStudentScore(self, name: str) -> str:
        student = self.student_dict.get(name)
        if student is None:
            return "未找到该学生的相关数据！请检查学生姓名是否输入正确"
        self.currentSelectedStudent = name
        return student.getSummary()

    def setStudentScore(self, s: tuple[int, int, int]) -> str:
        chinese_score, math_score, english_score = s
        student = self.student_dict.get(self.currentSelectedStudent)
        if student is None:
            return "未找到该学生的相关数据！请检查学生姓名是否输入正确"
        ok = all(0 <= v <= 100 or v == -1 for v in (chinese_score, math_score, english_score))
        if not ok:
            return "请检查成绩输入是否有误!"
        student.setScore(chinese_score, math_score, english_score)
        return "学生数据已修改！"

    def delStudentScore(self, confirm: bool) -> str:
        self.check_result = False
        if not confirm:
            return "已取消删除"
        if self.student_dict.pop(self.currentSelectedStudent, None) is not None:
            self.currentSelectedStudent = ""
            return "删除成功"
        return "删除失败"

    def check(self, name: str) -> str:
        if name not in self.student_dict:
            self.check_result = False
            return "未找到该学生的相关数据！请检查学生姓名是否输入正确"
        self.currentSelectedStudent = name
        self.check_result = True
        return "是否确认删除该学生的成绩？\n请输入: Y / N (Y:是，N否)"

    def getAllStudentScore(self) -> list[str]:
        return [student.getSummary() for student in self.student_dict.values()]


class User:
    def __init__(self):
        management = Management()
        print("欢迎使用教务管理系统!")
        while True:
            print("请选择你要做的操作:\n"
                  "1. 添加学生数据\n2. 修改学生数据\n3. 删除学生数据\n"
                  "4. 查询所有学生数据\n5. 退出教务管理系统")
            try:
                i = int(input())
            except ValueError:
                print("请输入 1-5 的数字")
                continue

            match i:
                case 1:
                    name = input("请输入你要添加的学生的姓名:\n")
                    try:
                        chinese_score = int(input("请输入语文成绩:\n"))
                        math_score = int(input("请输入数学成绩:\n"))
                        english_score = int(input("请输入英语成绩:\n"))
                    except ValueError:
                        print("成绩输入有误！请检查输入类型是否正确")
                        continue
                    print(management.addStudent((name, chinese_score, math_score, english_score)))

                case 2:
                    name = input("请输入你要修改的学生的姓名:\n")
                    msg = management.getStudentScore(name)
                    print(msg)
                    if not management.check_result and name not in management.student_dict:
                        continue
                    modified_score: list = []
                    try:
                        print("请输入修改后的语文成绩: (不需要修改请留空并直接回车)")
                        modified_score.append(input())
                        print("请输入修改后的数学成绩: (不需要修改请留空并直接回车)")
                        modified_score.append(input())
                        print("请输入修改后的英语成绩: (不需要修改请留空并直接回车)")
                        modified_score.append(input())
                        parsed = [(-1 if x == "" else int(x)) for x in modified_score]
                        chinese_score, math_score, english_score = parsed
                    except ValueError:
                        print("成绩输入有误！请检查输入类型是否正确")
                        continue
                    print(management.setStudentScore((chinese_score, math_score, english_score)))

                case 3:
                    name = input("请输入你要删除的学生的姓名:\n")
                    print(management.check(name))
                    if not management.check_result:
                        continue
                    sc = input().strip().upper()
                    if sc == "Y":
                        print(management.delStudentScore(True))
                    elif sc == "N":
                        print(management.delStudentScore(False))
                    else:
                        print("输入有误！请检查输入是否正确")

                case 4:
                    students = management.getAllStudentScore()
                    if not students:
                        print("暂无学生数据")
                    for s in students:
                        print(s)

                case 5:
                    break

                case _:
                    print("输入有误！请检查输入是否正确")
        print("感谢使用教务管理系统!")


# 启动程序
user = User()
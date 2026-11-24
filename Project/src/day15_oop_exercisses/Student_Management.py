class Student:
    def __init__(self, name: str, chinese_score: int, math_score:int, english_score:int) -> None:
        self.name = name
        self.chinese_score = chinese_score
        self.math_score = math_score
        self.english_score = english_score
    def __str__(self) -> str:
        return f"姓名: {self.name} | 语文: {self.chinese_score} | 数学: {self.math_score} | 英语: {self.english_score} | 总分: {self.chinese_score + self.math_score + self.english_score} "
    def setScore(self, chinese_score: int, math_score:int, english_score:int):
        if chinese_score != -1:
            self.chinese_score = chinese_score
        if math_score != -1:
            self.math_score = math_score
        if english_score != -1:
            self.english_score = english_score
class Management:
    system_ver:str = "1.0.0"
    system_name:str = "教务管理系统"
    student_dict:dict[str, Student] = {}
    def __init__(self) -> None:
        self.nameTemp = ""
        self.check_result = False
    def addStudent(self, s:tuple[str, int, int, int]):
        name: str = s[0]
        chinese_score: int = s[1]
        math_score:int = s[2]
        english_score:int = s[3]
        if name not in self.student_dict:
            if 0<=chinese_score<=100 and 0<=math_score<=100 and 0<=english_score<=100:
                self.student_dict[name] = Student(name, chinese_score, math_score, english_score)
                return "学生数据已添加！"
            else : return "请检查成绩输入是否有误!"
        else : return "这名学生的数据已存在!"
    def getStudentScore(self, name):
        if name in self.student_dict:
            self.nameTemp = name
            return self.student_dict.get(name).__str__()
        else : return "未找到该学生的相关数据！请检查学生姓名是否输入正确"
    def setStudentScore(self, s:tuple[int, int, int]):
        chinese_score: int = s[0]
        math_score:int = s[1]
        english_score:int = s[2]
        student = self.student_dict.get(self.nameTemp)
        if student != None:
            if (0<=chinese_score<=100 or chinese_score == -1) and (0<=math_score<=100 or math_score == -1) and (0<=english_score<=100 or english_score == -1):
                student.setScore(chinese_score, math_score, english_score)
                return "学生数据已修改！"
            else : return "请检查成绩输入是否有误!"
        else : return "未找到该学生的相关数据！请检查学生姓名是否输入正确"
    def delStudentScore(self):
        self.check_result = False
        sc = str(input())
        match sc:
            case "Y":
                r = True
            case "N":
                r = False
            case _:
                return "输入有误！请检查输入是否正确"
        if r == True:
            if self.student_dict.pop(self.nameTemp, None) != None:
                return "删除成功"
            else : return "删除失败"
    def check(self, name):
        self.nameTemp = name
        if name in self.student_dict:
            self.check_result = True
            return "是否确认删除该学生的成绩？\n请输入: Y / N (Y:是，N否)"
        else : return "未找到该学生的相关数据！请检查学生姓名是否输入正确"
    def allScanner(self) -> tuple[str, int, int, int]:
        name, *scores = input().replace("，", ",").split(",")
        chinese_score, math_score, english_score = map(int, scores)
        return (name, chinese_score, math_score, english_score)
    def scoreScanner(self):
        chinese_score, math_score, english_score = map(int, input().replace("，", ",").replace(" ", "-1").split(","))
        return (chinese_score, math_score, english_score)
class User:
    def __init__(self):
        management = Management()
        print("欢迎使用教务管理系统!")
        while True:
            print("请选择你要做的操作:\n1. 添加学生数据\n2. 修改学生数据\n3. 删除学生数据\n4. 退出教务管理系统")
            i = int(input())
            match i:
                case 1:
                    print("请输入你要添加的学生的信息:\n格式:\n姓名，语文成绩，数学成绩，英语成绩\n数据之间用逗号分隔")
                    print(management.addStudent(management.allScanner()))
                case 2:
                    print("请输入你要修改的学生的姓名:")
                    print(management.getStudentScore(input()))
                    print("请输入你要修改的学生的成绩:\n格式:\n语文成绩，数学成绩，英语成绩\n数据之间用逗号分隔\n不需要修改的数据处请输入一个空格(如: ,100, )")
                    print(management.setStudentScore(management.scoreScanner()))
                case 3:
                    print("请输入你要删除的学生的姓名:")
                    print(management.check(input()))
                    print(management.delStudentScore())
                case 4:
                    break
        print("感谢使用教务管理系统!")
#启动程序
user = User()
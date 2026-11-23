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
        pass
    def addStudent(self, name: str, chinese_score: int, math_score:int, english_score:int):
        if name not in self.student_dict:
            if 0<=chinese_score<=100 and 0<=math_score<=100 and 0<=english_score<=100:
                self.student_dict[name] = Student(name, chinese_score, math_score, english_score)
            else : print("请检查成绩输入是否有误!")
        else : print("这名学生的数据已存在!")
    def getStudentScore(self, name):
        return self.student_dict.get(name).__str__
    def setStudentScore(self, name, chinese_score: int = -1, math_score:int = -1, english_score:int = -1):
        student = self.student_dict.get(name)
        if student != None:
            if 0<=chinese_score<=100 and 0<=math_score<=100 and 0<=english_score<=100:
                student.setScore(chinese_score, math_score, english_score)
            else : print("请检查成绩输入是否有误!")
        else : print("未找到该学生的相关数据！请检查学生姓名是否输入正确")
    def delStudentScore(self, name):
        if name in self.student_dict:
            print("确定要删除吗")
            r = str(input())
            if r=="Y":
                self.student_dict.pop(name)
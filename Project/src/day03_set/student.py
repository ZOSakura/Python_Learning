footballSet = {"Alice", "Bob", "Charlie"}
basketballSet = {"Alice", "Bob", "David", "Eve"}
EnglishSet = {"Alice", "David", "Frank"}
artSet = {"Charlie", "Eve", "Frank", "Alice"}
print("同时选修英语和美术的学生有: " + str(EnglishSet.intersection(artSet)))
print("选修了足球但没有选修篮球的学生有: " + str(footballSet.difference(basketballSet)))
print("同时选修了四门课程的学生有: " + str(footballSet.intersection(basketballSet).intersection(EnglishSet).intersection(artSet)))
#每个学生选修的课程数
allSet = footballSet.union(basketballSet).union(EnglishSet).union(artSet)
allList = list(allSet)
for student in allList:
    count = 0
    if student in footballSet:
        count += 1
    if student in basketballSet:
        count += 1
    if student in EnglishSet:
        count += 1
    if student in artSet:
        count += 1
    print(student + "选修了" + str(count) + "门课程")
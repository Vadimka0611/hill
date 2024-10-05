# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
num1 = [0, 1, 0, 12, 3]
num2 = [0]
num3 = [1, 0, 13, 0, 0, 0, 5]
num4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#Переменные для чисел
for i in num1:
    if i == 0:
        num1.remove(i)
        num1.append(i)
print(num1)
#Удаление нулей и вставка в конец
for i in num2:
    if i == 0:
        num2.remove(i)
        num2.append(i)
print(num2)

for i in num3:
    if i == 0:
        num3.remove(i)
        num3.append(i)
print(num3)


for i in num4:
    if i == 0:
        num4.remove(i)
        num4.append(i)
print(num4)



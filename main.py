stroke = input("Введите строковое значение: ")
print("Ваша строка: ", stroke)

stroke = stroke.replace(" ", "")
secure = list()

for i in range(len(stroke)):
    if stroke[i] not in secure:
        numb = stroke.count(stroke[i])
        print("Кол-во букв ", stroke[i], " - ", numb)
        secure.append(stroke[i])

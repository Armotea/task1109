stroke = input("Введите строковое значение: ")                  #Получение строки от пользователя
print("Ваша строка: ", stroke)

stroke = stroke.replace(" ", "")                                #Удаление пробелов в строке
secure = list()                                                 #Список для последующей проверки

for i in range(len(stroke)):
    if stroke[i] not in secure:                                 #Проверка на начиличе символа в списке secure,
        numb = stroke.count(stroke[i])                          #если символа нет в списке secure, то выводится кол-во вхождений символа в список stroke
        print("Кол-во букв ", stroke[i], " - ", numb)
        secure.append(stroke[i])                                #К списку secure добавляется символ, прошедший через цикл


color=("красный","синий", "жёлтый")
c1=input()
c2=input()
if c1 in color and c2 in color:
    if c1 == c2:
        print(c1)
    elif (c1 == "красный" or c1 == "синий" and c2 == " синий" or c2 == "красный"):
            print("фиолетовый")
    elif (c1 == "красный"or c1 == "жёлтый" and c2 == "жёлтый" or c2 ==  "красный"):
            print("оранжевый")
    elif (c1 == "синий"or c1 == "жёлтый" and c2 == "жёлтый" or c2 == "синий"):
            print("зелёный")
else:
        print("ошибка цвета")

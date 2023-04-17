class List:
    List1 = ["1", "Королев", "2", "Гулов"]
    List2 = []
    for i in List1[1::2]:
        inp = int(input(f"{i} оценка \n"))
        if inp > 2:
            List2.extend(List1[:2])
            List2.append(inp)
            for i in List1[0:2]:
                List1.remove(i)
        else:
            for i in List1[0:2]:
                List1.remove(i)
            print(f"Студент {i} завалил экзамен!")
        print("Студентов осталось: ", List1)
        print("Студенты сдали: ", List2)

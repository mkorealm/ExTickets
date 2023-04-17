import matplotlib.pyplot as plt

# plt.style.use('seaborn-whitegrid')
titlebar = plt.figure("Королев Максим 41ИС-19")


class Vector:
    vector1 = [1, 2, 3, 4]
    vector2 = [2, 3, 4, 1, 1.5, 2]
    result = vector1 + vector2

    plt.plot(result, linewidth=2.0)
    plt.show()

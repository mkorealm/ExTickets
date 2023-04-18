import os
import numpy as np
import math
import matplotlib.pyplot as plt

script_dir = os.path.dirname(__file__)

plt.style.use('seaborn-whitegrid')
titlebar = plt.figure("Королев Максим 41ИС-19")


class Main:
    FUNCTION_TEMPLATE = '{0} * cos(x) + {1}'

    @staticmethod
    def average(arr):
        return max(arr) - min(arr)

    def __init__(self, filename):
        self.points_x = []
        self.points_y = []
        with open(filename) as file:
            line = file.readline().split()
            self.coefs = line[0:2]
            self.steps = line[2::1]
            self.function = self.FUNCTION_TEMPLATE.format(*self.coefs)
            if len(line) > 2:
                self.ct_x_step = float(1 / eval(line[2].replace(',', '.')))  # 1 > x > 0
                self.ct_y_step = float(1 / eval(line[3].replace(',', '.')))  # 1 > y > 0
        self.create_points()

    def calc_point(self, x):
        result = eval(self.function.replace('cos(x)', f'({str(math.cos(x))})'))
        print(result)
        return result

    def create_points(self, start=-20, end=20, step=2.0):
        if re.search(r'^[^}]+$', self.function):
            for X in np.arange(start, end, step):
                self.points_x.append(X)
                self.points_y = self.calc_point(X)
                self.create_plot(self.points_x, self.points_y)

    def create_plot(self, points_x, points_y):
        ct_x_steps = self.ct_x_step
        ct_y_steps = self.ct_y_step
        ox_step = self.average(self.ox_points) / ct_x_steps
        oy_step = self.average(self.oy_points) / ct_y_steps
        print(f'Шаг по X: {ox_step}', f'Кол-во отрезков: {ct_x_steps}', min(self.ox_points), max(self.points_x))
        print(f'Шаг по Y: {oy_step}', f'Кол-во отрезков: {ct_y_steps}', min(self.oy_points), max(self.points_y))
        plt.plot(points_x, points_y)
        plt.show()

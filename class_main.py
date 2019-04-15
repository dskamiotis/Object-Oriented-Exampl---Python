from classes import Operations
from classes import Plotter
# from classes import *
import numpy as np

object_operations = Operations(3, 4)
# print(object_operations.add())
# print(object_operations.subtraction())
object_operations.print()


x = np.linspace(start=0, stop=6, num=100)
# y = np.random.randn(100)
#
y = 50 * np.random.randn(10000) + 10
y = np.random.random_integers(0, 100, 100)
marks = list([50, 31, 32, 39, 48, 38, 45, 31, 37, 29, 33, 22])
marksx=np.linspace(0,len(marks),len(marks))


plotter_obj = Plotter(x, y)
plotter_obj.plot()

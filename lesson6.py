print("Введите длины сторон предполагаемого треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует и будет построен")
else:
    print("Треугольник не существует")

from tkinter import *

root = Tk()

c = Canvas(root, width=300, height=300, bg='white')
c.pack()

c.create_arc(1*(a), 1*(b), 100, 200, fill='blue', outline='red',
                     width=5)

root.mainloop()
# Я не успел найти способ на рисовать треугольник и обЪеденить ввод данных с рисованием треугольника
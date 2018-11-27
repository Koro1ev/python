#Задание 1
a = [i**2 for i in range(1,15)]
print(a)

#Задание 2
a = ["Яблоко", "Груша", "Виноград"]
b = ["Яблоко", "Киви", "Груша"]
c = [x for x in a if x in b]
print(c)

#Задание 3
#import random
#d = [random.randint(-100,100) for _ in range(50)]
#e = [i for i in d if i > 0 and i % 3 == 0 and i %4 != 0]
#print(e)



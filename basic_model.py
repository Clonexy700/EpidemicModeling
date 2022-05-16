import time
import random
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

x_points = []
y_points = []
recovered = 0
vulnerable = 5000
population = recovered + vulnerable
INFECTIVITY_INDEX = 24
infected = 1
day = 0

while infected <= population:
    population = recovered + vulnerable
    print(f'День: {day}, количество инфицированных: {infected}, количество переболевших: {recovered}, количество '
          f'уязвимых к вирусу {vulnerable}, популяция человечества: {population}')
    x_points.append(infected)
    y_points.append(day)
    day += 1
    can_infect = vulnerable
    if recovered == population-1:
        print(f'День: {day}, количество инфицированных: 0, количество переболевших: {population}, количество '
              f'уязвимых к вирусу 0, популяция человечества: {population}')
        break
    infected += infected * INFECTIVITY_INDEX
    if infected > can_infect:
        infected = vulnerable
    if (day != 0) and (day % 3) == 0:
        people_will_be_recovered = infected//random.randint(2,3)
        recovered += people_will_be_recovered
        infected -= people_will_be_recovered
        vulnerable -= people_will_be_recovered


plt.title("Эпидемия")
plt.xlabel("Время (Дни)")
plt.ylabel("Инфицированные")
plt.grid()
plt.plot(y_points, x_points)
plt.show()


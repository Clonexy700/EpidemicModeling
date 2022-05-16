import time
import random
import matplotlib.pyplot as plt

x_points = []
y_points = []
x_points_recovered = []
y_points_recovered = []
recovered = 0
vulnerable = 1000000
population = recovered + vulnerable
INFECTIVITY_INDEX = 1
infected = 1
day = 0

while infected <= population:
    population = recovered + vulnerable
    print(f'День: {day}, количество инфицированных: {infected}, количество переболевших: {recovered}, количество '
          f'уязвимых к вирусу {vulnerable}, популяция человечества: {population}')
    x_points.append(infected)
    y_points.append(day)
    x_points_recovered.append(recovered)
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

f, ax = plt.subplots(1, 1, figsize=(15, 9))
plt.title("Эпидемия (Школьная модель)")
ax.plot(y_points, x_points, 'r', linewidth=1, label='Заражённые')
ax.plot(y_points, x_points_recovered, 'g', linewidth=1, label='Выздоровившие')
ax.set_xlabel('Время (Дни)')
ax.legend(borderpad=6)
plt.show()


from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def plotseird(t, S, E, I, R, D=None, L=None, R0=None, Alpha=None, CFR=None):
    f, ax = plt.subplots(1, 1, figsize=(15, 9))
    plt.title('Эпидемия')
    ax.plot(t, S, 'b', linewidth=2, label='Восприимчивые к вирусу')
    ax.plot(t, E, 'y', linewidth=1, label='Инкубационный период')
    ax.plot(t, I, 'r', linewidth=3, label='Заражённые')
    ax.plot(t, R, 'g', linewidth=2, label='Выздоровившие')
    ax.plot(t, S + E + I + R, 'c--', linewidth=3, label='Всего людей')
    ax.set_xlabel('Время (Дни)')
    ax.legend(borderpad=6)
    plt.show()


def calculateDValues(y, t, N, beta, gamma, delta):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - delta * E
    dIdt = delta * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt


def calculateDValuesWithDead(y, t, N, beta, gamma, delta, alpha, rho):
    S, E, I, R, D = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - delta * E
    dIdt = delta * E - (1 - alpha) * gamma * I - alpha * rho * I
    dRdt = (1 - alpha) * gamma * I
    dDdt = alpha * rho * I
    return dSdt, dEdt, dIdt, dRdt, dDdt


N = 1_000_000
D = 4.0
gamma = 1.0 / D
delta = 1.0 / 5.0
R_0 = 5.0
beta = R_0 * gamma
S0, E0, I0, R0 = N-1, 1, 0, 0
t = np.linspace(0, 99, 100)
y0 = S0, E0, I0, R0

ret = odeint(calculateDValues, y0, t, args=(N, beta, gamma, delta))
S, E, I, R = ret.T
plotseird(t, S, E, I, R)


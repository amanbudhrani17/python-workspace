import random
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
from numpy import savetxt, loadtxt
from datetime import date
from matplotlib import cm


def problem1_1():
    a = np.zeros(10)
    b = np.ones(10)
    c = b * 5
    print(a)
    print(b)
    print(c)


def problem1_2():
    a = np.arange(10, 51, 2)
    print(a)


def problem1_34():
    a = [[random.random() for _ in range(10)] for _ in range(10)]
    print(a)
    savetxt('lab1.txt', a)
    b = loadtxt('lab1.txt')
    print(b)


def problem2_1():
    a = Image.open('image.jpg')
    b = np.asarray(a)
    c = b.reshape(3, -1)
    pd.DataFrame(c).to_csv('LAb1.csv')


def problem2_2():
    x = pd.read_csv('abc.csv')
    x = x.to_numpy()
    x = np.delete(x=-1,axis=0)
    x = np.delete(x=-1,axis=1)
    print(x)


def problem2_3():
    d = pd.to_datetime(str(date.today()), format='%Y-%m-%d')
    print(d)


def problem3(birth_date):
    a = (date.today()-birth_date).days
    b = int(a / 365.25)
    print(b)


if __name__ == '__main__':
    problem1_1()

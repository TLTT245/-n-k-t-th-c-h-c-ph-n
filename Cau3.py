import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols,Eq,solve
from sympy import *
def viet_phuong_trinh_daoham(a,b,c):
    fig, ax = plt.subplots()
    x = np.linspace(start=a,stop=b, num=c)
    y =  x ** 4 - 2 * x ** 2 - 3
    y1 = 4*x**3 - 4 * x
    y2 = 12*x**2 -4
    y3 = 24*x
    ax.plot(x, y)
    ax.plot(x, y1)
    ax.plot(x, y2)
    ax.plot(x, y3)
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.plot(x, y,label=r'$y=x^{4}-2x^{2}-3$')
    ax.plot(x, y1, label=r'$y=4x^{3} - 4x$')
    ax.plot(x, y2,label=r'$y2=12x^{2}-4$')
    ax.plot(x, y3, label=r'$y=24x $')
    ax.set_title("Đồ thị phương trình")
    ax.legend()
    plt.show()
def main():
    viet_phuong_trinh_daoham(-20,20,100)
if __name__=='__main__':
    main()



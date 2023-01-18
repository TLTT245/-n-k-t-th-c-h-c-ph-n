import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def tao_vecto(a,b,c):
    x = np.linspace(a, b, c)
    return x
def do_thi_yen_ngua(ax,x,y):
    X, Y = np.meshgrid(x, y)
    Z = (X/3)**2 - (Y/2)**2
    ax.plot_surface(X, Y, Z, cmap='Blues')
    ax.set_title('Đồ thị mặt yên ngựa')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
def do_thi_hyperbolic(ax,x,y):
    x, y = np.meshgrid(x, y)
    z1 = 4 * ((x / 3) ** 2 + (y / 5) ** 2 - 1) ** (1 / 2)
    z2 = -4 * ((x / 3) ** 2 + (y / 5) ** 2 - 1) ** (1 / 2)
    ax.plot_surface(x, y, z1, cmap='Blues')
    ax.plot_surface(x, y, z2, cmap='Blues')
    ax.set_title('Đồ thị hyperbolic')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
def do_thi_mat_cau(ax,u,v):
    x = (2*(np.outer(np.cos(u), np.sin(v)))-2)
    y = (2*(np.outer(np.sin(u), np.sin(v)))+1)
    z = (2*(np.outer(np.ones(np.size(u)), np.cos(v)))+4)
    ax.plot_surface(x, y, z, cmap='Blues')
    ax.set_title('Đồ thị mặt cầu')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
def main():
    x = tao_vecto(-30,30,100)
    y = tao_vecto(-30,30,100)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    fig = plt.figure(figsize=(18, 6))
    ax1 = fig.add_subplot(131, projection='3d')
    ax2 = fig.add_subplot(132, projection='3d')
    ax3 = fig.add_subplot(133, projection='3d')
    do_thi_yen_ngua(ax1,x,y)
    ax1.set_title('Đồ thị mặt yên ngựa')
    do_thi_hyperbolic(ax2,x,y)
    ax2.set_title('Đồ thị hyperbolic')
    do_thi_mat_cau(ax3,u,v)
    ax3.set_title('Đồ thị mặt cầu')
    plt.show()
if __name__=='__main__':
    main()
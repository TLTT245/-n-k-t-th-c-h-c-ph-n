from sympy import symbols, Eq, solve
def giai_pt_bac3(a,b,c,d,e,f,g,h,j,q,l,m):
    x, y, z = symbols('x y z')
    eq1 = Eq(a*x + b*y + c*z, d)
    eq2 = Eq(e*x + f*y + g*z, h)
    eq3 = Eq(j*x + q*y + l*z, m)
    answer = solve((eq1, eq2, eq3), (x, y, z))
    print(answer)
from sympy import *
def tinh_gioi_han(x,f,n):
    answer = limit(f, x, n)
    print('Kết quả giới hạn: ', answer)
def tinh_dao_ham(x,f):
    answer = diff(f, x)
    print(answer)
def tinh_nguyen_ham(x,f):
    answer = integrate(f, x)
    print(answer)
def tinh_tich_phan(x,f,a,b):
    answer = integrate(f, (x, a, b))
    print(answer)
def main():
    x = symbols('x')
    giai_pt_bac3(2,-5,1,-5,4,2,-2,2,1,1,-1,0)
    tinh_gioi_han(x,(x**3-3*x**2)**1/3+(x**2-2*x)**1/2,+00)
    tinh_dao_ham(x,(2*x-1)/(x+2))
    tinh_nguyen_ham(x,x/(x**2+1))
    tinh_tich_phan(x,(1-(x**2*tan(x))/(x**2+cos(x)+x)),pi,(2*pi)/3)
if __name__=="__main__":
    main()



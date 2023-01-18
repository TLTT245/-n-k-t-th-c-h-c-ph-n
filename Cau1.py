import numpy as np
np.random.seed(123)
def tao_ma_tran(a,b,m,n):
    x = np.random.randint(low=a, high=b,size=m*n).reshape((m, n))
    print(x)
    return x
def nhan_ma_tran_stn(n,y):
    C = n * y
    print('Nhân ma trận với',n,'là',C)
def nhan_ma_tran(x,y):
    C = np.multiply(x, y)
    print(C)
def nhan_mt_mtcv(x):
    y = tao_ma_tran(5,10,3,5)
    y_chuyenvi = y.T
    C = np.dot(x, y_chuyenvi)
    print(C)
def main():
    x = tao_ma_tran(3,10,3,5)
    y = tao_ma_tran(3,10,3,5)
    nhan_ma_tran(x,y)
    nhan_mt_mtcv(x)
    nhan_ma_tran_stn(3,x)
if __name__=='__main__':
    main()





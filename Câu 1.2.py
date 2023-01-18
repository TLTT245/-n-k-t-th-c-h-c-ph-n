import numpy
import random
def sinh_list1_thuc(n,a,b):
  c = [random.uniform(a, b) for i in range(n)]
  print(c)
  return c
def sinh_list2(n,a,b):
  c = [random.randint(a, b) for i in range(n)]
  print(c)
  return c
def sap_xep_tang_dan(x):
  x = sorted(x,reverse = False)
  print(x)
  return x
def sap_xep_giam_dan(x):
  x = sorted(x,reverse = True)
  print(x)
  return x
def sap_xep(x, flag):
  if flag == True:
    return sap_xep_tang_dan(x)
  else:
    return sap_xep_giam_dan(x)
def liet_ke_phan_tu(v, n):
  shd = []
  for i in range(len(v)):
    if v[i] == n:
      shd.append(i)
  return shd
def save_text_file(list1,file):
  with open(file,'w') as f:
    for item in list1:
      f.write('%s/n'%item)
  print('Tập tin được tạo')
def save_text_filekmat(list1,file):
  with open(file,'a+') as f:
    for item in list1:
      f.write('%s/n'%item)
  print('Tập tin được tạo')
def save_binary_file(list1,file):
  with open(file,'wb') as f:
    for item in list1:
      doi  = int(item)
      f.write(doi.to_bytes(8,'big'))
  print('Tập tin được tạo')
def main():
  x = sinh_list1_thuc(5,2,5)
  save_text_file(x,r'D:/doan/taptin.txt')
  d = sap_xep(x, False)
  save_text_filekmat(d, r'D:/doan/taptin.txt')
  c = liet_ke_phan_tu(x, 2)
  if len(c) == 0:
    print('Khong co phan tu nay trong vector')
  else:
    print('Cac vi tri xuat hien la: ', c)
if __name__=='__main__':
  main()

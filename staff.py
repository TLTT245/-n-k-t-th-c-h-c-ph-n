class NhanVien:
  def __init__(self, name, age, wage):
    self.ten = name
    self.tuoi = age
    self.luong = wage
  def __str__(self):
    message = '[ Tên : ' + self.ten + '; Tuổi: ' + str(self.tuoi) + '; Lương : ' + str(self.luong) + ']'
    return message
  def __gt__(self, obj):
    return(self.tuoi > obj.tuoi)
  def __ge__(self, obj):
    return(self.tuoi >= obj.tuoi)
  def __lt__(self, obj):
    return(self.tuoi < obj.tuoi)
  def __le__(self, obj):
    return(self.tuoi <= obj.tuoi)
  def __eq__(self, obj):
   return(self.tuoi == obj.tuoi)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Tạo một lưới các giá trị cho trục x và y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = (X + 2)**2 + (Y - 1)**2 + (4 - 4)**2 - 4

# Tạo đồ thị mặt cầu ba chiều
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vẽ đồ thị mặt cầu
ax.plot_surface(X, Y, Z, cmap='coolwarm')

# Hiển thị đồ thị
plt.show()
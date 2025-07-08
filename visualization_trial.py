from matplotlib import pyplot as plt
import random

w = []
x = []
y = []
z = []


for i in range(30):
    x.append(i)
    y.append(random.randint(2000, 2500))
    z.append(random.randint(2000, 2900))
    w.append(2300)


plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,w)

plt.title("Sample Visualization")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()
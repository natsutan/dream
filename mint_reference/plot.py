import matplotlib.pyplot as plt
import numpy as np

x = []
with open('loss.txt') as fp:
    for l in fp.readlines():
        loss = float(l.split()[1][:-1])

        x.append(loss)

y = np.arange(len(x))

#plt.plot(y, x, linestyle="solid")
#plt.title("Loss")

#plt.savefig("loss1.png")


x = x[1000:]
y = np.arange(len(x))
y = y + 1000

plt.plot(y, x, linestyle="solid")
plt.title("Loss")

plt.savefig("loss2.png")
plt.show()

from matplotlib import pyplot as plt
from formulae import getVertices

allVertices = getVertices()
xLi = [_[0] for _ in allVertices]
yLi = [_[1] for _ in allVertices]

fig = plt.figure()
ax = fig.add_subplot()

plt.axhline(y=0, color='black', linestyle=':')
plt.axvline(x=0, color='black', linestyle=':')

plt.plot(xLi+[xLi[0]],yLi+[yLi[0]],c="b")
plt.scatter(xLi,yLi,c="k")

ax.set_aspect('equal', adjustable='box')
ax.spines[['right', 'top']].set_visible(False)

plt.show()
from matplotlib import pyplot as plt
from formulae import getVertices

allVertices = getVertices()
xLi = [_[0] for _ in allVertices]
yLi = [_[1] for _ in allVertices]

def drawBaseStructure():
    fig, ax = plt.subplots()

    plt.axhline(y=0, color='black', linestyle=':')
    plt.axvline(x=0, color='black', linestyle=':')

    plt.plot(xLi+[xLi[0]],yLi+[yLi[0]],c="b",label="Equilateral Triangular Structure")
    plt.scatter(xLi,yLi,c="k",label="Vertices of Triangle")

    plt.legend()

    ax.set_aspect('equal', adjustable='box')
    ax.spines[['right', 'top']].set_visible(False)
    return fig,ax
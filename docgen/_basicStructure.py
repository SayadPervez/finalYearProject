from matplotlib import pyplot as plt
from formulae import getVertices

allVertices = getVertices()
xLi = [_[0] for _ in allVertices]
yLi = [_[1] for _ in allVertices]

def drawBaseStructure():
    fig, ax = plt.subplots()

    plt.axhline(y=0, color='black', linestyle=':')
    plt.axvline(x=0, color='black', linestyle=':')

    plt.plot(xLi+[xLi[0]],yLi+[yLi[0]],c="gray",linewidth=0.5)
    plt.scatter(xLi,yLi,c="k",label="Vertices of Equilateral Triangle")

    ax.text(xLi[0]+0.01,yLi[0]+0.01,"A")
    ax.text(xLi[1]+0.01,yLi[1]+0.01,"B")
    ax.text(xLi[2]+0.01,yLi[2]+0.01,"C")
    plt.legend()

    ax.set_aspect('equal', adjustable='box')
    ax.spines[['right', 'top']].set_visible(False)
    return fig,ax
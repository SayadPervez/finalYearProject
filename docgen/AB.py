from matplotlib import pyplot as plt
from formulae import getVertices,drawLine

allVertices = getVertices()
xLi = [_[0] for _ in allVertices]
yLi = [_[1] for _ in allVertices]

def drawBaseStructure():
    fig, ax = plt.subplots()

    plt.axhline(y=0, color='black', linestyle=':')
    plt.axvline(x=0, color='black', linestyle=':')

    plt.plot(xLi+[xLi[0]],yLi+[yLi[0]],c="b")
    plt.scatter(xLi,yLi,c="k")

    ax.set_aspect('equal', adjustable='box')
    ax.spines[['right', 'top']].set_visible(False)

    # wave approaching at 30 degrees to the X axis
    # (1,0) & (0,2.732)
    return fig,ax

hitOrder="ABC"

waveAngle = 20 # degrees
lineAngle = waveAngle+90

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,(1,0))
ax.set_title(f'Wave at {waveAngle} Degrees')

plt.show()

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,allVertices[0])
drawLine(ax,waveAngle,allVertices[1],color="k",linewidth=0.5)
drawLine(ax,waveAngle,(0,0),color="green",linewidth=0.5, linestyle="dashed")
ax.set_title(f'Wave at {waveAngle} Degrees hitting {hitOrder[0]}')
plt.xlim(-0.5, 0.6)
plt.ylim(-0.5, 0.6)
plt.show()

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,allVertices[1])
drawLine(ax,waveAngle,allVertices[2],color="k",linewidth=0.5)
drawLine(ax,waveAngle,(0,0),color="green",linewidth=0.5, linestyle="dashed")
ax.set_title(f'Wave at {waveAngle} Degrees hitting {hitOrder[1]}')
plt.xlim(-0.5, 0.6)
plt.ylim(-0.5, 0.6)
plt.show()
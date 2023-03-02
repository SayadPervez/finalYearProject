from matplotlib import pyplot as plt
from formulae import getVertices,drawLine,drawAngle

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

hitOrder="CBA"

waveAngle = 220 # degrees
lineAngle = waveAngle+90

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,(-1,0),"sound wave")
ax.set_title(f'Wave at {waveAngle} Degrees')
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,allVertices[2],"sound wave")
drawLine(ax,waveAngle,allVertices[1],"line perpendicular to sound wave",color="k",linewidth=0.5)
drawLine(ax,waveAngle,(0,0),"angle of sound wave",color="green",linewidth=0.5, linestyle="dashed")
drawAngle(ax,(0,0),0,waveAngle,0.37)
ax.set_title(f'Wave at {waveAngle} Degrees hitting {hitOrder[0]}')
drawAngle(ax,allVertices[1],150,waveAngle)
drawAngle(ax,allVertices[1],90,150,0.09)
plt.xlim(-0.5, 0.6)
plt.ylim(-0.5, 0.6)
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,allVertices[1],"sound wave")
drawLine(ax,waveAngle,allVertices[0],"line perpendicular to sound wave",color="k",linewidth=0.5)
drawLine(ax,waveAngle,(0,0),"angle of sound wave",color="green",linewidth=0.5, linestyle="dashed")
drawAngle(ax,(0,0),0,waveAngle,0.37)
ax.set_title(f'Wave at {waveAngle} Degrees hitting {hitOrder[1]}')
drawAngle(ax,allVertices[0],waveAngle,270)
plt.xlim(-0.5, 0.6)
plt.ylim(-0.5, 0.6)
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()
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

    # wave approaching at 30 degrees to the X axis
    # (1,0) & (0,2.732)
    return fig,ax

hitOrder="BAC"

waveAngle = -20 # degrees
lineAngle = waveAngle+90

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,(1,0),"sound wave")
ax.set_title(f'Wave at {waveAngle} Degrees')
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,allVertices[1],"sound wave")
drawLine(ax,waveAngle,allVertices[0],"line perpendicular to sound wave",color="k",linewidth=0.5)
drawLine(ax,waveAngle,(0,0),"angle of sound wave",color="green",linewidth=0.5, linestyle="dashed")
drawAngle(ax,(0,0),waveAngle,0,0.7)
ax.set_title(f'Wave at {waveAngle} Degrees hitting {hitOrder[0]}')
drawAngle(ax,allVertices[0],-90,waveAngle)
plt.xlim(-0.5, 0.6)
plt.ylim(-0.5, 0.6)
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,allVertices[0],"sound wave")
drawLine(ax,waveAngle,allVertices[2],"line perpendicular to sound wave",color="k",linewidth=0.5)
drawLine(ax,waveAngle,(0,0),"angle of sound wave",color="green",linewidth=0.5, linestyle="dashed")
drawAngle(ax,(0,0),waveAngle,0,0.7)
ax.set_title(f'Wave at {waveAngle} Degrees hitting {hitOrder[1]}')
drawAngle(ax,allVertices[2],waveAngle,30,0.1)
drawLine(ax,90,allVertices[2],"Reference Line parallel to Y axis","orange",0.5,"dashed")
drawAngle(ax,allVertices[2],30,90,0.15)
plt.xlim(-0.5, 0.6)
plt.ylim(-0.5, 0.6)
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()
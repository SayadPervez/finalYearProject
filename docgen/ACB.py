from matplotlib import pyplot as plt
from formulae import getVertices,drawLine,drawAngle
from _basicStructure import drawBaseStructure

allVertices = getVertices()
xLi = [_[0] for _ in allVertices]
yLi = [_[1] for _ in allVertices]

hitOrder="ACB"

waveAngle = 100 # degrees
lineAngle = waveAngle+90

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,(0,1),"sound wave")
ax.set_title(f'Wave at {waveAngle} Degrees')
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,allVertices[0],"sound wave")
drawLine(ax,waveAngle,allVertices[2],"line perpendicular to sound wave",color="k",linewidth=0.5)
drawLine(ax,waveAngle,(0,0),"angle of sound wave",color="green",linewidth=0.5, linestyle="dashed")
drawAngle(ax,(0,0),0,waveAngle,0.37)
ax.set_title(f'Wave at {waveAngle} Degrees hitting {hitOrder[0]}')
drawAngle(ax,allVertices[2],30,waveAngle)
drawAngle(ax,allVertices[2],0,30,0.09)
plt.xlim(-0.5, 0.6)
plt.ylim(-0.5, 0.6)
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()

fig,ax = drawBaseStructure()
drawLine(ax,lineAngle,allVertices[2],"sound wave")
drawLine(ax,waveAngle,allVertices[1],"line perpendicular to sound wave",color="k",linewidth=0.5)
drawLine(ax,waveAngle,(0,0),"angle of sound wave",color="green",linewidth=0.5, linestyle="dashed")
drawAngle(ax,(0,0),0,waveAngle,0.37)
ax.set_title(f'Wave at {waveAngle} Degrees hitting {hitOrder[1]}')
drawAngle(ax,allVertices[1],waveAngle,150)
drawLine(ax,0,allVertices[1],"reference line parallel to X axis",color="orange",linewidth=0.5, linestyle="dashed")
drawAngle(ax,allVertices[1],150,180,0.09)
plt.xlim(-0.5, 0.6)
plt.ylim(-0.5, 0.6)
plt.xlabel("X Axis Distance in meters (m)")
plt.ylabel("Y Axis Distance in meters (m)")
plt.legend()
plt.show()
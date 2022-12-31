from calculateAngle import calculateAngle,calculateTime

loPoints = []

theoreticalAngles = []
observedAngles = []

diffLi = []
xLi = []
yLi = []

divisor = 2000

# vertices : (0.028867513459481298, 0.05) (0.028867513459481298, -0.05) (-0.05773502691896258, 7.07050159149938e-18)
xLi.append(0.028867513459481298)
xLi.append(0.028867513459481298)
xLi.append(-0.05773502691896258)
yLi.append(0.05)
yLi.append(-0.05)
yLi.append(0)
diffLi.append(-10)
diffLi.append(-10)
diffLi.append(-10)

for x in range(-100,101):
    for y in range(-100,101):
        timeObject,theoreticalAngle = calculateTime((x/divisor,y/divisor),0,returnSourceAngle=True)
        observedAngle = calculateAngle(timeObject)
        loPoints.append((x/divisor,y/divisor))
        xLi.append(x/divisor)
        yLi.append(y/divisor)
        theoreticalAngles.append(theoreticalAngle)
        observedAngles.append(observedAngle)
        diffLi.append(abs(theoreticalAngle-observedAngle))

import matplotlib.pyplot as plt  
from matplotlib import cm
import numpy as np

plt.plot([_ for _ in range(len(observedAngles))], [abs(theoreticalAngles[i]-observedAngles[i]) for i in range(len(observedAngles))],c="black")

plt.xlabel("Data Points")  # add X-axis label
plt.ylabel("Magnitude Difference")  # add Y-axis label
plt.title("Triangulation Angle Difference")  # add title
plt.show()
'''
a1 = plt.axes(projection='3d')

a1.plot_trisurf(xLi,yLi,np.array(theoreticalAngles))
a1.plot_trisurf(xLi,yLi,np.array(observedAngles))

plt.xlabel("Points")  # add X-axis label
plt.ylabel("Points")  # add Y-axis label
a1.set_zlabel("Angles")  # add Z-axis label
plt.title("Triangulation Angle Sensor")  # add title
plt.show()
'''
ax = plt.axes(projection='3d')

surf = ax.plot_trisurf(xLi,yLi,np.array(diffLi),cmap=cm.jet)

plt.colorbar(surf, shrink=0.5, aspect=5)

ax.view_init(-90,-90)

plt.xlabel("X Data Points")  # add X-axis label
plt.ylabel("Y Data Points")  # add Y-axis label
plt.title("Triangulation Angle Difference")  # add title
plt.show()
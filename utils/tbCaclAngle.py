from calculateAngle import calculateAngle,calculateTime

angles = [_ for _ in range(0,361,1)]
sourcePosition = (0.2,0.2)

theoreticalAngles = []
observedAngles = []

for ind,val in enumerate(angles):
    timeObject,theoreticalAngle = calculateTime(sourcePosition,angles[ind],returnSourceAngle=True)
    observedAngle = calculateAngle(timeObject)
    theoreticalAngles.append(theoreticalAngle)
    observedAngles.append(observedAngle)
    print(val,theoreticalAngle,observedAngle)

import matplotlib.pyplot as plt  
  
plt.plot(angles, theoreticalAngles)
plt.plot(angles, observedAngles)

plt.xlabel("Orientation")  # add X-axis label
plt.ylabel("Inference")  # add Y-axis label
plt.title("Triangulation Angle Sensor")  # add title
plt.show()
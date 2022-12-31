def basePlot(room,currentSource,pointsOfInterestX,pointsOfInterestY):
    pltObj = room.plot(True) # Visualizing the room

    pltObj.plot(pointsOfInterestX+[pointsOfInterestX[0]],pointsOfInterestY+[pointsOfInterestY[0]],c="cyan")

    # plotting the input points as large yellow circles
    pltObj.scatter(pointsOfInterestX,pointsOfInterestY,c="orange",s=55)

    pltObj.scatter([currentSource[0]],[currentSource[1]],c="black",s=10)

    return pltObj
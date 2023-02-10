from matplotlib import pyplot as plt

with open("./source.txt","r") as inputFile:
    rawData = inputFile.read()

arrayOfEntries = rawData.split("$$$$$")

for entry in arrayOfEntries:
    arrayOfArrays = entry.split("\n\n")[:-1]
    for ind,arr in enumerate(arrayOfArrays):
        if(ind!=4):
            arrayOfArrays[ind] = list(map(float,arr.split(",")[:-1]))
            plt.plot([_ for _ in range(len(arrayOfArrays[ind]))],arrayOfArrays[ind])
            plt.show()
        else:
            print(arrayOfArrays[ind])
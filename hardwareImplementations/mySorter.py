def segregater(a0a): # array of arrays

    array0categories = []

    for arr in a0a:
        category = None
        lessThan4250 = len([_ for _ in arr if _ < 4250])
        moreThan10_000 = len([_ for _ in arr if _ > 10_000])
        commonFreq = len([_ for _ in arr if 4250<=_<=10_000])

        if(lessThan4250>0):
            category = "A"
        elif(moreThan10_000>0):
            category = "C"
        elif(commonFreq>0):
            category = "B"

        array0categories.append(category)

    return(array0categories)

def infer(arr,bins,freq=44100):
    finalArr = []
    tArr = []

    ind = 0
    while(len(finalArr)<3 and ind<len(arr)):
        categ = arr[ind]
        if(categ not in finalArr):
            finalArr.append(categ)
            tArr.append(bins[ind])
        ind+=1

    t = 1/freq

    deltaTs = []

    try:
        deltaTs.append((tArr[1] - tArr[0])*t)
        deltaTs.append((tArr[2] - tArr[1])*t)
    except Exception as e:
        print(tArr,e)

    return(finalArr,deltaTs)
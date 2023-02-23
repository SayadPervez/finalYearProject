from math import cos,pi

FFT_FORWARD = 0x01
FFT_REVERSE = 0x00
FFT_HAMMING = 0x01

def Exponent(value):
    result = 0
    while (((value >> result) & 1) != 1):
        result+=1
    return(result)

def Compute(vReal,vImag,samples,dir):
    return _Compute(vReal,vImag,samples,Exponent(samples),dir)

def _Compute(vReal,vImag,samples,power,dir):
    j = 0
    for i in range(0,samples-1):
        if(i<j):
            vReal[i],vReal[j] = vReal[j],vReal[i]
            if(dir==FFT_REVERSE):
                vImag[i],vImag[j] = vImag[j],vImag[i]
        k = samples >> 1
        while(k<=j):
            j-=k
            k = k>>1
        j+=k

    c1 = -1.0
    c2 = 0.0
    l2 = 1

    l = 0
    while(l<power):
        l1 = l2
        l2 = l2<<1
        u1 = 1.0
        u2 = 0.0
        for j in range(0,l1):
            i = j
            for i in range(i,samples,l2):
                i1 = i+l1
                t1 = u1*vReal[i1] - u2*vImag[i1]
                t2 = u1*vImag[i1] - u2*vReal[i1]
                vReal[i1] = vReal[i] - t1
                vImag[i1] = vImag[i] - t2
                vReal[i]+=t1
                vImag[i]+=t2
            z = ((u1*c1)-(u2*c1))
            u2 = ((u1*c2)+(u2*c1))
            u1 = z

        c2 = ((1.0-c1)/2.0)**0.5
        c1 = ((1.0+c1)/2.0)**0.5

        if(dir==FFT_FORWARD):
            c2 = -c2

        l+=1

    if(dir!=FFT_FORWARD):
        for i in range(0,samples):
            vReal[i]/=samples
            vImag[i]/=samples

    return (vReal,vImag)

def ComplexToMagnitude(vReal,vImag,samples):
    for i in range(0,samples):
        vReal[i] = (vReal[i]**2 + vImag[i]**2)**0.5

    return(vReal,vImag)

def Windowing(vData,samples,windowType,dir):
    samplesMinusOne = float(samples)-1.0
    for i in range(0,samples>>1):
        indexMinusOne = float(i)
        ratio = indexMinusOne/samplesMinusOne
        weighingFactor = 0.54 - (0.46 * cos(2*pi*ratio))

        if(dir==FFT_FORWARD):
            vData[i]*weighingFactor
            vData[samples - (i+1)]*=weighingFactor

        else:
            vData[i] /= weighingFactor
            vData[samples - (i+1)] /=weighingFactor

    return vData

def MajorPeak(vD,samples,samplingFrequency):

    maxY = 0
    IndexOfMaxY = 0

    for i in range(1,((samples>>1) + 1)):
        if((vD[i-1] < vD[i]) and (vD[i] > vD[i+1])):
            if(vD[i]>maxY):
                maxY = vD[i]
                IndexOfMaxY = i

    delta = 0.5 * ((vD[IndexOfMaxY-1] - vD[IndexOfMaxY+1]) / (vD[IndexOfMaxY-1] - (2.0 * vD[IndexOfMaxY]) + vD[IndexOfMaxY+1]))
    interpolatedX = ((IndexOfMaxY + delta)  * samplingFrequency) / (samples-1)

    if(IndexOfMaxY==(samples >> 1)):
        interpolatedX = ((IndexOfMaxY + delta)  * samplingFrequency) / (samples)

    return(interpolatedX)
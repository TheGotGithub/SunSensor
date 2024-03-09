def findCentroid(sunSpot):
    sumXI = []
    sumYI = []
    sumI = []
    for i in range(len(sunSpot)):
        for j in range(len(sunSpot[0])):
            sumXI.append(j*sunSpot[i][j])
            sumI.append(sunSpot[i][j])
            sumYI.append(i*sunSpot[i][j])
    Xc = sum(sumXI)/sum(sumI)
    Yc = sum(sumYI)/sum(sumI)
    return Xc,Yc

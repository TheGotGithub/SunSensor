class SunSpot:
    def __init__(self) -> None:
        pass

    def findSunSpot(self,rawData):
        row_data = []
        colum_data = []
        for i in range(len(rawData)) :
            mData = 0
            for j in range(len(rawData[i])):
                mData += rawData[i][j]
            mData = mData/len(rawData[0])
            row_data.append(mData)

        for i in range(len(rawData[0])) :
            mData = 0
            for j in range(len(rawData)) :
                mData += rawData[j][i]
            mData = mData/len(rawData)
            colum_data.append(mData)

        peakPoint = [row_data.index(max(row_data)),colum_data.index(max(colum_data))]
        roiData = [row_data,colum_data]
        return peakPoint , roiData[1] ,roiData[0]
    
    def roiFill(self,peakPoint,rawData):
        fillData = rawData[peakPoint[0]-15:peakPoint[0]+15]
        fillData2 = []
        for i in range(len(fillData)):
            fillData2.append(fillData[i][peakPoint[1]-10:peakPoint[1]+10].copy())
            for j in range(len(fillData2[-1])):
                if fillData2[-1][j] <=170 : fillData2[-1][j] = 0

        return fillData2
    
    def findCentroid(self,sunSpot):
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

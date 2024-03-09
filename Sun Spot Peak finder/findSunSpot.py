import imageGen as data_gen

# loade  image
def findSunSpot(rawData):
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
    # print('Peak Point = ',peakPoint)
    return peakPoint , roiData

def sunSpotShow(peakPoint,rawData,roiData):
    #Select Sun Spot
    fillData = rawData[peakPoint[0]-15:peakPoint[0]+15]
    fillData2 = []
    for i in range(len(fillData)):
        fillData2.append(fillData[i][peakPoint[1]-10:peakPoint[1]+10].copy())
        for j in range(len(fillData2[-1])):
            if fillData2[-1][j] <=170 : fillData2[-1][j] = 0

    # print(range(len(peakPoint[0])))
    # print(len(fillData2))
    # data_gen.sunSpotPlot(rawData,fillData2,roiData[0],roiData[1])
    return fillData2

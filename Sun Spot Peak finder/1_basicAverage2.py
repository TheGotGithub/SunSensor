import imageGen as data_gen

#Gen Sun Spot Image
sensor_width = 752  
sensor_height = 480  
 
rawData = data_gen.genSunSpot(sensor_height, sensor_width,400,200,10)

# loade  image
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
print('Peak Point = ',peakPoint)

#Select Sun Spot
fillData = rawData[peakPoint[0]-15:peakPoint[0]+15]
fillData2 = []
for i in range(len(fillData)):
    fillData2.append(fillData[i][peakPoint[1]-15:peakPoint[1]+15].copy())
    for j in range(len(fillData2[-1])):
        if fillData2[-1][j] <=125 : fillData2[-1][j] = 0

# print(range(len(peakPoint[0])))
data_gen.sunSpotPlot(rawData,fillData2,row_data,colum_data)

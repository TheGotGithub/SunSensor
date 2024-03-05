
import imageGen as data_gen
row_data = []
colum_data = []

sensor_width = 752  # Number of pixels in the sensor width
sensor_height = 480  # Number of pixels in the sensor height
 
rawData = data_gen.genSunSpot(sensor_height, sensor_width,400,200,10)

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

# rawData[peakPoint[0]][peakPoint[1]] = 0
fillData = rawData[peakPoint[0]-15:peakPoint[0]+15]
fillData2 = []
for i in range(len(fillData)):
    fillData2.append(fillData[i][peakPoint[1]-15:peakPoint[1]+15].copy())
    for j in range(len(fillData2[-1])):
        if fillData2[-1][j] <=125 : fillData2[-1][j] = 0

# print(fillData2)
print('Peak Point = ',peakPoint)
data_gen.sunSpotPlot(rawData,fillData2)
# data_gen.sunSpotPlot3D(rawData)
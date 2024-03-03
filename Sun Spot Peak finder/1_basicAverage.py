

import imageGen as data_gen
row_data = []
colum_data = []

rawData = data_gen.genSunSpot(500,300,50)
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
fillData = rawData[peakPoint[0]-50:peakPoint[0]+50]
fillData2 = []
for i in range(len(fillData)):
    fillData2.append(fillData[i][peakPoint[1]-50:peakPoint[1]+50])

print(fillData2)
print('Peak Point = ',peakPoint)
data_gen.sunSpotPlot(rawData,fillData2)
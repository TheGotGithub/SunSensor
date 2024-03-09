import imageGen as data_gen
import findSunSpot
import findCentroid
#Gen Sun Spot Image
sensor_width = 752  
sensor_height = 480  
rawData = data_gen.genSunSpot(sensor_height, sensor_width,470,300,10)

peakPoint , roiData = findSunSpot.findSunSpot(rawData)

fillData = findSunSpot.sunSpotShow(peakPoint,rawData,roiData)
Xc,Yc = findCentroid.findCentroid(fillData)
print(Xc,Yc)
fillData[int(Yc)][int(Xc)] = 0
data_gen.sunSpotPlot(rawData,fillData,roiData[0],roiData[1])

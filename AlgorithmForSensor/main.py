# Importing necessary modules
from Genarate_row_data_CMOS import CMOS_sensor
from Process_Sun_Sensor import SunSpot
import math

# Creating instances of CMOS sensor and SunSpot detector
data = CMOS_sensor.CMOS_Sensor()
sunSpot = SunSpot.SunSpot()

# Setting parameters for the sensor and noise
sensor_width = 752  
sensor_height = 480  
width_pos = 700  
height_pos = 240
noiseVal = 5  

data.h = 0.8
data.coordinateX = sensor_width/2
data.coordinateY = sensor_height/2
data.Px = 6*(10**-3)
data.Py = 6*(10**-3)

# Generating simulated sun spot data with noise
data.genSunSpot(sensor_height, sensor_width, width_pos, height_pos, noiseVal)

# Finding peak point and sum values along rows and columns for sun spot detection
data.peakPoint, data.sumRowVal, data.sumColVal = sunSpot.findSunSpot(data.rawData)

# Filling the region of interest (ROI) based on the detected sun spot
data.roiData = sunSpot.roiFill(data.peakPoint, data.rawData)

# Finding the centroid of the ROI
data.Xc, data.Yc = sunSpot.findCentroid(data.roiData)

# Setting the centroid pixel value to 0 to remove the sun spot from the ROI data
data.roiData[math.ceil(data.Yc)][math.ceil(data.Xc)] = 0

# Printing the centroid coordinates
print(data.Xc, data.Yc)
print(math.ceil(data.Xc), math.ceil(data.Yc))

# Plotting the sun spot
data.sunSpotPlot()

data.alpha ,data.beta = sunSpot.findAngle(data.peakPoint[1],data.peakPoint[0],data.coordinateX,data.coordinateY,data.Px,data.Py,data.h)


print("Peak X : ",data.peakPoint[1])
print("Peak Y : ",data.peakPoint[0])
print("Alpha : ",data.alpha)
print("Beta : ",data.beta)
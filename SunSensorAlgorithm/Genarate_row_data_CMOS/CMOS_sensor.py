import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys
sys.path.append("SunSensorAlgorithm/Genarate_row_data_CMOS/")  
from CMOS_dataType import CMOS_datatype  

class CMOS_Sensor(CMOS_datatype):
    # def __init__(self):
    #     self.sensorData = []
    #     self.sun_intensity = 1000 
    #     print(self.rawData)

    def genSunSpot(self, sensor_height, sensor_width, width_pos, height_pos, noiseVal):
        # Create a 2D array to represent the sensor
        sensor_data = np.zeros((sensor_height, sensor_width))

        # Simulate sunlight hitting the sensor
        sun_position = (width_pos, height_pos)  # Assuming the sun is at the center of the sensor for simplicity

        for y in range(sensor_height):
            for x in range(sensor_width):
                # Calculate the distance between the current pixel and the sun
                distance_to_sun = np.sqrt((x - sun_position[0])**2 + (y - sun_position[1])**2)
                
                # Calculate the intensity of sunlight hitting the current pixel
                intensity = 1000 / (distance_to_sun + 1)  # Inverse square law
                
                # Add noise to simulate sensor imperfections
                noise = np.random.normal(0, noiseVal)  # Gaussian noise
                
                # Assign the intensity to the pixel in the sensor data array
                sensor_data[y, x] = intensity + noise

        # Add some additional noise to the entire sensor data to simulate sensor noise
        sensor_data += np.random.normal(0, 2, size=(sensor_height, sensor_width))

        # Clip the sensor data to ensure it's within a valid range (0 to 255)
        sensor_data = np.clip(sensor_data, 0, 255)

        # Convert the sensor data to integers (raw data)
        sensor_data = sensor_data.astype(np.uint8)
        self.rawData = sensor_data.tolist()

    # @staticmethod
    def sunSpotPlot(self):
        fig = plt.figure(figsize=(10,7))
        
        if self.rawData!=None:
            fig.add_subplot(2,2,1)
            plt.imshow(self.rawData, cmap='gray')
            plt.colorbar(label='Intensity')
            plt.title('Sun Sensor Data')
        
        if self.roiData!=None:
            fig.add_subplot(2,2,4)
            plt.imshow(self.roiData, cmap='gray')
            plt.colorbar(label='Intensity')
            plt.title('Sun Sensor Fill Data')

        if self.sumColVal!= None:
            col = list(reversed(self.sumColVal)).copy()
            fig.add_subplot(2,2,2)
            x1 = np.linspace(0,1,len(col))
            plt.plot(col,x1)

        if self.sumRowVal!= None:
            fig.add_subplot(2,2,3)
            x2 = np.linspace(0,1,len(self.sumRowVal))
            plt.plot(x2,self.sumRowVal)

        plt.show()

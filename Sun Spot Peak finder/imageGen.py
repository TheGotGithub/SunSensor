import numpy as np
import matplotlib.pyplot as plt

# Define sensor parameters
sensor_width = 752  # Number of pixels in the sensor width
sensor_height = 480  # Number of pixels in the sensor height
sun_intensity = 1000  # Intensity of sunlight hitting the sensor (arbitrary units)
def genSunSpot(width_pos,height_pos,noiseVal):
    # Create a 2D array to represent the sensor
    sensor_data = np.zeros((sensor_height, sensor_width))

    # Simulate sunlight hitting the sensor
    sun_position = (width_pos, height_pos)  # Assuming the sun is at the center of the sensor for simplicity

    for y in range(sensor_height):
        for x in range(sensor_width):
            # Calculate the distance between the current pixel and the sun
            distance_to_sun = np.sqrt((x - sun_position[0])**2 + (y - sun_position[1])**2)
            
            # Calculate the intensity of sunlight hitting the current pixel
            intensity = sun_intensity / (distance_to_sun + 1)  # Inverse square law
            
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
    return sensor_data

# Now sensor_data contains the simulated raw data from the CMOS array sun sensor
def sunSpotPlot(sensor_data,sensor_data2):

    fig = plt.figure(figsize=(10,7))
    
    fig.add_subplot(1,2,1)
    plt.imshow(sensor_data)
    plt.colorbar(label='Intensity')
    plt.title('Sun Sensor Data')
    # plt.xlabel('Pixels')
    # plt.ylabel('Pixels')
    
    fig.add_subplot(1,2,2)
    plt.imshow(sensor_data2)
    plt.colorbar(label='Intensity')
    plt.title('Sun Sensor Fill Data')
    # plt.xlabel('Pixels')
    # plt.ylabel('Pixels')

    plt.show()


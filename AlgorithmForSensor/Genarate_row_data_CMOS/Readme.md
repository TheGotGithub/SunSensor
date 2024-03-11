# CMOS Sensor Simulation

This repository contains code for simulating a CMOS sensor capturing data from a simulated sun spot. The simulation includes generating sensor data with noise and plotting various aspects of the sensor output.

## Files

- **CMOS_dataType.py**: Defines the `CMOS_datatype` class, which serves as a base class for storing sensor data and related attributes. It includes methods for printing and clearing attributes.

- **CMOS_Sensor.py**: Implements the `CMOS_Sensor` class, which inherits from `CMOS_datatype`. This class generates simulated sun spot data, adds noise, plots the sensor data, and provides methods for plotting various aspects of the data.

## Usage

1. **Setting up the Environment**: Ensure you have Python installed on your system. You might need to install additional libraries like NumPy and Matplotlib if not already installed. You can install them via pip:

    ```bash
    pip install numpy
    pip install matplotlib
    ```

2. **Generating Sensor Data**: You can use the `genSunSpot` method of the `CMOS_Sensor` class to generate simulated sensor data. This method simulates sunlight hitting the sensor and adds noise to mimic real-world imperfections.

3. **Plotting Sensor Data**: The `sunSpotPlot` method of the `CMOS_Sensor` class plots various aspects of the generated sensor data, including the raw data, region of interest data, row and column sums, etc.

## Example

```python
from CMOS_Sensor import CMOS_Sensor

# Create an instance of CMOS_Sensor
sensor = CMOS_Sensor()

# Generate sun spot data with specified parameters
sensor.genSunSpot(sensor_height=100, sensor_width=100, width_pos=50, height_pos=50, noiseVal=5)

# Plot the sensor data
sensor.sunSpotPlot()

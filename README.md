## STM32-Based CubeSat Sun Sensor Prototype with COTS Components

This project aims to develop a Sun Sensor prototype for CubeSats using off-the-shelf components. The main contents are divided into three major parts:

<img width="828" alt="image" src="https://github.com/TheGotGithub/SunSensor/assets/104858772/350a54eb-12d9-4fef-ba18-baafdecfdf9c">

### Algorithm
In this section, fundamental algorithms necessary for data reading and basic processing analysis are discussed:

1. **Sun Spot Detected (find ROI):** This algorithm focuses on detecting the sun spot and finding the Region of Interest (ROI).
   - [Sun Spot Detected (find ROI)](https://www.notion.so/Sun-Spot-Detected-find-ROI-d0d4dd2c118742b09f39f3ce9d2593d6?pvs=21)

2. **Sun Spot Centroid:** This algorithm calculates the centroid of the detected sun spot.
   - [Sun Spot Centroid](https://www.notion.so/Sun-Spot-Centroid-727f3aa5d62d410a89342f2ce6f7c4fd?pvs=21)

3. **Sun Angles:** This algorithm determines the angles of the sun relative to the CubeSat.
   - [Sun Angles](https://www.notion.so/Sun-Angles-f7b60984959d421d9d065ef3971e3ed9?pvs=21)

### Implement
This section involves further development and adaptation of the aforementioned algorithms to work efficiently on the STM32 (ARM Architecture) platform.

### Interface
This section focuses on studying the interface with CMOS and selecting the appropriate controller.

---

**Note:** This README is a work in progress and will be updated with more detailed information. Stay tuned for further updates!

---


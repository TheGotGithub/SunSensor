import imageGen as data_gen

sensor_width = 100  # Number of pixels in the sensor width
sensor_height = 100  # Number of pixels in the sensor height
 
rawData = data_gen.genSunSpot(sensor_height, sensor_width,70,30,10)
rawData2 = rawData
startState=[int(len(rawData[0])/2),int(len(rawData)/2)]
# print(startState)
# data_gen.sunSpotPlot(rawData,rawData)
def greedyAlgorithm(startState):
    currentState = startState
    while(True):
        env = [rawData[currentState[1]-1][currentState[0]],
            rawData[currentState[1]][currentState[0]+1],
            rawData[currentState[1]+1][currentState[0]],
            rawData[currentState[1]][currentState[0]]-1]
        envMax = env.index(max(env))
        print(rawData[currentState[1]][currentState[0]] ,max(env))
        if rawData[currentState[0]][currentState[1]] <= max(env):
            rawData[currentState[0]][currentState[1]] = 0
            if envMax == 0 : currentState = [currentState[1]-1,currentState[0]]
            elif envMax == 1 : currentState = [currentState[1],currentState[0]+1]
            elif envMax == 2 : currentState = [currentState[1]+1,currentState[0]]
            else : currentState = [currentState[1],currentState[0]-1]
            print(currentState , envMax ,rawData[currentState[1]][currentState[0]])
        else : 
            print(currentState)
            break

    # print(env)

greedyAlgorithm(startState)
# print(len(rawData)/2)

data_gen.sunSpotPlot(rawData,rawData2)
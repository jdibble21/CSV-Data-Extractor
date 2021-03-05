# Choose 4 attributes from 100 rows, normalize numeric vals and compute distance between row values

import pandas as pd
import math

def normalizeDataframe(dataframe):
    MAX = dataframe.max()
    MIN = dataframe.min()
    dataframe = dataframe.astype(float)
    for i in range(0,len(dataframe)):
        value = float(dataframe[i])
        normValue = float((value - MIN)/(MAX-MIN))
        dataframe[i] = math.fabs(normValue)
    return dataframe

def calculateTwoRecordDistance(num1rec1,num1rec2,num2rec1,num2rec2,ordDistance,catDistance):
    #example: index = 8,38 need num1[8] - num1[38] + num2[8] - num2[38] + ordDistance + catDistance
    distance = math.fabs(num1rec1 - num1rec2) + math.fabs(num2rec1 - num2rec2) + ordDistance + catDistance
    return distance * 0.25

def calculateOrdinalDistance(ordDataframe,d1,d2):
    valDict = {
        "A": 0.25,
        "B":0.50,
        "C":0.75,
        "D":1
    }
    #First record data
    record1 = ordDataframe[d1]
    record1Letter = record1[0]
    record1NumVal = float(record1[1:3])
    record1Distance = valDict[record1Letter] + (record1NumVal*0.001)

    #Second record data
    record2 = ordDataframe[d2]
    record1Letter = record2[0]
    record1NumVal = float(record2[1:3])
    record2Distance = valDict[record1Letter] + (record1NumVal*0.001)

    return math.fabs(record1Distance - record2Distance)
        
def calculateCategoricalDistance(catDataframe,d1,d2):
    valDict = {
        "outoftime": 0.25,
        "resign":0.50,
        "mate":0.75,
        "draw":1
    }
    #First record data
    record1 = valDict[catDataframe[d1]]

    #Second record data
    record2 = valDict[catDataframe[d2]]
    return math.fabs(record1 - record2)

R8 = 8
R38 = 38
R73 = 73

pd.set_option('display.max_rows', None)
data = pd.read_csv("cs455_homework3_dataset_dibble.csv")

numericData1 = data['white_rating']
numericData2 = data['black_rating']
categoricalData = data['victory_status']
numericData1 = normalizeDataframe(numericData1)
numericData2 = normalizeDataframe(numericData2)
ordinalData = data['opening_eco']

# FIRST COMPUTATION
# Calculate Distance between record 8 and 38
ordDistance = calculateOrdinalDistance(ordinalData,R8,R38)
categoricalDistance = calculateCategoricalDistance(categoricalData,R8,R38)
print("== FIRST COMPUTATION ==")
print("Final Distance between record 8 and 38: ",calculateTwoRecordDistance(numericData1[R8],numericData1[R38],numericData2[R8],numericData2[R38],ordDistance,categoricalDistance),"\n")

# SECOND COMPUTATION
# Calculate Distance between record 38 and 73
ordDistance = calculateOrdinalDistance(ordinalData,R38,R73)
categoricalDistance = calculateCategoricalDistance(categoricalData,R38,R73)
print("Final Distance between record 38 and 73: ",calculateTwoRecordDistance(numericData1[R38],numericData1[R73],numericData2[R38],numericData2[R73],ordDistance,categoricalDistance),"\n")

# THIRD COMPUTATION
# Calculate Distance between record 8 and 73
ordDistance = calculateOrdinalDistance(ordinalData,R8,R73)
categoricalDistance = calculateCategoricalDistance(categoricalData,R8,R73)
print("Final Distance between record 8 and 73: ",calculateTwoRecordDistance(numericData1[R8],numericData1[R73],numericData2[R8],numericData2[R73],ordDistance,categoricalDistance),"\n")



